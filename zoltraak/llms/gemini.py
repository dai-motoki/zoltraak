"""
Google AI Python SDKをインストールする

$ pip install google-generativeai

詳細は以下のガイドを参照してください:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def generate_response(model_name="gemini-1.5-pro", prompt="helloworld", max_tokens=8192, temperature=1):
    """
    Google Generative AIを使用してプロンプトに対する応答を生成する関数。

    Args:
        model_name (str): 使用するモデルの名前。
        prompt (str): 応答を生成するためのプロンプト。
        max_tokens (int): 応答の最大トークン数。
        temperature (float): 応答の多様性を制御する温度パラメータ。

    Returns:
        str: 生成された応答テキスト。
    """
    # モデルの設定
    generation_config = {
        "temperature": temperature,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": max_tokens,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
        history=[]
    )

    response = chat_session.send_message(prompt)

    return response.text

# 使用例
response_text = generate_response("gemini-1.5-pro", "prompt", 8192, 1)
print(response_text)
