# 作業内容
**`要件定義書`を元に、以下の指示に従ってPythonでディレクトリ構成を構築するコードを記述してください。コードのみ**

## 指示
1. コードブロックは使用せず、Pythonコードでディレクトリとファイルの構成を作成する
2. ディレクトリ構成は `ルートディレクトリ` の配下にすべて作成すること、README.md を除いて、それ以外のファイルは記述
    2.1 os.mkdirsを使用して`ルートディレクトリ`を作成する
    2.2 os.path.joinとos.mkdirsを使用して、詳細なディレクトリ構成を作成する  
    ディレクトリ名をリストに記述し実行
    2.3 osモジュールの機能を使用して、必要なファイル群を作成する（ディレクトリの中に何もない場合は新しく作る）
    ファイル名をリストに記述し実行
    2.4 `react&fastapi`を参考にdaiagramsモジュール を利用して然るべきディレクトリにpngファイルを作成するコードを記載
    アーキテクチャの全体像を図示してください。主要なサービスとそれらの関係性を含めてください。
    以下参考、diagramsのsaveやrenderは利用しないこと
    2.5 ルートディレクトリにREADME.mdファイルを書き込みモードで開く
        - `要件定義ファイル`の内容を読み込みモードで開く
        -- `要件定義ファイル`の内容をREADME.mdに書き込む
3. ディレクトリを新しく開く
pythonのsubprocessを使って code `ルートディレクトリ`
pythonのsubprocessを使って code `ルートディレクトリ`/README.md
4. 生成したコードは即座に実行可能な状態にすること
5. 出力先ファイルはpythonであり、プログラムコードのみを記載し文言はコメントアウトで記載すること

# 引用
- `要件定義書` = [source_content]
- `要件定義書ファイル` = [source_file_path]
- `ルートディレクトリ` = generated/[source_file_name]/

- `react&fastapi` = 
```
from diagrams import Diagram, Cluster
from diagrams.programming.framework import FastAPI, React
from diagrams.onprem.database import PostgreSQL
from diagrams.programming.language import Python

graph_attr = {
    "fontsize": "45",
    "bgcolor": "transparent"
}

with Diagram("Application Architecture", show=False, direction="TB", filename=os.path.join(root_dir, 'diagrams', 'app_architecture'), outformat="png"):
    with Cluster("A"):
    with Cluster("B"):
```
