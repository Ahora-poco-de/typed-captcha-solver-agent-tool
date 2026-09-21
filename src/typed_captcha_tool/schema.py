from __future__ import annotations


def tool_schema() -> dict:
    """Return a framework-neutral function-tool schema."""
    return {
        "name": "solve_authorized_image_captcha",
        "description": (
            "Read a text CAPTCHA image from an explicitly authorized QA or RPA target. "
            "The caller must provide a written authorization reference and exact origin."
        ),
        "parameters": {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "schema_version",
                "request_id",
                "authorization_ref",
                "target_origin",
                "image_base64",
            ],
            "properties": {
                "schema_version": {"type": "string", "const": "1.0"},
                "request_id": {"type": "string", "minLength": 1, "maxLength": 80},
                "authorization_ref": {"type": "string", "minLength": 1, "maxLength": 120},
                "target_origin": {"type": "string", "format": "uri"},
                "image_base64": {
                    "type": "string",
                    "description": "Base64 image bytes without a data URL prefix.",
                },
                "module": {"type": "string", "enum": ["common", "number"], "default": "common"},
            },
        },
    }

