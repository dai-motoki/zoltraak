# Pythonパッケージ開発のための要件定義書
## ゴール: {prompt}
上記を満たす要件定義書を作成してください。
オブジェクト指向の原則に従って、以下の要件を含めて要件定義書を作成してください。

## 1. 目的
システムの全体的な目的を簡潔に説明してください。

## 2. パッケージの基本構造
Pythonパッケージの標準的なディレクトリ構成と、各ディレクトリ・ファイルの役割について説明してください。
マークダウン形式

多言語翻訳のi18nice[YAML]についてもディレクトリ構成に含めること
CICDはカスタマージャーニーを詳細に記載

```
project/
├── .github/workflows/
│   ├── ci.yml       # GitHub ActionsによるCIワークフローの設定ファイル
                        CICDはカスタマージャーニーを詳細に記載
│   └── cd.yml       # GitHub ActionsによるCDワークフローの設定ファイル
                        CICDはカスタマージャーニーを詳細に記載
├── package/
├── tests/
├── docs/
│   ├── conf.py      # Sphinxドキュメントの設定ファイル
│   ├── index.rst    # Sphinxドキュメントのルートファイル
│   └── ...          # その他のドキュメントファイル
├── README.md        # パッケージの概要、インストール方法、使用方法などを記載するファイル
├── LICENSE          # パッケージのライセンスを記載するファイル
├── setup.py         # パッケージのメタデータやインストール方法を定義するファイル
├── requirements.txt # パッケージが依存する外部ライブラリを記載するファイル
├── Dockerfile       # Dockerイメージのビルド手順を記述するファイル
├── docker-compose.yml # 複数のDockerコンテナを定義・実行するための設定ファイル
└── app.py           # Streamlit/Gradioを使用したWebアプリケーションのエントリーポイント
├── .gitignore       # Gitで追跡しないファイルやディレクトリを指定するファイル
└── app.py           # Streamlit/Gradioを使用したWebアプリケーションのエントリーポイント
└── pypi_update.sh  # PyPIへのパッケージアップロードを自動化するスクリプト
```

```pypi_update.sh  # PyPIへのパッケージアップロードを自動化するスクリプト
pip install wheel
python setup.py sdist bdist_wheel
twine upload dist/grimo-1.3.46*
git add . && git commit -m "Release v1.3.46" && git push && git tag v1.3.46 && git push --tags

```

## 3. setup.pyの書き方
pypiにおけるsetup.pyファイルの役割と、記述すべき主要な項目について以下を参考に具体的に説明してください。
以下はあくまで一般的な例です。
- `name`: パッケージ名
- `version`: パッケージのバージョン
- `description`: パッケージの短い説明
- `long_description`: パッケージの詳細な説明（README.mdの内容を指定することが多い）
- `author`: 作者名
- `author_email`: 作者のメールアドレス
- `url`: パッケージのWebサイトやリポジトリのURL
- `packages`: パッケージに含めるPythonモジュールを指定
- `install_requires`: パッケージが依存する外部ライブラリを指定

また、pypiへのアップロード方法も記載
pip install wheel
pip install --upgrade setuptools wheel


python setup.py sdist bdist_wheel
twine upload dist/package_name



## 4. __init__.pyの役割
記述すべき主要な項目について以下を参考に具体的に説明してください。
- パッケージの初期化処理を行う
- `__version__`変数でパッケージのバージョンを定義する
- パッケージの公開APIをimportする

## 5. README.mdの書き方
記述すべき主要な項目について以下を参考に具体的に説明してください。
- パッケージの概要
- インストール方法
- 使用方法
- ライセンス
- 貢献方法
- サポート方法

## 6. LICENSEファイル
LICENSEファイルの役割と、主要なオープンソースライセンスについて説明してください。
- MIT License
- Apache License 2.0
- GNU General Public License (GPL)
- BSD License

## 7. パッケージのバージョン管理
セマンティックバージョニングに基づくバージョン管理の方法について説明してください。
- MAJOR.MINOR.PATCH形式でバージョンを表現
- APIの互換性が損なわれる変更を行った場合はMAJORバージョンを上げる
- 後方互換性を保ちつつ機能を追加した場合はMINORバージョンを上げる
- バグ修正などの小さな変更はPATCHバージョンを上げる

## 8. テストの書き方
- テストファイルの命名規則は、test_*.pyまたは*_test.pyとします。
- テストクラスは、unittest.TestCaseを継承して定義します。
- テストメソッドの命名規則は、test_で始めます。
- assertメソッドを使用して、期待する結果と実際の結果を比較します。
- coverage.pyなどのツールを使用して、テストのカバレッジを測定します。
- CLIコマンドの実行結果をキャプチャして、期待する出力と比較するテスト
- 異なるコマンドラインオプションを指定した場合のテスト
- エラー処理のテスト（不正な引数を渡した場合など）

## 9. ドキュメントの作成方法
Sphinxを使用したドキュメントの作成方法について説明してください。
- Sphinxプロジェクトの作成方法
- reStructuredText記法の基本
- docstringを使用したモジュールやクラス、関数のドキュメント化
- conf.pyの設定方法
- HTMLドキュメントの生成方法

## 10. Docker化とCI/CDの設定
- Dockerfileの作成方法
- docker-composeの設定方法
- DockerイメージのビルドとPushの方法
- GitHub ActionsによるCI/CDパイプラインの設定方法

## 11. WebアプリケーションのUI設定
- Streamlitを使用したWebアプリケーションのUI設定方法
- Gradioを使用したWebアプリケーションのUI設定方法

Pythonパッケージ開発のベストプラクティスに基づき、メンテナンス性、拡張性、再利用性を考慮したパッケージ構造とコーディングスタイルを推奨してください。
また、パッケージの公開方法（PyPIへのアップロード）や、継続的インテグレーション・継続的デリバリー（CI/CD）の設定方法についても言及してください。
