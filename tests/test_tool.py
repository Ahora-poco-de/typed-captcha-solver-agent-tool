import base64

from typed_captcha_tool import TypedCaptchaSolverTool, tool_schema


class FakeClient:
    def __init__(self, error=False):
        self.error = error
        self.calls = 0

    def solve(self, request):
        self.calls += 1
        if self.error:
            raise TimeoutError("fixture timeout")
        return "QA42", "fixture-task-1"


def valid_arguments(**updates):
    value = {
        "schema_version": "1.0",
        "request_id": "req-1",
        "authorization_ref": "QA-42",
        "target_origin": "https://qa.example.test",
        "image_base64": base64.b64encode(b"fixture").decode(),
        "module": "common",
    }
    value.update(updates)
    return value


def make_tool(client=None):
    return TypedCaptchaSolverTool(client or FakeClient(), frozenset({"https://qa.example.test"}))


def test_schema_rejects_extra_properties():
    assert tool_schema()["parameters"]["additionalProperties"] is False


def test_valid_request_is_solved():
    result = make_tool().invoke(valid_arguments())
    assert result["status"] == "solved"
    assert result["text"] == "QA42"


def test_unknown_field_stops_before_client():
    client = FakeClient()
    result = make_tool(client).invoke(valid_arguments(surprise=True))
    assert result["status"] == "stopped"
    assert client.calls == 0


def test_schema_version_is_enforced():
    result = make_tool().invoke(valid_arguments(schema_version="2.0"))
    assert result["status"] == "stopped"


def test_origin_allowlist_is_enforced():
    result = make_tool().invoke(valid_arguments(target_origin="https://other.example"))
    assert result["stop_reason"] == "origin_not_allowed"


def test_duplicate_request_id_is_idempotent():
    tool = make_tool()
    assert tool.invoke(valid_arguments())["status"] == "solved"
    assert tool.invoke(valid_arguments())["stop_reason"] == "duplicate_request_id"


def test_call_budget_is_bounded():
    tool = make_tool()
    tool.invoke(valid_arguments())
    result = tool.invoke(valid_arguments(request_id="req-2"))
    assert result["stop_reason"] == "call_budget_exhausted"


def test_client_error_is_structured_and_redacted():
    result = make_tool(FakeClient(error=True)).invoke(valid_arguments())
    assert result["status"] == "error"
    assert result["stop_reason"] == "solver_error:TimeoutError"
    assert "fixture timeout" not in str(result)

