# 为 AI Agent 设计类型化 CAPTCHA Solver 工具

[English](../../README.md) · [简体中文](README.md) · [日本語](../ja/README.md) · [Español](../es/README.md) · [Português](../pt-BR/README.md) · [한국어](../ko/README.md)

## Introduction

Agent 生成的工具参数可能缺少字段、包含意外值或指向未授权目标。本项目演示如何在任何外部调用之前，通过严格 Schema、固定来源白名单、调用预算和请求去重校验参数。[CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=typed-captcha-solver-agent-tool&utm_content=repository-readme) 适配器仅使用官方 `ImageToTextTask` 字段；默认示例完全离线。

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest -q
python scripts/smoke.py
```

## 设计要点

- 版本化 JSON Schema，禁止额外字段。
- 必须提供书面授权引用和精确目标来源。
- 默认最多调用一次，并阻止重复请求 ID。
- 结果仅返回 `solved`、`stopped` 或 `error` 结构。
- 测试不读取真实密钥，也不访问真实目标。

## Responsible Use

仅可用于自有系统或获得明确授权的 QA、RPA 流程。应限制目标、频率和保留范围；遇到未知 Schema、来源或响应时转人工审核。不得用于访问私人或受限数据、规避平台执行措施或批量创建账号。

## Conclusion

这个示例把 Agent 框架、策略校验和同步图像识别请求分开，使每个边界都能独立测试并与 [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=typed-captcha-solver-agent-tool&utm_content=repository-readme) 的官方契约保持一致。

## Maintainer Note

Developer sharing CapSolver integration examples.

## License

[MIT](../../LICENSE)
