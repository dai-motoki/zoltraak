import subprocess
import anthropic
import os
import hashlib
from dotenv import load_dotenv
import shutil
from zoltraak.md_generator import generate_md_from_prompt
from zoltraak.utils.prompt_import import load_prompt
import zoltraak
import zoltraak.llms.claude as claude
from zoltraak.gencode import TargetCodeGenerator


load_dotenv()  # .envファイルから環境変数を読み込む
anthropic.api_key = os.getenv("ANTHROPIC_API_KEY")  # 環境変数からAPI keyを取得

def convert_md_to_py(md_file_path, py_file_path, prompt=None, compiler_path=None, formatter_path=None, language=None):
    client = anthropic.Anthropic(api_key=anthropic.api_key)

    if prompt is None:
        source_file_path = md_file_path
        target_file_path = py_file_path
        # デバッグ用のprint文を追加
        # print(f"ソースファイルのパス: {source_file_path}")
        # print(f"ターゲットファイルのパス: {target_file_path}")
        # print(f"プロンプト: {prompt}")
        
        past_source_folder = "past_md_files"
    else:
        source_file_path = md_file_path
        target_file_path = md_file_path
        past_source_folder = "past_prompt_files"
        

        # md_file_pathが存在し、promptがある場合はpropose_target_diffを実行
        if os.path.exists(md_file_path):
            print(f"{md_file_path}は既存のファイルです。promptに従って変更を提案します。")
            propose_target_diff(target_file_path, prompt, client)
            return

    # ソースファイルが存在する場合のみ処理を行う
    if os.path.exists(source_file_path):
        # ソースファイルのハッシュ値を計算
        source_hash = calculate_file_hash(source_file_path)

        # 過去のソースファイルを保存するフォルダのパス
        os.makedirs(past_source_folder, exist_ok=True)

        # 過去のソースファイルのパスを生成
        past_source_file_path = os.path.join(past_source_folder, os.path.basename(source_file_path))

    # ターゲットファイルが存在し、ハッシュ値が一致する場合はターゲットファイルを実行または返す
    if os.path.exists(target_file_path):
        with open(target_file_path, "r", encoding = "utf-8") as target_file:
            lines = target_file.readlines()
            if len(lines) > 0 and lines[-1].startswith("# HASH: "):
                embedded_hash = lines[-1].split("# HASH: ")[1].strip()
                if source_hash == embedded_hash:
                    if prompt is None:
                        # ターゲットファイル（Pythonファイル）を実行
                        subprocess.run(["python", target_file_path])
                    else:
                        # ターゲットファイル（マークダウンファイル）の内容を返す
                        with open(target_file_path, "r", encoding = "utf-8") as md_file:
                            md_content = md_file.read()
                        return md_content
                else:
                    print(f"{source_file_path}の変更を検知しました。")
                    print("ソースファイルの差分:")
                    # 過去のソースファイルが存在する場合は差分を表示
                    if os.path.exists(past_source_file_path):
                        import difflib

                        with open(past_source_file_path, "r", encoding = "utf-8") as old_source_file:
                            old_source_lines = old_source_file.readlines()
                        with open(source_file_path, "r", encoding = "utf-8") as new_source_file:
                            new_source_lines = new_source_file.readlines()

                        # ソースファイルの差分を計算
                        source_diff = difflib.unified_diff(old_source_lines, new_source_lines, lineterm='', n=0)
                        source_diff_text = ''.join(source_diff)

                        print(source_diff_text)

                        if prompt is not None:
                            propose_target_diff(target_file_path, prompt, client)
                            print(f"ターゲットファイル: {target_file_path}")
                            input("修正が完了したらEnterキーを押してください。")
                        else:
                            while True:
                                
                                if not target_file_path.endswith(".md"):
                                    print(f"要件定義書の変更を検知しました。高級言語ファイル: {target_file_path}の修正方法を選択してください:")
                                else:
                                    print(f"要求を受け付けました。要件定義書: {target_file_path}の修正方法を選択してください:")
                                print("1. 変更差分を提案する")
                                print("2. AIですべてのコードを書き直す")
                                print("3. 手動で修正する")
                                print("4. 変更しない")
                                choice = input("選択肢の番号を入力してください (1, 2, 3, 4): ")

                                if choice == "1":
                                    propose_target_diff(target_file_path, source_diff_text, client)
                                    print(f"ターゲットファイル: {target_file_path}")
                                    input("修正が完了したらEnterキーを押してください。")
                                    break
                                elif choice == "2":
                                    target = TargetCodeGenerator(source_file_path, target_file_path, past_source_file_path, source_hash)
                                    target.generate_target_code()
                                    print(f"新しく生成されたターゲットファイル: {target_file_path}")
                                    break
                                elif choice == "3":
                                    print("ターゲットファイルを手動で修正してください。")
                                    print(f"ターゲットファイル: {target_file_path}")
                                    input("修正が完了したらEnterキーを押してください。")
                                    break
                                elif choice == "4":
                                    print("変更しない。")
                                    break
                                else:
                                    print("無効な選択肢です。もう一度入力してください。")
                        
                        # 全ての選択肢でハッシュ値を更新
                        with open(target_file_path, "a", encoding = "utf-8") as target_file:
                            target_file.write(f"\n# HASH: {source_hash}")
                    else:
                        print(f"{source_file_path}は新しいファイルです。")
    else:
        if prompt is None:
            print(f"""
高級言語コンパイル中: {target_file_path}は新しいファイルです。少々お時間をいただきます。
{source_file_path} -> {target_file_path}
                  """)
            # print(past_source_file_path)
            target = TargetCodeGenerator(source_file_path, target_file_path, past_source_file_path, source_hash)
            target.generate_target_code()
            
        else:
            print(f"""
要件定義書執筆中: {target_file_path}は新しいファイルです。少々お時間をいただきます。
                  """)
            generate_md_from_prompt(
                prompt,
                target_file_path,
                developer="anthropic",
                model_name="claude-3-haiku-20240307",
                compiler_path=compiler_path,
                formatter_path=formatter_path,
                language = language,
                open_file=True
            )

