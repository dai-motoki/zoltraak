import zoltraak.llms.claude as claude

def test_generate_response():
    """
    generate_response関数のテスト
    """
    model = "claude-3-haiku-20240307"
    prompt = "今日の晩御飯を提案して"
    max_tokens = 100
    temperature = 0.8

    response = claude.generate_response(model, prompt, max_tokens, temperature)

    # レスポンスが文字列であることを確認
    assert isinstance(response, str)


    # レスポンスが空でないことを確認
    assert response.strip() != ""
