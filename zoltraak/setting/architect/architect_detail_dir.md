
# モジュール
- `要件定義書` =
```md

zoltraak/
├── README.md
├── docs/
│   ├── getting_started.md
│   ├── usage.md
│   ├── examples.md
│   ├── architecture.md
│   ├── contributing.md
│   └── faq.md
├── src/
│   ├── __init__.py
│   ├── compiler.py
│   ├── executor.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_compiler.py
│   └── test_executor.py
├── examples/
│   ├── example1.md
│   └── example2.md
├── requirements.txt
├── setup.py
└── LICENSE
```

- README.md: プロジェクトの概要、インストール方法、クイックスタート、ライセンス情報などを簡潔に記載。
- docs/: 詳細なドキュメントを格納。
  - getting_started.md: インストールと初期設定の方法。
  - usage.md: 使用方法の詳細。
  - examples.md: 具体的な使用例。
  - architecture.md: システムアーキテクチャの説明。
  - contributing.md: プロジェクトへの貢献方法。
  - faq.md: よくある質問と回答。
- src/: ソースコードを格納。
  - `__init__.py`: パッケージの初期化ファイル。
  - compiler.py: コンパイラの実装。
  - executor.py: 実行器の実装。
  - utils.py: ユーティリティ関数の実装。
- tests/: テストコードを格納。
  - `__init__.py`: テストパッケージの初期化ファイル。
  - test_compiler.py: コンパイラのテスト。
  - test_executor.py: 実行器のテスト。
- examples/: 使用例となるMarkdownファイルを格納。
- requirements.txt: 依存ライブラリのリスト。
- setup.py: パッケージのセットアップ情報。
- LICENSE: ライセンス情報。

- `要件定義書ファイルパス` = [source_file_path]
- `ルートディレクトリ` = generated/[source_file_name]/

# 作業内容
**上記の要件定義を元に、以下の指示に従ってPythonでディレクトリ構成を構築するコードを記述してください。コードのみ**

## 指示
1. コードブロックは使用せず、Pythonコードでディレクトリとファイルの構成を作成する
3. ディレクトリ構成は `ルートディレクトリ` の配下にすべて作成すること、README.md を除いて、それ以外のファイルは記述

4. os.mkdirsで`ルートディレクトリ`の作成
5. os.path.joinと os.mkdirsで 詳細なディレクトリを作成
6. os機能を使ってファイルを作成
7. README.mdを作成
`要件定義ファイルパス`をpythonのsubprocessを使って、システム的にコピー&ペーストして
8. 以下をpythonプログラムで実行
pythonのsubprocessを使って code `ルートディレクトリ`
pythonのsubprocessを使って code `ルートディレクトリ`/README.md
9. 生成したコードは即座に実行可能な状態にすること
10. 出力先ファイルはpythonであり、プログラムコードのみを記載し文言はコメントアウトで記載すること

