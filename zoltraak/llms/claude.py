import os
import anthropic
from zoltraak import settings
from zoltraak.llms.large_language_model import LargeLanguageModel

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
        # APIキーの先頭3文字と末尾3文字のみを表示し、残りは"..."で省略する
        # これにより、APIキーが漏洩することを防ぎつつ、正しいAPIキーが設定されていることを確認できる
        print("ANTHROPIC_API_KEY:" + os.environ.get("ANTHROPIC_API_KEY")[:3] + "..." + os.environ.get("ANTHROPIC_API_KEY")[-3:])
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
        
        return response.content[0].text.strip()

    

if __name__ == "__main__":

    model = "claude-3-haiku-20240307"
    prompt = "今日の晩御飯を提案して"
    max_tokens = 100
    temperature = 0.8
    response = AnthropicModel.generate_response(model, prompt, max_tokens, temperature)

    print(response)

