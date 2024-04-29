![](assets/videos/zoltraak2_smooth_high_quality.gif)
<h1>創造魔法 Zoltraak</h1>
<p>
Zoltraakは本格的な魔法時代の始まりを象徴する強大な創造魔法の名です。

これまでの未体系であった呪文からの術の発動を、魔法の文法体系に昇華しより高速かつ広範囲な術式展開と強大な魔法の発動を可能とするシステムです。

</p>
<a href="https://twitter.com/ai_syacho" alt="Twitter Follow">
<img src="https://img.shields.io/twitter/follow/Xiaogang_He.svg?label=Follow&style=social" /></a>
<a href="https://twitter.com/ai_syacho" alt="License"></a>
</p>

<!-- <p align="center">
<a href="https://github.com/dai-motoki/zoltraak" alt="GitHub contributors">
<img src="https://img.shields.io/github/contributors/XiaogangHe/python-climate-visuals.svg" /></a>
<a href="https://github.com/dai-motoki/zoltraak" alt="GitHub issues by-label">
<img src="https://img.shields.io/github/issues/XiaogangHe/InVEST-Cities-in-Nature" /></a> -->

# 貢献者

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dai-motoki"><img src="https://avatars.githubusercontent.com/u/58665894?v=4?s=100" width="100px;" alt="DAISUKE MOTOKI"/><br /><sub><b>DAISUKE MOTOKI</b></sub></a><br /><a href="#code-dai-motoki" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>


