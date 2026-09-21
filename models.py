from __future__ import annotations

import base64
import binascii
from dataclasses import dataclass
from typing import Any, Literal
from urllib.parse import urlparse

SCHEMA_VERSION = "1.0"
MAX_IMAGE_BYTES = 750_000


class InputError(ValueError):
    """Raised when model-produced tool arguments fail local validation."""


@dataclass(frozen=True)
class SolveRequest:
    schema_version: str
    request_id: str
    authorization_ref: str
    target_origin: str
    image_base64: str
    module: Literal["common", "number"] = "common"

    @classmethod
    def from_mapping(cls, value: dict[str, Any]) -> "SolveRequest":
        allowed = {
            "schema_version",
            "request_id",
            "authorization_ref",
            "target_origin",
            "image_base64",
            "module",
        }
        unknown = sorted(set(value) - allowed)
        if unknown:
            raise InputError(f"unknown fields: {', '.join(unknown)}")

        required = allowed - {"module"}
        missing = sorted(name for name in required if not value.get(name))
        if missing:
            raise InputError(f"missing fields: {', '.join(missing)}")

        if value["schema_version"] != SCHEMA_VERSION:
            raise InputError(f"unsupported schema_version: {value['schema_version']}")

        module = value.get("module", "common")
        if module not in {"common", "number"}:
            raise InputError("module must be common or number")

        parsed = urlparse(str(value["target_origin"]))
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            raise InputError("target_origin must be an absolute HTTP(S) origin")
        if parsed.path not in {"", "/"} or parsed.query or parsed.fragment:
            raise InputError("target_origin must not contain a path, query, or fragment")

        try:
            decoded = base64.b64decode(value["image_base64"], validate=True)
        except (binascii.Error, ValueError) as exc:
            raise InputError("image_base64 must be valid base64 without a data URL prefix") from exc
        if not decoded:
            raise InputError("image_base64 must not decode to an empty payload")
        if len(decoded) > MAX_IMAGE_BYTES:
            raise InputError(f"decoded image exceeds {MAX_IMAGE_BYTES} bytes")

        return cls(
            schema_version=SCHEMA_VERSION,
            request_id=str(value["request_id"]),
            authorization_ref=str(value["authorization_ref"]),
            target_origin=f"{parsed.scheme}://{parsed.netloc}",
            image_base64=str(value["image_base64"]),
            module=module,
        )


@dataclass(frozen=True)
class ToolResult:
    schema_version: str
    request_id: str
    status: Literal["solved", "stopped", "error"]
    text: str | None = None
    stop_reason: str | None = None
    task_id: str | None = None

    def to_mapping(self) -> dict[str, str | None]:
        return {
            "schema_version": self.schema_version,
            "request_id": self.request_id,
            "status": self.status,
            "text": self.text,
            "stop_reason": self.stop_reason,
            "task_id": self.task_id,
        }

