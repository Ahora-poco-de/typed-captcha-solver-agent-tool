# Ferramenta tipada de CAPTCHA Solver para agentes de IA

[English](../../README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Español](../es/README.md) · [Português](README.md) · [한국어](../ko/README.md)

## Introduction

Agentes podem produzir argumentos incompletos, valores inesperados ou alvos fora do escopo autorizado. Este projeto valida um Schema estrito, a origem exata, o orçamento de chamadas e o ID antes de qualquer solicitação externa. O adaptador do [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=typed-captcha-solver-agent-tool&utm_content=repository-readme) usa somente os campos oficiais de `ImageToTextTask`; a demonstração padrão é totalmente offline.

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest -q && python scripts/smoke.py
```

## Responsible Use

Use o projeto apenas em sistemas próprios ou com autorização explícita para QA ou RPA. Restrinja alvos, chamadas e retenção, e encaminhe entradas ou respostas inesperadas para revisão humana. Não use para dados privados, para evitar medidas da plataforma ou para criação de contas em massa.

## Conclusion

Separar o framework, a política local e a solicitação síncrona permite testar cada limite e manter o contrato alinhado à documentação oficial do [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=typed-captcha-solver-agent-tool&utm_content=repository-readme).

## Maintainer Note

Developer sharing CapSolver integration examples.

## License

[MIT](../../LICENSE)
