import os
import pyperclip
import anthropic
from dotenv import load_dotenv
from groq import Groq  # Groqをインポート
import zoltraak
from tqdm import tqdm  # tqdmをインポート
import threading
import time
import sys
import zoltraak.settings
import zoltraak.llms.claude as claude
import re

load_dotenv()  # .envファイルから環境変数を読み込む
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")  # 環境変数からAnthropicのAPI keyを取得
groq_api_key = os.getenv("GROQ_API_KEY")  # 環境変数からGroqのAPI keyを取得

def generate_md_from_prompt(
    goal_prompt,
    target_file_path,
    developer="anthropic",  # デベロッパーを指定する引数を追加
    model_name="claude-3-opus-20240229",  # モデル名の引数を独立させる
    compiler_path=None,
    formatter_path=None,
    language=None, #汎用言語指定
    readme_lang=None, # Readme翻訳先言語指定
    open_file=False,  # ファイルを開くかどうかのフラグを追加
):
    """
    promptから要件定義書（マークダウンファイル）を生成する関数

    Args:
        goal_prompt (str): 要件定義書の生成に使用するプロンプト
        target_file_path (str): 生成する要件定義書のパス
        developer (str): 使用するデベロッパー（デフォルトは "anthropic"）
        model_name (str): 使用するモデルの名前（デフォルトは "claude-3-opus-20240229"）
        compiler_path (str): コンパイラのパス（デフォルトはNone）
        formatter_path (str): フォーマッタのパス（デフォルトはNone）
        open_file (bool): ファイルを開くかどうかのフラグ（デフォルトはTrue）
    """
    # プロンプトコンパイラとプロンプトフォーマッタを変数として受け取る
    if compiler_path is not None and "grimoires" in compiler_path:                                          # grimoires/ディレクトリにコンパイラパスが含まれている場合
        prompt_compiler = os.path.basename(compiler_path)                     # - コンパイラパスからファイル名のみを取得してprompt_compilerに代入
    else:                                                                     # grimoires/ディレクトリにコンパイラパスが含まれていない場合
        prompt_compiler = compiler_path                                       # - コンパイラパスをそのままprompt_compilerに代入
    
    # 汎用言語フォーマッタへの変更
    if language is not None:
        # formatter_pathに_lang.mdが存在するならそれを、しないならformatter_pathのまま
        lang_formatter_path = os.path.splitext(formatter_path)[0] + "_lang.md"
        if os.path.exists(lang_formatter_path):
            formatter_path = lang_formatter_path
    
    # フォーマッターについて、デフォフォルダの時見栄えをシンプルにする
    if "grimoires" in formatter_path:                                         # grimoires/ディレクトリにフォーマッタパスが含まれている場合
        prompt_formatter = os.path.basename(formatter_path)                   # - フォーマッタパスからファイル名のみを取得してprompt_formatterに代入
    else:                                                                     # grimoires/ディレクトリにフォーマッタパスが含まれていない場合
        prompt_formatter = formatter_path                                     # - フォーマッタパスをそのままprompt_formatterに代入
    
    print(f"""
ステップ1. 起動術式を用いて魔法術式を構築する
==============================================================
\033[31m起動術式\033[0m (プロンプトコンパイラ)   : {prompt_compiler}
\033[32m魔法術式\033[0m (要件定義書)             : {target_file_path}
\033[34m錬成術式\033[0m (プロンプトフォーマッタ) : {prompt_formatter}
\033[90m言霊\033[0m   (LLMベンダー・モデル 名)   : {developer}/{model_name}{" → claude-3-sonnet-20240229(2回目以降)" if readme_lang is not None else ""}
ファイルを開く                    : {open_file}
==============================================================
    """)


    prompt = create_prompt(goal_prompt, compiler_path, formatter_path, language, readme_lang)  # プロンプトを作成
    done = False                                                        # スピナーの終了フラグを追加
    spinner_thread = threading.Thread(                                  # スピナーを表示するスレッドを作成し、終了フラグとgoalを渡す
        target=show_spinner,
        args=(lambda: done, f"ステップ1. \033[31m起動術式\033[0mを用いて\033[32m魔法術式\033[0mを構築")           
    )                                                                   #
    spinner_thread.start()                                              # スピナーの表示を開始
    response = generate_response(                                       # developerごとの分岐を関数化して応答を生成
        developer, model_name, prompt                                   #
    )
    
    # 翻訳時
    iteration = 0
    while readme_lang is not None and response.find("END OF TRANSLATION") < 0 and iteration < 5:
        prompt = prompt[0:prompt.find("## Task")] + f"\n\n## Additional Task.\n\n Your translation is still incomplete. Continue with your translating above from Japanese into {readme_lang} by detecting the restarting point, which is equivalent to the end of \"Current Progress\" section. Keep all the original structures as is, which include but are not limited to: links, image links, tags, and the markdown format. Only output the continued part of the translation result. Make sure you continue until the end, which is equivalent to the end of \"超大事なことメモ\" section above. DO NOT INCLUDE THIS \"Additional Task\" SECTION ITSELF AND BELOW. When and only when you finished your translation, that is, when everything above this \"Additional Task\" section is translated, write \"END OF TRANSLATION\" in English at the end of the line.\n\n## Current Progress\n{response.strip()}"
        print("") # レイアウト崩れ防止の改行
        # print(prompt) # デバッグ用
        # print(len(response.split("\n"))) # デバッグ用
        print("翻訳が途中で途切れたため、継続します。")
        response = response.strip() + generate_response(developer, "claude-3-sonnet-20240229", prompt).strip() # 2回目以降の不安定さはモデル性能で殴って解決する
        iteration += 1

    done = True                                                         # 応答生成後にスピナーの終了フラグをTrueに設定
    spinner_thread.join()                                               # スピナーの表示を終了
    md_content = response.strip()                                       # 生成された要件定義書の内容を取得し、前後の空白を削除
    save_md_content(md_content, target_file_path, readme_lang)        # 生成された要件定義書の内容をファイルに保存
    print_generation_result(target_file_path, compiler_path, readme_lang, open_file)                # 生成結果を出力し、open_fileフラグに応じてファイルを開く

