

from litellm import completion

def generate_response(model_name, prompt, max_tokens=None, temperature=None, api_base=None):
    # print("-------- litellm --------")
    response = completion(
        model=model_name, 
        messages=[{ "content": prompt,"role": "user"}], 
        # api_base="http://localhost:11434", # ollamaなどはこのエンドポイント
        api_base=api_base
    )
    return response['choices'][0].message.content.strip()


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(verbose=True)

    response = generate_response("groq/llama3-70b-8192", "こんにちは !! 今日の気分はどう？")
    print(response)
    print("-------------------")
    response = generate_response("groq/gemma-7b-it", "こんにちは !! 今日の気分はどう？")
    print(response)
    