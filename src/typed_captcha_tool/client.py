from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Protocol
from urllib.request import Request, urlopen

from .models import SolveRequest

CREATE_TASK_URL = "https://api.capsolver.com/createTask"


class Transport(Protocol):
    def post_json(self, url: str, payload: dict, timeout_seconds: float) -> dict: ...


class UrllibTransport:
    def post_json(self, url: str, payload: dict, timeout_seconds: float) -> dict:
        request = Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request, timeout=timeout_seconds) as response:
            return json.loads(response.read().decode("utf-8"))


@dataclass
class CapSolverImageToTextClient:
    api_key: str
    transport: Transport
    timeout_seconds: float = 20.0

    def solve(self, request: SolveRequest) -> tuple[str, str | None]:
        task = {
            "type": "ImageToTextTask",
            "body": request.image_base64,
            "module": request.module,
            "websiteURL": request.target_origin,
        }
        response = self.transport.post_json(
            CREATE_TASK_URL,
            {"clientKey": self.api_key, "task": task},
            self.timeout_seconds,
        )
        if response.get("errorId"):
            code = response.get("errorCode") or "CAPSOLVER_ERROR"
            description = response.get("errorDescription") or "task failed"
            raise RuntimeError(f"{code}: {description}")
        if response.get("status") != "ready":
            raise RuntimeError("ImageToTextTask did not return a synchronous ready result")
        text = response.get("solution", {}).get("text")
        if not isinstance(text, str) or not text:
            raise RuntimeError("response did not include solution.text")
        return text, response.get("taskId")