def show_spinner(done, goal):
    """スピナーを表示する関数

    Args:
        done (function): スピナーを終了するかどうかを判定する関数
    """
    progress_bar = "━" * 22

    spinner_base = goal + "中... 🪄 "
    spinner_animation = [
        f"{progress_bar[:i]}☆ﾟ.*･｡ﾟ{' ' * (len(progress_bar) - i)}"
        for i in range(1, len(progress_bar) + 1)
    ] + [f"{progress_bar}☆ﾟ.*･｡"]
    spinner = [spinner_base + anim for anim in spinner_animation]
    
    while not done():                                                   # done()がFalseの間、スピナーを表示し続ける
        for cursor in spinner:                                          # - スピナーのアニメーションパターンを順番に処理
            sys.stdout.write(cursor + "\b" * (len(cursor)+100))          # -- カーソル文字を出力し、その文字数分だけバックスペースを出力して上書き
            sys.stdout.flush()                                          # -- 出力をフラッシュして即時表示
            time.sleep(0.1)                                             # -- 0.1秒のディレイを追加



def generate_response(developer, model_name, prompt):
    """
    対応デベロッパーごとに分岐してレスポンスを生成する関数

    現在対応しているデベロッパーとモデルは以下の通りです:
    - Anthropic: 
      - claude-3-opus-20240229
      - claude-3-sonnet-20240229
      - claude-3-haiku-20240307
    - Groq:
      - llama3-8b-8192
      - llama3-70b-8192
      - llama2-70b-4096
      - mixtral-8x7b-32768
      - gemma-7b-it

    Args:
        developer (str): 使用するデベロッパー名（"anthropic" または "groq"）
        model_name (str): 使用するモデルの名前
        prompt (str): APIに送信するプロンプト

    Returns:
        str: APIから生成されたレスポンス
    """
    if developer == "groq":  # Groqを使用する場合
        response = create_prompt_and_get_response_groq(model_name, prompt)
    elif developer == "anthropic":  # Anthropicを使用する場合
        response = claude.generate_response(model_name, prompt, 4000, 0.7)
    else:  # 想定外のデベロッパーの場合
        raise ValueError(
            f"サポートされていないデベロッパー: {developer}。"
            "サポートされているデベロッパーは 'anthropic' と 'groq' です。"
        )

    return response


def create_prompt_and_get_response_groq(model, prompt):
    """
    Groq APIを使用して、指定されたモデルでプロンプトに基づいてテキストを生成する関数

    Args:
        model (str): 使用するモデルの名前
        prompt (str): 送信するプロンプト

    Returns:
        str: 生成されたテキスト
    """
    client = Groq(api_key=groq_api_key)  # Groq APIクライアントを作成
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )
    return chat_completion.choices[0].message.content.strip()

