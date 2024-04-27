import os
import anthropic
from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む

def generate_response(prompt):
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
        # model="claude-3-opus-20240229",
        model="claude-3-haiku-20240307",
        max_tokens=100,
        temperature=0.7,
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

    print(response)
    
    return response.content[0].text.strip()
