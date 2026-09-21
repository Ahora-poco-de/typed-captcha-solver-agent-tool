# AI Agent 向け型付き CAPTCHA Solver ツール

[English](../../README.md) · [简体中文](../zh-CN/README.md) · [日本語](README.md) · [Español](../es/README.md) · [Português](../pt-BR/README.md) · [한국어](../ko/README.md)

## Introduction

Agent が生成する引数には、欠落フィールド、未定義値、許可されていない対象が含まれる場合があります。本リポジトリは、外部呼び出し前に厳格な Schema、オリジン許可リスト、呼び出し上限、リクエスト ID を検証します。[CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=typed-captcha-solver-agent-tool&utm_content=repository-readme) アダプターは公式 `ImageToTextTask` フィールドだけを使用し、既定のデモは完全にオフラインです。

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest -q && python scripts/smoke.py
```

## Responsible Use

所有または明示的な許可を得た QA/RPA 環境だけで使用してください。対象、回数、保存範囲を限定し、不明な入力や応答では人による確認に切り替えます。非公開データへのアクセス、プラットフォーム措置の回避、大量アカウント作成には使用できません。

## Conclusion

Agent フレームワーク、ローカルポリシー、同期画像認識を分離することで、各境界を独立して検証し、[CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=typed-captcha-solver-agent-tool&utm_content=repository-readme) の公式契約に合わせられます。

## Maintainer Note

Developer sharing CapSolver integration examples.

## License

[MIT](../../LICENSE)