def create_prompt(goal_prompt, compiler_path=None, formatter_path=None, language=None, readme_lang=None):
    """
    LLMへのプロンプトを作成する関数

    Args:
        goal_prompt (str): 要件定義書の生成に使用するプロンプト
        compiler_path (str): コンパイラのパス
        formatter_path (str): フォーマッタのパス

    Returns:
        str: 作成されたプロンプト
    """
    # prompt_file = "grimoires/compiler/dev_obj.md"  # デフォルトのプロンプトファイルのパスを指定
    # if compiler_path:  # コンパイラパスが指定されている場合
        # prompt_file = compiler_path  # - プロンプトファイルのパスをコンパイラパスに変更

    formatter = get_formatter(formatter_path, language, readme_lang)

    if compiler_path is None:
        # 検索関数の起動
        zoltraak_dir = os.path.dirname(zoltraak.__file__)
        compiler_folder = f"{zoltraak_dir}/grimoires/compiler"
        compiler_files = [file for file in os.listdir(compiler_folder) if file.endswith(".md")]

        prompt = "以下のファイルから、goal_promptに最も適したものを選んでください。\n\n"

        for file in compiler_files:
            file_path = os.path.join(compiler_folder, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().split("\n")[:3]
            prompt += f"## {file}\n```\n{' '.join(content)}\n```\n\n"

        prompt += f"## goal_prompt\n\n```{goal_prompt}```\n\n"
        prompt += f"""まず、goal_promptを踏まえて、最初に取るべきステップを明示してください。
        そのステップやgoal_prompt自身と比較して、最も適切なファイルを上位5つ選び、それぞれの理由とともに説明してください。
        また、それぞれの実行プロンプトを、zoltraak \"{goal_prompt}\" -c [ファイル名（拡張子なし）]で、code blockに入れて添付してください。"""
        prompt += prompt + formatter
    elif os.path.exists(compiler_path):  # プロンプトファイルが存在する場合
        with open(compiler_path, "r", encoding = "utf-8") as file:  # - プロンプトファイルを読み込みモードで開く
            prompt = file.read()  # -- プロンプトファイルの内容を読み込み、goal_promptを埋め込む
        prompt = prompt + formatter  # - プロンプトにフォーマッタを追加
    else:  # プロンプトファイルが存在しない場合
        print(f"プロンプトファイル {compiler_path} が見つかりません。")  # - エラーメッセージを表示
        prompt = ""

    if prompt != "" and language is not None:
        if not formatter_path.endswith("_lang.md"):
            prompt = formatter[formatter.rindex("## Output Language"):]  + "\n- Follow the format defined in the format section. DO NOT output the section itself." + prompt # 言語指定の強調前出しでサンドイッチにしてみる。
        elif re.match("(english|英語|en)", language.lower()):
            prompt = formatter + prompt # 特に英語指示が「デフォルト言語指示」と混同されやすく、効きがやたら悪いので英語の場合は挟み撃ちにする

    if readme_lang is not None:
        prompt = re.sub(r'\n{3,}', '\n\n', prompt) # 連続しすぎた改行が悪さするっぽいので

    # print(prompt) # デバッグ用
    return prompt


def get_formatter(formatter_path, language=None, readme_lang=None):
    """
    フォーマッタを取得する関数

    Args:
        formatter_path (str): フォーマッタのパス

    Returns:
        str: フォーマッタの内容
    """
    if readme_lang is not None:
        formatter = f"\n\n---\n\n## Task\nTranslate above into {readme_lang}. Translate everything. Keep all the original structures as is, which include but are not limited to: links, image links, tags, and the markdown format. Only output the translated result. Make sure you continue until the end, which is equivalent to the \"超大事なことメモ\" section above. When and only when you finished your translation, that is, when everything in the original document is translated, write \"END OF TRANSLATION\" in English at the end of the line."
    elif formatter_path is None:  # フォーマッタパスが指定されていない場合
        formatter = ""  # - フォーマッタを空文字列に設定
    else:  # フォーマッタパスが指定されている場合
        if os.path.exists(formatter_path):  # -- フォーマッタファイルが存在する場合
            with open(formatter_path, "r", encoding = "utf-8") as file:  # --- フォーマッタファイルを読み込みモードで開く
                formatter = file.read()  # ---- フォーマッタの内容を読み込む
                if language is not None:
                    # print(formatter_path) # デバッグ用
                    if formatter_path.endswith("_lang.md"):
                        formatter = formatter.replace("{language}", language)
                    else:
                        formatter += f"\n- You must output everything including code block and diagrams, according to the previous instructions, but make sure you write your response in {language}.\n\n## Output Language\n- You must generate your response using {language}, which is the language of the formatter just above this sentence."
        else:  # -- フォーマッタファイルが存在しない場合
            print(f"フォーマッタファイル {formatter_path} が見つかりません。")  # --- エラーメッセージを表示
            formatter = ""  # --- フォーマッタを空文字列に設定

    return formatter


def save_md_content(md_content, target_file_path, readme_lang=None):
    """
    生成された要件定義書の内容をファイルに保存する関数

    Args:
        md_content (str): 生成された要件定義書の内容
        target_file_path (str): 保存先のファイルパス
    """
    output_dir = ""
    if readme_lang is not None:
        output_dir = os.path.dirname(zoltraak.__file__)
    # TODO --ouput-dir引数対応
    else:
        output_dir = "requirements"                                         # 生成された要件定義書をrequirements/の中に格納する
        os.makedirs(output_dir, exist_ok=True)                              # - requirements/ディレクトリを作成（既に存在する場合は何もしない）
    target_file_name = os.path.basename(target_file_path)                     # - ターゲットファイルのファイル名を取得
    target_file_path = os.path.join(output_dir, target_file_name)       # - outputディレクトリとファイル名を結合してターゲットファイルのパスを生成
    with open(target_file_path, "w", encoding = "utf-8") as target_file:                          # ターゲットファイルを書き込みモードで開く
        target_file.write(md_content)                                         # - 生成された要件定義書の内容をファイルに書き込む

def print_generation_result(target_file_path, compiler_path, readme_lang=None, open_file=False):
    """
    要件定義書の生成結果を表示する関数

    Args:
        target_file_path (str): 生成された要件定義書のファイルパス
        compiler_path (str): コンパイラのパス
        open_file (bool): ファイルを開くかどうかのフラグ（デフォルトはTrue）
    """
    req = "requirements"
    target_file_path = f"{req}/{target_file_path}" if readme_lang is None else f"{os.path.dirname(zoltraak.__file__)}/{target_file_path}"
    print(f"\033[32m魔法術式を構築しました: {target_file_path}\033[0m")  # 要件定義書の生成完了メッセージを緑色で表示
    
    # 検索結果生成以外ではユーザーに要件定義書からディレクトリを構築するかどうかを尋ねる
    if  compiler_path is not None and readme_lang is None and input("\033[32m魔法術式\033[0mから\033[33m領域術式\033[0mを実行しますか？ (y/n): ").lower() == 'y':
        # ユーザーがyと答えた場合、zoltraakコマンドを実行してディレクトリを構築
        done = False  # スピナーの終了フラグを追加
        spinner_thread = threading.Thread(  # スピナーを表示するスレッドを作成し、終了フラグとgoalを渡す
            target=show_spinner,
            args=(lambda: done, f"ステップ2. \033[32m魔法式\033[0mから\033[33m領域\033[0mを構築")
        )
        spinner_thread.start()  # スピナーの表示を開始
        
        import subprocess
        subprocess.run(["zoltraak", target_file_path])
        
        done = True  # zoltraakコマンド実行後にスピナーの終了フラグをTrueに設定
        spinner_thread.join()  # スピナーの表示を終了
    else:
        # ユーザーがnと答えた場合、既存の手順を表示
        print(f"\033[33m以下のコマンドをコピーして、ターミナルに貼り付けて実行してください。\033[0m")  # 実行方法の説明を黄色で表示
        print(f"\033[36mzoltraak {target_file_path}\033[0m")  # 実行コマンドを水色で表示
        pyperclip.copy(f"zoltraak {target_file_path}")  # 実行コマンドをクリップボードにコピー
        print("\033[35mコマンドをクリップボードにコピーしました。ターミナルに貼り付けて実行できます。\033[0m")  # コピー完了メッセージを紫色で表示
        if open_file:  # open_fileフラグがTrueの場合
            print("中身を確認するオプションがONであるため、ファイルを開きます。")
            os.system(f"code {target_file_path}")  # ファイルを開く（VSCodeにおける`code syllabus_graph.png`に相当）
        