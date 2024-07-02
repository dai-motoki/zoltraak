# niwatokoプログラミング言語のPythonパッケージ開発要件定義書

## 1. 目的
niwatokoという自然言語でプログラムを行うことのできるプログラミング言語のPythonパッケージを開発する。このパッケージでは、裏でLLM（Large Language Model）を使用して自然言語処理を行い、ユーザーがniwatokoという言語でプログラムを記述することを可能にする。また、LLMの管理と実験も行える機能を提供する。

## 2. パッケージの基本構造
以下のようなディレクトリ構成でPythonパッケージを開発する。

```
niwatoko/
├── app/
│   ├── __init__.py   # パッケージの初期化と公開APIのimport
│   ├── core.py       # appの中核となる機能を実装するモジュール
│   ├── llm.py        # LLMの管理と実行を行うモジュール
│   └── utils.py      # ユーティリティ関数を定義するモジュール
├── tests/
│   ├── __init__.py   # テストパッケージの初期化
│   ├── test_core.py  # core.pyのテストを定義するモジュール
│   ├── test_llm.py   # llm.pyのテストを定義するモジュール
│   └── test_utils.py # utils.pyのテストを定義するモジュール
├── docs/
│   ├── conf.py       # Sphinxドキュメントの設定ファイル
│   ├── index.rst     # Sphinxドキュメントのルートファイル
│   └── ...           # その他のドキュメントファイル
├── README.md         # パッケージの概要、インストール方法、使用方法などを記載
├── LICENSE           # パッケージのライセンスを記載
├── setup.py          # パッケージのメタデータやインストール方法を定義
├── requirements.txt  # パッケージが依存する外部ライブラリを記載
├── Dockerfile        # Dockerイメージのビルド手順を記述
├── docker-compose.yml # 複数のDockerコンテナを定義・実行するための設定
├── .github/workflows/
│   ├── ci.yml        # GitHub ActionsによるCIワークフローの設定
│   └── cd.yml        # GitHub ActionsによるCDワークフローの設定
└── app.py            # Streamlit/Gradioを使用したWebアプリケーションのエントリーポイント
```

## 3. setup.pyの書き方
setup.pyファイルでは、以下の項目を記述する。

```python
from setuptools import setup, find_packages

setup(
    name="niwatoko",
    version="0.1.0",
    description="A programming language that allows users to write programs in natural language.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/niwatoko",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "tensorflow",
        "transformers",
        "streamlit",
        "gradio",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
```

## 4. __init__.pyの役割
niwatoko/__init__.pyファイルでは、以下の処理を行う。

```python
__version__ = "0.1.0"

from .core import NiwatokoProgrammingLanguage
from .llm import LLMManager

__all__ = ["NiwatokoProgrammingLanguage", "LLMManager"]
```

- `__version__`変数でパッケージのバージョンを定義する。
- パッケージの公開APIである`NiwatokoProgrammingLanguage`と`LLMManager`をimportする。

## 5. README.mdの書き方
README.mdファイルでは、以下の項目を記述する。

```markdown
# Niwatoko Programming Language

Niwatoko is a programming language that allows users to write programs in natural language. It uses a large language model (LLM) under the hood to process the natural language and execute the corresponding code.

## Installation

To install Niwatoko, run the following command:

```
pip install niwatoko
```

## Usage

Here's a simple example of how to use Niwatoko:

```python
from niwatoko import NiwatokoProgrammingLanguage

npl = NiwatokoProgrammingLanguage()

code = """
自然数のリストを受け取り、その中の偶数のみを返す関数を作成してください。
"""

result = npl.execute(code)
print(result)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions to Niwatoko! Please see our [contributing guidelines](CONTRIBUTING.md) for more information.

## Support

