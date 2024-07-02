# 要件定義
## 目標: 自然言語でプログラミングができる「niwatoko」というPythonパッケージを作成する

このプロジェクトの要件は以下の通りです:

## 1. 目的
このプロジェクトの目的は、「niwatoko」と呼ばれる自然言語でプログラミングができるPythonパッケージを開発することです。このパッケージは、niwatoko言語でプログラムを書いて実行するためのユーザーフレンドリーなインターフェイスを提供し、プログラミング経験の少ない人々にも利用しやすくします。

## 2. パッケージ構造
Pythonパッケージの標準的なディレクトリ構造を使用します:

- `niwatoko/`
  - `__init__.py`
  - `core.py`
  - `utils.py`
  - `exceptions.py`
  - `tests/`
    - `__init__.py`
    - `test_core.py`
    - `test_utils.py`
  - `docs/`
    - `conf.py`
    - `index.rst`
    - `api.rst`
    - `user_guide.rst`
  - LICENSE
  - README.md
  - setup.py

各ディレクトリとファイルの役割は以下の通りです:

- `niwatoko/`: パッケージのソースコードを含むメインディレクトリ
- `__init__.py`: パッケージを初期化し、公開APIを定義する
- `core.py`: niwatoko言語の中核的な機能(パーサー、インタプリター、実行エンジンなど)を実装する
- `utils.py`: パッケージ全体で使用されるユーティリティ関数やヘルパークラスを提供する
- `exceptions.py`: パッケージで使用されるカスタム例外を定義する
- `tests/`: パッケージのユニットテストを含む
- `docs/`: Sphinxを使用して生成されたパッケージのドキュメンテーションを保持する
- LICENSE: パッケージのライセンスファイル
- README.md: パッケージの概要、インストール手順、使用例などを提供する
- setup.py: パッケージのメタデータと依存関係を定義し、配布用にパッケージ化する

## 3. setup.py
setup.pyファイルは、niwatoko Pythonパッケージのパッケージ化と配布を担当します。以下の主要な要素を含む必要があります:

```python
from setuptools import setup, find_packages

setup(
    name='niwatoko',
    version='1.0.0',
    description='niwatoko自然言語でプログラミングできるPythonパッケージ',
    long_description=open('README.md').read(),
    author='Your Name',
    author_email='dai.motoki1123@gmail.com',
    url='https://github.com/dai-motoki/niwatoko',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.19.0',
        'scipy>=1.5.0',
    ],
)
```

## 4. __init__.py
`__init__.py`ファイルは以下の目的を果たします:

1. niwatokonパッケージを初期化し、必要な設定を行う
2. `__version__`変数を定義し、パッケージの現在のバージョ`__version__`変数を定義し、パッケージの現在のバージョンを指定する。
3. パッケージの公開APIをインポートし、ユーザーが利用できるようにする。

## 5. README.md

- **概要**: niwatokonパッケージの概要と目的を簡潔に説明する
- **インストール**: パッケージのインストール手順と依存関係について説明する
- **使用方法**: パッケージの使用例とサンプルコードを示し、説明する
- **ライセンス**: パッケージが配布されるライセンス(Apache 2.0)を明記する
- **貢献**: プロジェクトへの貢献方法(問題の報告、プルリクエストの提出など)のガイドラインを示す
- **サポート**: ユーザーがサポートを受ける方法(メンテナーへの連絡、ドキュメントへのアクセスなど)を説明する

## 6. LICENSE
ライセンスファイルでは、niwatokonパッケージの配布条件を明記する必要があります。一般的な