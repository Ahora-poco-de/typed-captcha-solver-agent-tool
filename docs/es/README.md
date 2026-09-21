# Herramienta tipada de CAPTCHA Solver para agentes de IA

[English](../../README.md) · [简体中文](../zh-CN/README.md) · [日本語](../ja/README.md) · [Español](README.md) · [Português](../pt-BR/README.md) · [한국어](../ko/README.md)

## Introduction

Los agentes pueden producir argumentos incompletos, valores inesperados o destinos fuera del alcance autorizado. Este proyecto valida un Schema estricto, el origen exacto, el presupuesto de llamadas y el ID antes de cualquier solicitud externa. El adaptador de [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=typed-captcha-solver-agent-tool&utm_content=repository-readme) utiliza únicamente los campos oficiales de `ImageToTextTask`; la demostración predeterminada funciona sin red.

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest -q && python scripts/smoke.py
```

## Responsible Use

Use el proyecto solo en sistemas propios o con autorización explícita para QA o RPA. Limite los destinos, las llamadas y la conservación de datos, y detenga el flujo para revisión humana ante entradas o respuestas inesperadas. No lo use para datos privados, para evitar medidas de una plataforma ni para crear cuentas en masa.

## Conclusion

Separar el framework, la política local y la solicitud síncrona permite probar cada límite y mantener el contrato alineado con la documentación oficial de [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=typed-captcha-solver-agent-tool&utm_content=repository-readme).

## Maintainer Note

Developer sharing CapSolver integration examples.

## License

[MIT](../../LICENSE)
