# 作業内容
**`要件定義書`を元に、以下の指示に従ってPythonでディレクトリ構成を構築するコードを記述してください。コードのみ**

# モジュール情報
以下出力pythonファイル冒頭に記載すること
from zoltraak.llms.claude import `generate_response`
from zoltraak.utils.process_text import `normal`

## 指示
1. コードブロックは使用せず、Pythonコードでディレクトリとファイルの構成を作成する
2. ディレクトリ構成は `ルートディレクトリ` の配下にすべて作成すること、README.md を除いて、それ以外のファイルは記述
    2.1 os.mkdirsを使用して`ルートディレクトリ`を作成する
    2.2 os.path.joinとos.mkdirsを使用して、詳細なディレクトリ構成を作成する  
    ディレクトリ名をリストに記述し実行
    2.3 osモジュールの機能を使用して、必要なファイルを作成する（ディレクトリの中に何もない場合は新しく作る）
    以下参考、ただしメインファイルはプログラムを詳細に記載する
    ```
    files = [
    ('dirname', 'filename', 'fileのの拡張子の形式で、〜〜のプログラムを記載して下さい。という末尾で終了すること'),
    ]
    ```
    全てのpromptに`要件定義ファイル`を読み込みモードで取得した内容を入れて、ファイル名と必要なプロンプトを記載
    要件定義ファイルの内容を変数 readme_content に格納
    2.5 ルートディレクトリにREADME.mdファイルを書き込みモードで開く
        - `要件定義ファイル`の内容を読み込みモードで開く
        -- `要件定義ファイル`の内容をREADME.mdに書き込む
    - tqdmのプログレスバーを利用
        プログレスバーを初期化。合計処理ファイル数: len(files)、単位: "files"
        filesリストの要素を順にループ。各要素は (ディレクトリ名, ファイル名, プロンプト) のタプル
            モジュール記載忘れないように
            全てのファイルは`generate_response(model, prompt, max_tokens, temperature)`をもちいてfor文で然るべき内容を記載
                <!-- - モデル名を指定: "claude-3-haiku-20240307" -->
                - モデル名を指定: "claude-3-5-sonnet-20240620"
                - プロンプト: readme_content + 改行 + "上記の内容をもとにして" + prompt
                - 最大トークン数を指定: 1000
                - 温度パラメータを指定: 0.7
            出力結果は normal(response, "python")   にて加工して
        フォーマットしたレスポンスをファイルに書き込む
3. ディレクトリを新しく開く
pythonのsubprocessを使って code `ルートディレクトリ`
pythonのsubprocessを使って code `ルートディレクトリ`/README.md
4. 生成したコードは即座に実行可能な状態にすること
5. 出力先ファイルはpythonであり、プログラムコードのみを記載し文言はコメントアウトで記載すること
    必ず冒頭に以下を入れること
    from zoltraak.llms.claude import `generate_response`
    from zoltraak.utils.process_text import `normal`

# 引用
- `要件定義書` = [source_content]
- `要件定義書ファイル` = [source_file_path]
- `ルートディレクトリ` = generated/[source_file_name]/


# README.mdファイルのパスを作成
# README.mdファイルを書き込みモードで開く
# 要件定義ファイルを読み込みモードで開く
# - 要件定義ファイルのパスを指定
# - 
# -- 要件定義ファイルの内容をREADME.mdに書き込む
# -- 要件定義ファイルの内容を変数 readme_content に格納

# プログレスバーを初期化
# filesリストの要素を順にループ
# - ファイルのパスを作成
# - ファイルを書き込みモードで開く
# -- LLMを使用してレスポンスを生成
# --- モデル名を指定
ロンプトを作成 readme_content + \n 上記の内容をもとにしてprompt
# --- 最大トークン数を指定
# --- 温度パラメータを指定
# --
# -- レスポンスをフォーマットして変数に格納
# -- フォーマットしたレスポンスをファイルに書き込む
# - プログレスバーを更新