def apply_diff_to_target_file(target_file_path, target_diff, client, model="claude-3-sonnet-20240229"):
    """
    提案された差分をターゲットファイルに適用する関数

    Args:
        target_file_path (str): ターゲットファイルのパス
        target_diff (str): 適用する差分
        client (anthropic.Anthropic): Anthropic APIクライアント
        model (str): 使用するモデルの名前（デフォルトは "claude-3-sonnet-20240229"）
    """
    # ターゲットファイルの現在の内容を読み込む
    with open(target_file_path, "r", encoding = "utf-8") as file:
        current_content = file.read()

    # プロンプトを作成してAPIに送信し、修正された内容を取得
    prompt = f'''
現在のターゲットファイルの内容:
{"".join(current_content)}
上記のターゲットファイルの内容に対して、以下のUnified diff 適用後のターゲットファイルの内容を生成してください。

提案された差分:
{target_diff}

例）
変更前
- graph.node(week_node_name, shape='box', style='filled', fillcolor='#FFCCCC')

変更後
+ graph.node(week_node_name, shape='box', style='filled', fillcolor='#CCCCFF')

番号など変わった場合は振り直しもお願いします。
    '''
    modified_content = claude.generate_response(client, model, prompt, 2000, 0.3)

    # 修正後の内容をターゲットファイルに書き込む
    with open(target_file_path, "w", encoding = "utf-8") as file:
        file.write(modified_content)

    print(f"{target_file_path}に修正を適用しました。")
def propose_target_diff(target_file_path, source_diff_text, client):
    """
    ターゲットファイルの変更差分を提案する関数

    Args:
        target_file_path (str): 現在のターゲットファイルのパス
        source_diff_text (str): ソースファイルの差分テキスト、またはpromptの内容
        client (anthropic.Anthropic): Anthropic APIクライアント
    """
    # プロンプトにターゲットファイルの内容を変数として追加
    with open(target_file_path, "r", encoding = "utf-8") as target_file:
        current_target_code = target_file.read()
    
    prompt = f'''
現在のターゲットファイルの内容:
{current_target_code}
上記からソースファイルの差分、またはpromptの内容:
{source_diff_text}
をもとに、

ターゲットファイルの変更が必要な部分"のみ"をプログラムで出力してください。
出力はunified diff形式で、削除した文を薄い赤色、追加した文を薄い緑色にして

@@ -1,4 +1,4 @@
 line1
-line2
+line2 modified
 line3
-line4
+line4 modified

    '''
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.0,
        system="You are a programmer.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    target_diff = response.content[0].text.strip()
    # ターゲットファイルの差分を表示
    print("ターゲットファイルの差分:")
    print(target_diff)

    # ユーザーに適用方法を尋ねる
    print("差分をどのように適用しますか？")
    print("1. AIで適用する")
    print("2. 自分で行う")
    print("3. 何もせず閉じる")
    choice = input("選択してください (1, 2, 3): ")

    while True:
        if choice == '1':
            # 差分をターゲットファイルに自動で適用

            apply_diff_to_target_file(target_file_path, target_diff, client)
            print(f"{target_file_path}に差分を自動で適用しました。")

            # ターゲットファイルがPythonファイルの場合は実行する
            if target_file_path.endswith(".py"):
                print(f"Pythonファイルを実行します: {target_file_path}")
                subprocess.run(["python", target_file_path])



            break
        elif choice == '2':
            # ユーザーが手動で差分を適用するための指示を表示
            print("以下の差分を手動で適用してください:")
            # 差分の内容をクリップボードにコピー
            import pyperclip
            pyperclip.copy(target_diff)
            print("差分をクリップボードにコピーしました。")
            # ターゲットファイルのパスを表示
            print(f"ターゲットファイルを開きます: {target_file_path}")
            # ターゲットファイルをVS Codeで開く
            import subprocess
            subprocess.run(['code', target_file_path])
            # ユーザーにエディタで差分を適用するよう指示
            print("エディタで差分を適用後、Enterキーを押してください。")
            
            # ユーザーの入力（Enterキー）を待機
            input()
            break
        elif choice == '3':
            # 何もせずに閉じる
            print("操作をキャンセルしました。")
            break
        else:
            print("無効な選択です。もう一度選択してください。")
            print("1. 自動で適用する")
            print("2. エディタで行う")
            print("3. 何もせず閉じる")
            choice = input("選択してください (1, 2, 3): ")


def calculate_file_hash(file_path):
    """
    ファイルのハッシュ値を計算する関数

    Args:
        file_path (str): ファイルのパス

    Returns:
        str: ファイルのハッシュ値
    """
    with open(file_path, "rb") as file:
        content = file.read()
        return hashlib.md5(content).hexdigest()