コントリビュータの追加方法はこちら
→ 
[クリック](#コントリビューターの追加方法)

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

Zoltraakは自然言語を実行言語に変換するプロンプトコンパイラシステムを採用し、数語の呪文から起動術式を用いて複雑な術式を展開しこれを即時実行可能な古代システム語へとコンパイルします。これにより術師の数語の呪文は強力な言霊の数々を織り込んだ魔法陣を通り魔法の範囲と威力を大幅に向上させることが可能となります。また詠唱、無詠唱での高速な創造魔法を実現可能とします。これにより相対する敵よりも圧倒的に高速かつ柔軟な術の発動を可能とします。

以下将来的にTODO: 
独自言語呪文や暗号呪文へのコンパイルも可能とするため周りから呪文を抜き取られリバースエンジニアリングされる心配もありません。 微調整の後それを古代語として圧縮し呪文を秘匿する事も可能です。 また、独自言語を用い数語微修正するのみで、実行言語が瞬時に変わり術が発動します。

## 他言語（Other languages）
他言語版readmeは以下からご覧になれます。現在サポートしているのは以下の言語です。

Readme files in other languages are available here. Currently we support:
- [English](README_EN.md)

# 目次


- [研究](docs/research.md)
- [設定](docs/configuration.md)
- [FAQ](docs/faq.md)
- [始め方](docs/getting-started.md)
- [インストール](docs/installation.md)
- [使用方法](docs/usage.md)
- [例](docs/examples)
- [トラブルシューティング](docs/troubleshooting.md)
- [ビデオ](docs/video.md)
- [貢献](docs/contributing.md)




# Zoltraakの動作イメージ
![Last frame of video](assets/images/last_frame.png)


## 利用方法

1. Zoltraakをインストール
   ```sh
   pip install --upgrade zoltraak
   ```

## 利用方法


1. 使い方
   1. `.env` ファイルに以下の環境変数を設定します。
      ```
      ANTHROPIC_API_KEY={Anthropicのキー}
      ```
   2. 以下のコマンドでZoltraakをインストールします。
      ```
      pip install zoltraak
      ```
   3. 以下のコマンドを実行し、プロンプトを入力します。
      ```
      zoltraak "最新の大規模言語モデルが学べるポケモンゲームの様なシステムを作りたい" -c dev_obj
      ```

   これにより、入力したプロンプトに基づいた要件定義書が生成されます。生成された要件定義書は叩き台となるため、必要に応じて内容を修正・拡充してください。

2. プロンプトコンパイラ（起動式）の指定
   `-c` オプション以降は用途に応じて変更できるプロンプトコンパイラ（起動式）を指定します。指定なしの場合は、最も適切と思われるプロンプトコンパイラを5つ自動でピックアップするコンパイラが実行されます。

   | コンパイラ名 | 説明 |
   | --- | --- |
   | dev_func | 関数型プログラミングを用いた開発タスクに関する要件定義書を生成するコンパイラ |
   | dev_obj | オブジェクト指向設計を用いた開発タスクに関する要件定義書を生成するコンパイラ |
   | biz_consult | ビジネスコンサルティングに関するドキュメントを生成するコンパイラ |
   | general_def | 一般的な開発タスクに関する要件定義書を生成するコンパイラ |
   | general_reqdef | 一般的な要求事項に関する要件定義書を生成するコンパイラ |
   | dev_react_fastapi | React + FastAPIを用いた開発タスクに関する要件定義書を生成するコンパイラ |

3. 具体例
   ```sh
   zoltraak "Manimを用いて、MoE（専門家の混合）モデルを視覚化するプログラムを開発する" -c dev_func
   zoltraak "今月中にオブジェクト指向設計を用いて、多機能在庫管理システムを開発する" -c dev_obj 
   zoltraak "今月中に中小企業向けのビジネスコンサルティングドキュメントを作成する。具体的には、マーケティング戦略、財務管理、人材育成に関するアドバイスを含む" -c biz_consult
   zoltraak "今月中に教育用の拡張現実（AR）アプリケーションを開発する" -c general_def
   zoltraak "今月中に政府向けの少子化対策として、具体的な施策と予算案を含む提言書を執筆する" -c general_reqdef
   ```


4. `test_dev_obj.md`というファイルを作成し、後続スレッドの内容をコピーして貼り付けてください。このファイルをzoltraakを実行するディレクトリと同じ階層に配置します。

5. `test_dev_obj.md`を以下のルールに従って自分の定義書生成プログラムに書き換えましょう:
   - `{prompt}`は zoltraakの後のプロンプト（呪文）が入るので消さないでください。
   - `## 2. ファイル・フォルダ構成`も消さないでください。
   - それ以外は自由に変更可能です。

6. 以下のコマンドを実行して、自作コンパイラを使用します:
   ```sh
   zoltraak プロンプト -cc 自作コンパイラ
   zoltraak "コーヒーショップ顧客管理システムを作りたい" -cc test_dev_obj.md
   ```

7. `zoltraak requirements/~~~.md`が貼り付けできるようになっているはずなので実行してください。

8. ディレクトリが構築されます。Cursor、VSCodeにてopenコマンドが起動しない方は以下を参照してください:
   https://note.com/88gram/n/n4ead3a677b83

注意: 全てClaude3 Haikuにより実行されています（一回あたり約1円の料金がかかります。ご自身で確認ください）。


```
zoltraak book.md -p "本を書きたい"
```

ファイル作成後は以下のように何度でも書き換えることができる。
```
zoltraak book.md -p "もっと分量増やしたい"
```

```sh
# RAGに突っ込むファイル群を指定
zoltraak aaaa.md -f ./input.md （作成予定）
# 一括修正
zoltraak dir/*.md （作成予定）
```


![llmcomment.png](assets/images/llmcomment.png)

### オプショナル引数
- ``-f`` : フォーマット指定。grimoiresフォルダ
- ``-l`` : 汎用言語指定。言語名は、"Español"などの現地名でも、"Spanish"のような英語でも、「スペイン語」のような日本語でもOKです。
  - 指定フォーマットについて、汎用言語フォーマッター（"``_lang.md``"で終わるファイル）が存在する場合は、そのファイルに基づき処理されます。
  - 存在しない場合は、デフォルトの言語セットコンパイラが起動します。ただ、相対的に効果がやや不安定なので、汎用言語フォーマッターを作成しておくことが強く推奨されます。

```
zoltraak "今月中にオブジェクト指向設計を用いて、多機能在庫管理システムを開発する" -c dev_obj -l English
zoltraak "今月中にオブジェクト指向設計を用いて、多機能在庫管理システムを開発する" -c dev_obj -f md_comment -l CSharp
zoltraak "今月中にオブジェクト指向設計を用いて、多機能在庫管理システムを開発する" -c dev_obj -l グルジア語
```


## プロジェクトへの参加

1. リポジトリをクローンします:
   ```
   git clone https://github.com/yourusername/Zoltraak.git
   ```

2. プロジェクトディレクトリに移動します:
   ```
   cd Zoltraak
   ```

3. 必要な依存関係をインストールします:
   ```
   pip install -r requirements.txt
   ```

4. Anthropic APIキーを設定します:
   - プロジェクトのルートディレクトリに`.env`ファイルを作成します。
   - 以下の行を`.env`ファイルに追加し、`YOUR_API_KEY`を実際のAnthropicのAPIキーに置き換えます:
     ```
     ANTHROPIC_API_KEY=YOUR_API_KEY
     ```








# pypiパッケージをローカル環境で開発するには以下の手順を踏むのが一般的です。

1. 仮想環境の作成
まず、パッケージ開発用の独立した仮想環境を作成します。これにより、システム全体のPythonとは分離された環境で開発できます。

```bash
python -m venv zoltraak-dev
source zoltraak-dev/bin/activate  # Linuxの場合
mypackage-env\Scripts\activate.bat  # Windowsの場合 
```

2. 必要なパッケージのインストール
開発に必要な依存パッケージをインストールします。例えば、`setuptools`と`wheel`は最低限必要です。

```bash
pip install setuptools wheel
```

3. パッケージのディレクトリ構成
以下のような基本的なディレクトリ構成でパッケージを作成します。

```
mypackage/
    mypackage/
        __init__.py
        module1.py
        module2.py
    tests/
        test_module1.py
        test_module2.py
    setup.py
    README.md
```

4. `setup.py`の作成
パッケージのメタデータや依存関係を記述した`setup.py`ファイルを作成します。例えば以下のようになります。

```python
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # 依存パッケージ
    ],
)
```

5. パッケージのインストール
開発中のパッケージを仮想環境にインストールします。

```bash
pip install -e .
```

これで、仮想環境内でパッケージを使用したり、変更を加えたりできるようになります。

6. パッケージの使用とテスト
パッケージの機能を使用したり、ユニットテストを実行したりして、開発を進めます。

7. ビルドと配布
完成したパッケージは以下のコマンドでビルドし、PyPIに公開できます。

```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

以上が、ローカル環境でのpypiパッケージ開発の基本的な流れです。仮想環境を使い、適切なディレクトリ構成と`setup.py`を用意することがポイントです。






### 追加コマンド


update_and_upload.sh
```sh

echo "バージョンをアップデート中..."
python update_version.py

echo "パッケージをビルド中..."
python setup.py sdist bdist_wheel

echo "ビルドしたパッケージをPyPIにアップロード中..."
twine upload dist/*
```

## 魔導書構成

```
zoltraak/grimoires/
├── compiler: 詠唱から自然言語への変換器
│   ├── akirapp.md
│   ├── func.md
│   ├── lisp.md
│   ├── obj.md
│   ├── obj_mermaid.md
│   ├── obj_lisp.md
│   ├── obj_lisp_g.md
│   ├── obj_lisp_g_base64.md
│   └── reqdef.md
├── encryption: 暗号化ツール
│   └── emoji.md
├── formatter: プロンプトフォーマッタ
│   ├── md_comment.md
│   ├── md_comment_xx.md (md_commentの言語指定：en, zhなどに対応。ご利用の言語の略称でまずは動くか確認して、動かない場合は追加対応をお待ちください)
│   └── py_comment.md
├── interpretspec: インタプリタ型LLM強化プロンプト
│   └── hirokichi.md
└── softdb: 柔らかいDB


memo: grimoires内の全てのベンチマークは各々やるような実験システムもいれたい

```


## 使用方法

MarkdownファイルをPythonコードに変換するには、以下のコマンドを使用します。


はい、以下に英語のREADMEを日本語に翻訳しました。

## キャッシング

Zoltraakは、変更されていないMarkdownファイルの不要な変換を避けるために、キャッシングメカニズムを実装しています。各Markdownファイルのハッシュ値を計算し、`hashes.txt`ファイルに保存します。変換コマンドを実行すると、Zoltraakは現在のハッシュ値を保存されているものと比較します。ハッシュ値が一致する場合、Markdownファイルが変更されていないことを示しているため、変換はスキップされ、以前に生成されたPythonコードが使用されます。

## CI/CDとの統合

ZoltraakはCI/CDワークフローに統合して、変換プロセスを自動化することができます。`run_tests.sh`スクリプトは、この統合を容易にするために提供されています。以下の手順を実行します。

1. 仮想環境を作成し、アクティベートします。

2. 必要な依存関係をインストールします。

3. MarkdownファイルをPythonコードに変換します。

4. 生成されたPythonコードを実行します。

5. 対応するユニットテストを実行します。

`run_tests.sh`スクリプトをCI/CDパイプラインで使用するには、CI/CDシステムがビルドプロセスの一部としてスクリプトを実行するように設定してください。

## 貢献

コントリビューションを歓迎します！問題を見つけた場合や改善の提案がある場合は、issueを開くかプルリクエストを送信してください。

## ライセンス



## TODO

### 急ぎ

- [ ] https://x.com/ai_syacho/status/1782956863912649114
- [ ] zoltraak "slkajfka" -c ファイルパス（これで自作もいける様にする）

```
ModuleNotFoundError系は
pip install ~~~~
で解決されます。

今回は
pip install anthropic
を行うことで解決されます。

↓
pip install zoltraak
一発で依存関係全て入る様に調整します。
```

### CLIコマンド関連
- [ ] zoltraak -p "manim動画を作りたい"  これで要件定義書とプログラムが生成

  - 

### ドキュメント生成
- [ ] 出力されたPythonファイルと詳細設計書のドキュメントを欲しい。
  - pythonファイルからドキュメントを生成したい
    - 例: `Zoltraakgenerated/calc.py` のようにpythonファイルを指定すると、そのファイルに対応するマークダウンドキュメントを生成、更新できるようにする 
    - pythonファイルのdocstringやコメントからドキュメントを自動生成する
    - 生成されたドキュメントはマークダウン形式で出力する

### テスト
- [ ] テストファイルは別途作成し、必要なタイミングでgit pushなどによりテストが実行されるようにしたい。

### Issue管理
- [ ] issueを記述したい。

### ファイル管理
- [x] 繰り返し利用する場合は、MarkdownファイルとPythonファイルを自動的に紐付けたい。（変更がある場合のみ再コンパイル）

### 要件定義関連
- [ ] 読み上げ文章から要件定義書を生成するプログラムをあきらさんのプロジェクトで実装する。
  - 宣言型と手続き型はごちゃっと入れた方が良さそう
- [ ] ZoltraakAAA.md 〜したい で定義書を修正
- [ ] あると嬉しいのは要件定義を決める際のプロンプトドキュメント 
  - コンパイラファイルは選択したい
- [ ] プログラムから要件定義に戻すフローが必要。

### その他
- [ ] 各種高級言語の変な癖を解消するための中間ファイルを事前に用意しておくのがよい。
- [ ] このファイルで、色合いに相当する部分のプロンプトの行数を教えて
- [ ] 差分をプロンプトとして伝達したい。
- [ ] 全て１から作り直す。mdファイルから
![image](assets/images//graph.png)








## 全体の流れ

- ①曖昧で抽象的：初期のプロンプトがこれに相当。「ほにゃらしたい」という曖昧な要求。

shell
```
zoltraak "本書きたい"
```
↓

mdファイル
gen_def_{goal}.md

```
# ゴール: 本を書きたい
要件定義書:
{def}
```
↓

- ②厳密で抽象的：要件定義書など。プロンプトから定義書を作成することで曖昧さが排除され、抽象的な状態になる。 
def_{goal}.md
```
書籍執筆要件定義書:
import {def}
import {def}
import {def}

~~~~~~~
~~~~~~~
~~~~~~~
~~~~~~~
~~~~~~~
```
↓

- ③曖昧で具体的：具体的な行動は伴っているが、まだ試行錯誤している段階。対話型（インタプリタ）とも言える。
exe_{goal}.py
```
プログラム # コメント
プログラム # コメント
プログラム # コメント
プログラム # コメント
```
- ④厳密で具体的：1本の具体的な行動に落とし込まれており、マニュアル化（ドキュメント型、コンパイル）された状態。

exe_{goal}.md
```
詳細手順書（暗号化、抽象化、使い手がわかりやすい状態にする。[]

```

zoltraak book.md













### 自然言語プログラミングの系譜


```
*ChatGPT登場
    |→ プロンプトエンジニアリング
        *プロンプトのシステム開発適用の必要性
            |→ プロンプトプログラミング
                * Claude3 Opusの出現
                |→ ドキュメントプログラミング
                    |→ 自然言語プログラミング
                            motoki → arbor → zoltraak
                                        * Groq x Llama3の対話不可能な高速テキスト出力制御
                                                |→ 自然言語フレームワーク zoltraak
                                                |→ プログラミング統一言語 babel
                                                                        ↑ イマココ
```



### アップロードの仕方


PyPIにパッケージをアップロードする手順は以下の通りです。

1. パッケージの準備:
   - プロジェクトのディレクトリ構成を適切に設定します。
   - [setup.py](file:///Users/motokidaisuke/motoki/setup.py#1%2C1-1%2C1)ファイルを作成し、パッケージの情報（名前、バージョン、依存関係など）を記述します。
   - [README.md](file:///Users/motokidaisuke/motoki/README.md#1%2C1-1%2C1)ファイルを作成し、パッケージの説明や使用方法を記載します。

2. アカウントの作成とAPIトークンの取得:
   - PyPIのWebサイト（https://pypi.org/）にアクセスします。
   - 新しいアカウントを作成するか、既存のアカウントにログインします。
   - アカウントの設定ページで、APIトークンを生成します。

3. ビルドとアップロード用ツールのインストール:
   - `twine`と`setuptools`をインストールします。
     ```
     pip install twine setuptools
     ```

4. パッケージのビルド:
   - プロジェクトのルートディレクトリで以下のコマンドを実行し、パッケージをビルドします。
     ```
     python setup.py sdist bdist_wheel
     ```
   - これにより、`dist`ディレクトリにパッケージの配布用ファイルが生成されます。

5. PyPIへのアップロード:
   - 以下のコマンドを実行し、パッケージをPyPIにアップロードします。
     ```
     twine upload dist/*
     ```
   - ユーザー名とパスワードの代わりに、取得したAPIトークンを使用します。

6. アップロードの確認:
   - PyPIのWebサイトにアクセスし、アップロードしたパッケージが正しく表示されていることを確認します。

これで、`zoltraak`パッケージがPyPIに公開されました。ユーザーは`pip install zoltraak`コマンドを使用してパッケージをインストールできます。

注意点:
- パッケージ名は一意である必要があります。既に存在する名前は使用できません。
- バージョン番号は、新しいバージョンをアップロードするたびに増やす必要があります。
- `setup.py`ファイルには、適切なメタデータと依存関係を記述してください。
- `README.md`ファイルには、パッケージの説明や使用方法を明確に記載してください。

以上が、PyPIへのパッケージのアップロード手順です。問題がある場合は、PyPIのドキュメンテーションを参照するか、コミュニティに質問してください。




## 仮想環境を用いて実行

`pyenv` はPythonのバージョン管理ツールですが、直接的に仮想環境を作成する機能は持っていません。仮想環境を作成するためには、`pyenv-virtualenv` というプラグインを使用する必要があります。

以下は `pyenv-virtualenv` を使用して仮想環境を作成する手順です。

1. **pyenv-virtualenv のインストール**

   まずは `pyenv-virtualenv` プラグインをインストールします。これは `pyenv` が既にインストールされていることを前提としています。

   ```bash
   git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
   ```

   インストール後、シェルの設定ファイル (例えば `.bashrc` や `.zshrc`) に以下を追加して、シェルを再起動します。

   ```bash
   eval "$(pyenv init --path)"
   eval "$(pyenv virtualenv-init -)"
   ```

2. **Python のインストール**

   `pyenv` を使用して、仮想環境用の Python バージョンをインストールします。

   ```bash
   pyenv install 3.8.5  # 例として Python 3.8.5 をインストール
   ```

3. **仮想環境の作成**

   次に、指定した Python バージョンで仮想環境を作成します。

   ```bash
   pyenv virtualenv 3.8.5 my-virtual-env-3.8.5
   ```

   ここで `my-virtual-env-3.8.5` は仮想環境の名前です。

4. **仮想環境のアクティベーション**

   作成した仮想環境をアクティブにします。

   ```bash
   pyenv activate my-virtual-env-3.8.5
   ```

   これで、指定した仮想環境がアクティブになります。

5. **仮想環境のデアクティベーション**

   仮想環境をデアクティブにするには、以下のコマンドを使用します。

   ```bash
   pyenv deactivate
   ```

これで `pyenv` と `pyenv-virtualenv` を使用して Python の仮想環境を作成し、管理する方法を説明しました。


ローカル環境

pip install -e .

を行うと
Users/motokidaisuke/.pyenv/versions/3.11.5 
に入ってしまうらしい

python setup.py sdist bdist_wheel
twine upload --verbose dist/*


仮想環境
deactivate
rm -rf /Users/motokidaisuke/aaaaa/zoltraak-env
python3 -m venv /Users/motokidaisuke/aaaaa/zoltraak-env
source /Users/motokidaisuke/aaaaa/zoltraak-env/bin/activate




# アイデア（重要）

呪文 → 文書 → 構造体 → 情報構造体 → 実行
       |→ 自然言語     |→ 自然言語
                           |→ プログラミング言語



# メモ

```

import compiler.dev.obj
import writer.book.lecture

```



# TODO


- [ ] ディレクトリ構築はペーストではなくシステムから構築するか聞かれるようにする
- [ ] Pythonのファイル取得部は関数化して外部ファイル化ける
- [ ] デザイナーと開発者を導入。


# 0.1.25 更新情報
2024_04_28 

- setting → grimoiresに変更
- react & fast APIの要件定義書を記載しディレクトリを構築するdev_react_fast_api を追加
- formatter 25パターンほど追加
- 実行フローを整理、アニメーション追加


# チップス

zoltraak "かぞく情報データ分析v4" -c dev_react_fastapi  

とやると要件定義書名にバージョンを記載してくれる。


## コントリビューターの追加方法

コントリビューターを追加するには、以下の手順を実行してください:

1. issueまたはプルリクエストに、以下の形式でコメントを残してください:  

```
@all-contributors please add @username for <contributions>
```
`@username`をコントリビューターのGitHubユーザー名に、`<contributions>`をコントリビュートのタイプに置き換えてください。コントリビュートのタイプは、[Emoji Key](https://allcontributors.org/docs/en/emoji-key)を参照してください。


2. ボットがコントリビューターをプロジェクトに追加するためのプルリクエストを作成します。

3. プルリクエストがマージされると、コントリビューターがREADMEに追加されます。

