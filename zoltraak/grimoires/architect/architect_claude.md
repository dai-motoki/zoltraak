# 作業内容
**`要件定義書`を元に、以下の指示に従ってPythonでディレクトリ構成を構築するコードを記述してください。コードのみ**

## 指示
1. コードブロックは使用せず、Pythonコードでディレクトリとファイルの構成を作成する
2. ディレクトリ構成は `ルートディレクトリ` の配下にすべて作成すること、README.md を除いて、それ以外のファイルは記述
    2.1 os.mkdirsを使用して`ルートディレクトリ`を作成する
    2.2 os.path.joinとos.mkdirsを使用して、詳細なディレクトリ構成を作成する  
    ディレクトリ名をリストに記述し実行
    2.3 osモジュールの機能を使用して、必要なファイルを作成する（ディレクトリの中に何もない場合は新しく作る）
        全てのファイルは`claude.generate_response(model, prompt, max_tokens, temperature)`をもちいてfor文で然るべき内容を記載
        全てのpromptに`要件定義ファイル`を読み込みモードで取得した内容を入れて、ファイル名と必要なプロンプトを記載
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
- `claude` = 
```
import os
import anthropic
from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む

def generate_response(model, prompt, max_tokens, temperature):
    """
    Anthropic APIを使用してプロンプトに対する応答を生成する関数。

    Args:
        prompt (str): 応答を生成するためのプロンプト。

    Returns:
        str: 生成された応答テキスト。
    """
    client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")  # 環境変数からAPI keyを取得
    )
    # print(prompt)

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    # print(response)
    
    return response.content[0].text.strip()

```