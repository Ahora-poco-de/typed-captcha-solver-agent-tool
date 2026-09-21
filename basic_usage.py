import base64

from typed_captcha_tool import TypedCaptchaSolverTool, tool_schema


class FixtureClient:
    def solve(self, request):
        return "QA42", "fixture-task-1"


tool = TypedCaptchaSolverTool(
    client=FixtureClient(),
    allowed_origins=frozenset({"https://qa.example.test"}),
)

arguments = {
    "schema_version": "1.0",
    "request_id": "demo-001",
    "authorization_ref": "QA-CHANGE-42",
    "target_origin": "https://qa.example.test",
    "image_base64": base64.b64encode(b"owned-fixture").decode(),
    "module": "common",
}

print(tool_schema()["name"])
print(tool.invoke(arguments))