If you have any questions or need assistance, please [open an issue](https://github.com/yourusername/niwatoko/issues) on our GitHub repository.
```

## 6. LICENSEファイル
このパッケージではMITライセンスを採用する。以下の内容をLICENSEファイルに記述する。

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

## 7. パッケージのバージョン管理
セマンティックバージョニングに基づき、MAJOR.MINOR.PATCH形式でバージョンを管理する。

- APIの互換性が損なわれる変更を行った場合はMAJORバージョンを上げる。
- 後方互換性を保ちつつ機能を追加した場合はMINORバージョンを上げる。
- バグ修正などの小さな変更はPATCHバージョンを上げる。

バージョンは`niwatoko/__init__.py`の`__version__`変数で管理する。

## 8. テストの書き方
tests/ディレクトリ内にテストファイルを作成し、unittest.TestCaseを継承したテストクラスを定義する。テストメソッド名はtest_で始める。

```python
import unittest
from niwatoko.core import NiwatokoProgrammingLanguage

class TestNiwatokoProgrammingLanguage(unittest.TestCase):
    def setUp(self):
        self.npl = NiwatokoProgrammingLanguage()

    def test_execute_even_numbers(self):
        code = """
        自然数のリストを受け取り、その中の偶数のみを返す関数を作成してください。
        """
        expected_output = "def even_numbers(numbers):\n    return [n for n in numbers if n % 2 == 0]"
        self.assertEqual(self.npl.execute(code), expected_output)

if __name__ == "__main__":
    unittest.main()
```

coverage.pyを使用してテストのカバレッジを測定する。

## 9. ドキュメントの作成方法
Sphinxを使用してドキュメントを作成する。

1. docs/ディレクトリ内でsphinx-quickstartコマンドを実行し、Sphinxプロジェクトを作成する。
2. docs/conf.pyファイルでプロジェクトの設定を行う。
3. docs/index.rstファイルにドキュメントのルートページを記述する。
4. niwatoko/ディレクトリ内のモジュールやクラス、関数のdocstringを記述する。
5. docs/ディレクトリ内でmake htmlコマンドを実行し、HTMLドキュメントを生成する。

## 10. Docker化とCI/CDの設定
Dockerfileを作成し、Pythonパッケージとその依存関係をインストールする。docker-compose.ymlファイルを使用して、複数のサービス（Webアプリケーション、LLMサーバーなど）を定義・実行する。

GitHub Actionsを使用してCI/CDパイプラインを設定する。.github/workflows/ディレクトリ内にci.ymlとcd.ymlファイルを作成し、それぞれ以下の処理を行う。

- ci.yml: コードのリント、ユニットテスト、カバレッジ測定を行う。
- cd.yml: Dockerイメージのビルドとコンテナレジストリへのプッシュ、本番環境へのデプロイを行う。

## 11. WebアプリケーションのUI設定
Streamlitまたは Gradioを使用してWebアプリケーションのUIを設定する。app.pyファイルにWebアプリケーションのエントリーポイントを記述する。

```python
import streamlit as st
from niwatoko import NiwatokoProgrammingLanguage

st.title("Niwatoko Programming Language")

code = st.text_area("Enter your Niwatoko code:", height=200)

if st.button("Execute"):
    npl = NiwatokoProgrammingLanguage()
    result = npl.execute(code)
    st.code(result, language="python")
```

以上の要件定義書に基づいて、メンテナンス性、拡張性、再利用性を考慮したPythonパッケージを開発する。パッケージ開発が完了したら、以下の手順でPyPIに公開する。

1. setup.pyファイルにパッケージのメタデータを記述する。
2. パッケージをビルドする（python setup.py sdist bdist_wheel）。
3. TestPyPIにパッケージをアップロードしてテストする（twine upload --repository-url https://test.pypi.org/legacy/ dist/*）。
4. 問題がなければ、本番のPyPIにパッケージをアップロードする（twine upload dist/*）。

また、GitHub Actionsを使用してCI/CDパイプラインを設定し、コードの品質を維持しつつ、継続的にパッケージを改善・更新していく。