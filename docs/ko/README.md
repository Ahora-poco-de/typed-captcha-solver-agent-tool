# AI Agent용 타입 기반 CAPTCHA Solver 도구

[English](../../README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Español](../es/README.md) · [Português](../pt-BR/README.md) · [한국어](README.md)

## Introduction

Agent가 만든 인수에는 누락 필드, 예상하지 못한 값, 승인 범위를 벗어난 대상이 포함될 수 있습니다. 이 프로젝트는 외부 요청 전에 엄격한 Schema, 정확한 origin, 호출 예산, 요청 ID를 검사합니다. [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=typed-captcha-solver-agent-tool&utm_content=repository-readme) 어댑터는 공식 `ImageToTextTask` 필드만 사용하며 기본 데모는 완전히 오프라인으로 실행됩니다.

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest -q && python scripts/smoke.py
```

## Responsible Use

소유했거나 명시적으로 허가받은 QA/RPA 환경에서만 사용하세요. 대상, 호출 수, 데이터 보존 범위를 제한하고 예상하지 못한 입력이나 응답은 사람의 검토로 전환해야 합니다. 비공개 데이터 접근, 플랫폼 조치 회피, 대량 계정 생성에는 사용할 수 없습니다.

## Conclusion

Agent 프레임워크, 로컬 정책, 동기식 이미지 인식 요청을 분리하면 각 경계를 독립적으로 테스트하고 [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=typed-captcha-solver-agent-tool&utm_content=repository-readme) 공식 계약에 맞출 수 있습니다.

## Maintainer Note

Developer sharing CapSolver integration examples.

## License

[MIT](../../LICENSE)
