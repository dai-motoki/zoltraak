import os
import anthropic
from zoltraak import settings
from large_language_model import LargeLanguageModel

class AnthropicModel(LargeLanguageModel):
    def __init__(self, model):
        self.model = model
        self.client = anthropic.Anthropic(
            api_key=os.environ.get("ANTHROPIC_API_KEY")  # 環境変数からAPI keyを取得
        )

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
