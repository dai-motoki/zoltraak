
def load_prompt(file_path, variables):
    """
    プロンプトファイルを読み込み、変数を置換する汎用関数

    Args:
        file_path (str): プロンプトファイルのパス
        variables (dict): 置換する変数の辞書

    Returns:
        str: 変数が置換されたプロンプト
    """
    with open(file_path, "r") as f:
        prompt_template = f.read()
    
    prompt = prompt_template
    for key, value in variables.items():
        prompt = prompt.replace(f'[{key}]', value)
    
    return prompt