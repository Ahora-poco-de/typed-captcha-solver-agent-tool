from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol
from urllib.parse import urlparse

from .models import SCHEMA_VERSION, InputError, SolveRequest, ToolResult


class SolverClient(Protocol):
    def solve(self, request: SolveRequest) -> tuple[str, str | None]: ...


@dataclass
class TypedCaptchaSolverTool:
    client: SolverClient
    allowed_origins: frozenset[str]
    max_calls: int = 1
    _calls: int = 0
    _request_ids: set[str] = field(default_factory=set)

    def invoke(self, arguments: dict[str, Any]) -> dict[str, str | None]:
        request_id = str(arguments.get("request_id") or "unknown")
        try:
            request = SolveRequest.from_mapping(arguments)
        except InputError as exc:
            return ToolResult(SCHEMA_VERSION, request_id, "stopped", stop_reason=str(exc)).to_mapping()

        origin = f"{urlparse(request.target_origin).scheme}://{urlparse(request.target_origin).netloc}"
        if origin not in self.allowed_origins:
            return ToolResult(SCHEMA_VERSION, request.request_id, "stopped", stop_reason="origin_not_allowed").to_mapping()
        if request.request_id in self._request_ids:
            return ToolResult(SCHEMA_VERSION, request.request_id, "stopped", stop_reason="duplicate_request_id").to_mapping()
        if self._calls >= self.max_calls:
            return ToolResult(SCHEMA_VERSION, request.request_id, "stopped", stop_reason="call_budget_exhausted").to_mapping()

        self._request_ids.add(request.request_id)
        self._calls += 1
        try:
            text, task_id = self.client.solve(request)
        except Exception as exc:  # returned as data so an agent can stop safely
            return ToolResult(
                SCHEMA_VERSION,
                request.request_id,
                "error",
                stop_reason=f"solver_error:{type(exc).__name__}",
            ).to_mapping()
        return ToolResult(SCHEMA_VERSION, request.request_id, "solved", text=text, task_id=task_id).to_mapping()

