import base64

from typed_captcha_tool.client import CREATE_TASK_URL, CapSolverImageToTextClient
from typed_captcha_tool.models import SolveRequest


class RecordingTransport:
    def __init__(self, response):
        self.response = response
        self.call = None

    def post_json(self, url, payload, timeout_seconds):
        self.call = (url, payload, timeout_seconds)
        return self.response


def request():
    return SolveRequest.from_mapping({
        "schema_version": "1.0",
        "request_id": "req-1",
        "authorization_ref": "QA-42",
        "target_origin": "https://qa.example.test",
        "image_base64": base64.b64encode(b"fixture").decode(),
        "module": "common",
    })


def test_client_uses_official_image_to_text_fields():
    transport = RecordingTransport({"errorId": 0, "status": "ready", "solution": {"text": "QA42"}, "taskId": "t1"})
    client = CapSolverImageToTextClient("placeholder", transport)
    assert client.solve(request()) == ("QA42", "t1")
    url, payload, _ = transport.call
    assert url == CREATE_TASK_URL
    assert set(payload) == {"clientKey", "task"}
    assert payload["task"]["type"] == "ImageToTextTask"


def test_client_rejects_api_error():
    transport = RecordingTransport({"errorId": 1, "errorCode": "ERROR_TEST", "errorDescription": "fixture"})
    client = CapSolverImageToTextClient("placeholder", transport)
    try:
        client.solve(request())
    except RuntimeError as exc:
        assert "ERROR_TEST" in str(exc)
    else:
        raise AssertionError("expected RuntimeError")

