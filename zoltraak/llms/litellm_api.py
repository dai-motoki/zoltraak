from litellm import completion



def generate_response(model, prompt, max_tokens, temperature):
    """
    LiteLLM APIを使用してプロンプトに対する応答を生成する関数。

    Args:
        prompt (str): 応答を生成するためのプロンプト。
        max_tokens (int): 生成する最大トークン数。
        temperature (float): 生成時の温度パラメータ。

    Returns:
        str: 生成された応答テキスト。
    """
    response = completion(
        model=model,
        messages=[{"content": prompt, "role": "user"}],
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response

if __name__ == "__main__":
    model = "claude-3-haiku-20240307"
    prompt = "今日の晩御飯を提案して"
    max_tokens = 100
    temperature = 0.8

    response = generate_response(model, prompt, max_tokens, temperature)

    print(response)