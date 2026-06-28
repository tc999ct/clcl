#!/usr/bin/env python3
"""シンプルな CLI Todo アプリ。

タスクは JSON ファイルに保存されます。
使い方:
    py todo.py add "買い物に行く"
    py todo.py list
    py todo.py done 1
    py todo.py delete 1
"""
import json
import os
import sys

# スクリプトと同じ場所に todos.json を作る
TODO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_todos(todos):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def cmd_add(title):
    todos = load_todos()
    todos.append({"title": title, "done": False})
    save_todos(todos)
    print(f"追加しました: {title}")

def cmd_list():
    todos = load_todos()
    if not todos:
        print("タスクはありません。")
        return
    print("=== Todo リスト ===")
    for i, t in enumerate(todos, start=1):
        mark = "[x]" if t["done"] else "[ ]"
        print(f"{i:>3}. {mark} {t['title']}")

def _valid(index, todos):
    if index < 1 or index > len(todos):
        print(f"エラー: 番号 {index} は存在しません(1〜{len(todos)} の範囲で指定してください)。")
        return False
    return True

def cmd_done(index):
    todos = load_todos()
    if not _valid(index, todos):
        return
    todos[index - 1]["done"] = True
    save_todos(todos)
    print(f"完了にしました: {todos[index - 1]['title']}")

def cmd_delete(index):
    todos = load_todos()
    if not _valid(index, todos):
        return
    removed = todos.pop(index - 1)
    save_todos(todos)
    print(f"削除しました: {removed['title']}")

USAGE = """使い方:
    py todo.py add <タスク>   タスクを追加
    py todo.py list           タスク一覧を表示
    py todo.py done <番号>    指定番号のタスクを完了にする
    py todo.py delete <番号>  指定番号のタスクを削除
"""

def main():
    if len(sys.argv) < 2:
        print(USAGE)
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "add":
        if not args:
            print("エラー: add のあとにタスクを指定してください。")
            return
        cmd_add(" ".join(args))
    elif command == "list":
        cmd_list()
    elif command == "done":
        if not args:
            print("エラー: done のあとに番号を指定してください。")
            return
        try:
            cmd_done(int(args[0]))
        except ValueError:
            print("エラー: 番号は整数で指定してください。")
    elif command == "delete":
        if not args:
            print("エラー: delete のあとに番号を指定してください。")
            return
        try:
            cmd_delete(int(args[0]))
        except ValueError:
            print("エラー: 番号は整数で指定してください。")
    else:
        print(f"エラー: 不明なコマンド '{command}'")
        print(USAGE)

if __name__ == "__main__":
    main()