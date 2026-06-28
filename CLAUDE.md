# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

シンプルな CLI Todo アプリケーション。Python で作成され、タスクを JSON ファイル (`todos.json`) に保存する。

## ファイル構成

- `todo.py` - メインスクリプト（単一ファイル構成）
- `todos.json` - タスクデータ（自動生成）
- `readme.txt` - 仕様書

## 開発コマンド

```bash
# タスクを追加
py todo.py add "タスク内容"

# タスク一覧を表示
py todo.py list

# タスクを完了にする
py todo.py done <番号>

# タスクを削除
py todo.py delete <番号>
```

## アーキテクチャ

- **データ永続化**: JSON ファイル (`todos.json`) に配列形式で保存
- **状態管理**: 各タスクは `{title, done}` の 2 フィールド
- **エンコーディング**: UTF-8 出力に固定（Windows コンソール対応）
- **依存関係**: 標準ライブラリのみ使用（`json`, `os`, `sys`）