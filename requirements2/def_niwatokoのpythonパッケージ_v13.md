# 要件定義書: niwatoko プログラミング言語 Pythonパッケージ

## 1. 目的
niwatokoを利用することで、自然言語を用いてプログラミングができるPythonパッケージを開発する。このパッケージにより、プログラミング初心者でも簡単にniwatokoを使ってプログラムを記述できるようになる。

## 2. パッケージの基本構造

```
niwatoko/
├── niwatoko/
│   ├── __init__.py
│   ├── lexer.py
│   ├── parser.py
│   ├── interpreter.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_lexer.py
│   ├── test_parser.py
│   └── test_interpreter.py
├── docs/
│   ├── conf.py
│   ├── index.rst
│   └── ...
├── README.md
├── LICENSE
├── setup.py
└── requirements.txt
```

- `niwatoko/`: パッケージの本体となるディレクトリ。言語の構文解析や実行に関するモジュールを含む。
- `tests/`: ユニットテストを含むディレクトリ。各モジュールに対応するテストファイルを配置する。
- `docs/`: Sphinxを使用して生成するドキュメントのソースファイルを含むディレクトリ。
- `README.md`: パッケージの概要、インストール方法、使用方法などを記載するファイル。
- `LICENSE`: パッケージのライセンスを記載するファイル。
- `setup.py`: パッケージのメタデータやインストール方法を定義するファイル。
- `requirements.txt`: パッケージが依存する外部ライブラリを記載するファイル。

## 3. setup.pyの書き方
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="niwatoko",
    version="0.1.0", 
    description="自然言語 'niwatoko' を使用したプログラミング言語",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="dai-motoki",
    author_email="dai.motoki1123@gmail.com",
    url="https://github.com/dai-motoki/niwatoko",
    packages=find_packages(),
    install_requires=[
        "dependency1",
        "dependency2",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
```

- `name`: パッケージ名を指定する。
- `version`: パッケージのバージョンを指定する。
- `description`: パッケージの短い説明を記載する。
- `long_description`: パッケージの詳細な説明を記載する。通常はREADME.mdの内容を指定する。
- `author`: 作者名を指定する。
- `author_email`: 作者のメールアドレスを指定する。
- `url`: パッケージのWebサイトやリポジトリのURLを指定する。
- `packages`: パッケージに含めるPythonモジュールを指定する。`find_packages()`を使用すると自動的に検出される。
- `install_requires`: パッケージが依存する外部ライブラリを指定する。

## 4. __init__.pyの役割
```python
__version__ = "0.1.0"

from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter
```

- パッケージの初期化処理を行う。
- `__version__`変数でパッケージのバージョンを定義する。
- パッケージの公開APIをimportする。これにより、ユーザーはパッケージ名を指定するだけで主要なクラスにアクセスできる。

## 5. README.mdの書き方
```markdown
# niwatoko プログラミング言語

niwatokoは、自然言語を使用してプログラミングができるPythonパッケージです。

## インストール方法
```
pip install niwatoko
```

## 使用方法
```python
from niwatoko import Lexer, Parser, Interpreter

code = """
にわとこを 初期化する
「こんにちは、世界！」を 表示する
"""

lexer = Lexer(code)
tokens = lexer.tokenize()

parser = Parser(tokens)
ast = parser.parse()

interpreter = Interpreter(ast)
interpreter.interpret()
```

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。詳細については、LICENSEファイルを参照してください。

## 貢献方法
1. このリポジトリをフォークしてください。
2. 新しいブランチを作成してください: `git checkout -b my-new-feature`
3. 変更をコミットしてください: `git commit -am 'Add some feature'`
4. ブランチにプッシュしてください: `git push origin my-new-feature`
5. プルリクエストを作成してください。

## サポート
問題や機能リクエストがある場合は、Githubのイシューを使用してください。
- パッケージの概要、インストール方法、使用方法、ライセンス、貢献方法、サポート方法を記載する。
- コードブロックを使用して、インストール方法や使用方法を具体的に示す。

## 6. LICENSEファイル
```
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

- MITライセンスの例を示した。他のライセンスとしては、Apache License 2.0、GNU General Public License (GPL)、BSD Licenseなどがある。
- ライセンスファイルには、著作権表示とライセンスの条件を記載する。

## 7. パッケージのバージョン管理
- MAJOR.MINOR.PATCH形式でバージョンを表現する。
  - MAJOR: APIの互換性が損なわれる変更を行った場合に上げる。
  - MINOR: 後方互換性を保ちつつ機能を追加した場合に上げる。
  - PATCH: バグ修正などの小さな変更を行った場合に上げる。
- バージョンは`setup.py`と`__init__.py`の両方で管理する。
- リリース時には、適切なバージョンタグをGitリポジトリに付ける。

## 8. テストの書き方
```python
import unittest
from niwatoko.lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_tokenize(self):
        code = "「こんにちは」を 表示する"
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        self.assertEqual(len(tokens), 4)
        self.assertEqual(tokens[0].type, "STRING")
        self.assertEqual(tokens[0].value, "こんにちは")
        self.assertEqual(tokens[1].type, "PARTICLE")
        self.assertEqual(tokens[1].value, "を")
        self.assertEqual(tokens[2].type, "IDENTIFIER")
        self.assertEqual(tokens[2].value, "表示")
        self.assertEqual(tokens[3].type, "KEYWORD")
        self.assertEqual(tokens[3].value, "する")

if __name__ == "__main__":
    unittest.main()
```

- テストファイルは`test_*.py`または`*_test.py`の命名規則に従う。
- `unittest.TestCase`を継承してテストクラスを定義する。
- テストメソッドは`test_`で始める。
- `assertEqual`などのassertメソッドを使用して、期待される結果と実際の結果を比較する。
- テストのカバレッジを測定するには、`coverage`パッケージを使用する。

## 9. ドキュメントの作成方法
- Sphinxを使用してドキュメントを作成する。
- プロジェクトのルートディレクトリで`sphinx-quickstart`コマンドを実行し、Sphinxプロジェクトを作成する。
- `docs`ディレクトリ内の`index.rst`ファイルにドキュメントの目次を記述する。
- reStructuredText記法を使用して、各モジュールやクラス、関数のドキュメントを記述する。
- モジュール、クラス、関数のdocstringを記述し、`autodoc`拡張を使用して自動的にドキュメントに取り込む。
- `conf.py`ファイルでプロジェクトの設定を行う（プロジェクト名、バージョン、著者など）。
- `make html`コマンドを実行して、HTMLドキュメントを生成する。

## その他の考慮事項
- PEP 8に準拠したコーディングスタイルを採用する。
- 適切なエラーハンドリングとログ出力を行う。
- パッケージをPyPIに公開する。
- GitHub ActionsなどのCI/CDツールを使用して、自動テストとデプロイを設定する。

以上が、niwatokoプログラミング言語のPythonパッケージ開発における要件定義書です。オブジェクト指向の原則に従い、メンテナンス性、拡張性、再利用性を考慮したパッケージ構造とコーディングスタイルを心がけてください。