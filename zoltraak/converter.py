import subprocess
import anthropic
import os
import hashlib
from dotenv import load_dotenv
from zoltraak.md_generator import generate_md_from_prompt
import zoltraak

import zoltraak.settings
import zoltraak.llms.claude as claude
from zoltraak.gencode import TargetCodeGenerator


class MarkdownToPythonConverter:
    def __init__(self, md_file_path, py_file_path, prompt=None, compiler_path=None, formatter_path=None, language=None):
        self.md_file_path = md_file_path
        self.py_file_path = py_file_path
        self.prompt = prompt
        self.compiler_path = compiler_path
        self.formatter_path = formatter_path
        self.language = language
        self.client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    def convert(self):
        if self.prompt is None:                                                                                  # プロンプトが指定されていない場合
            self.source_file_path = self.md_file_path                                                            # - ソースファイルパスをマークダウンファイルパスに設定
            self.target_file_path = self.py_file_path                                                            # - ターゲットファイルパスをPythonファイルパスに設定
            self.past_source_folder = "past_md_files"                                                            # - 過去のソースフォルダを "past_md_files" に設定
        else:                                                                                                    # プロンプトが指定されている場合
            self.source_file_path = self.md_file_path                                                            # - ソースファイルパスをマークダウンファイルパスに設定
            self.target_file_path = self.md_file_path                                                            # - ターゲットファイルパスをマークダウンファイルパスに設定
            self.past_source_folder = "past_prompt_files"                                                        # - 過去のソースフォルダを "past_prompt_files" に設定

            if os.path.exists(self.md_file_path):                                                                # -- マークダウンファイルが存在する場合
                print(f"{self.md_file_path}は既存のファイルです。promptに従って変更を提案します。")                      # --- ファイルが既存であることを示すメッセージを表示
                self.propose_target_diff(self.target_file_path, self.prompt)                                     # --- プロンプトに従ってターゲットファイルの差分を提案
                return                                                                                           # --- 関数を終了

        if os.path.exists(self.source_file_path):                                                                # ソースファイルが存在する場合
            self.source_hash = self.calculate_file_hash(self.source_file_path)                                   # - ソースファイルのハッシュ値を計算
            os.makedirs(self.past_source_folder, exist_ok=True)                                                  # - 過去のソースフォルダを作成（既存の場合はスキップ）
            self.past_source_file_path = os.path.join(
                self.past_source_folder, os.path.basename(self.source_file_path))                                # - 過去のソースファイルパスを設定

        if os.path.exists(self.target_file_path):                                                                # ターゲットファイルが存在する場合
            self.handle_existing_target_file()                                                                   # - 既存のターゲットファイルを処理
        else:                                                                                                    # ターゲットファイルが存在しない場合
            self.handle_new_target_file()                                                                        # - 新しいターゲットファイルを処理

    def calculate_file_hash(self, file_path):
        with open(file_path, "rb") as file:
            content = file.read()
            return hashlib.md5(content).hexdigest()

    def handle_existing_target_file(self):
        with open(self.target_file_path, "r", encoding="utf-8") as target_file:
            lines = target_file.readlines()
            if len(lines) > 0 and lines[-1].startswith("# HASH: "):
                embedded_hash = lines[-1].split("# HASH: ")[1].strip()
                if self.source_hash == embedded_hash:
                    if self.prompt is None:
                        subprocess.run(["python", self.target_file_path])
                    else:
                        with open(self.target_file_path, "r", encoding="utf-8") as md_file:
                            md_content = md_file.read()
                        return md_content
                else:
                    print(f"{self.source_file_path}の変更を検知しました。")
                    print("ソースファイルの差分:")
                    if os.path.exists(self.past_source_file_path):
                        self.display_source_diff()

    def display_source_diff(self):
        import difflib
        with open(self.past_source_file_path, "r", encoding="utf-8") as old_source_file:
            old_source_lines = old_source_file.readlines()
        with open(self.source_file_path, "r", encoding="utf-8") as new_source_file:
            new_source_lines = new_source_file.readlines()

        source_diff = difflib.unified_diff(old_source_lines, new_source_lines, lineterm='', n=0)
        source_diff_text = ''.join(source_diff)
        print(source_diff_text)

        if self.prompt is not None:
            self.propose_target_diff(self.target_file_path, self.prompt)
            print(f"ターゲットファイル: {self.target_file_path}")
            input("修正が完了したらEnterキーを押してください。")
        else:
            self.handle_target_file_modification()

    def handle_new_target_file(self):
        if self.prompt is None:
            print(f"""
高級言語コンパイル中: {self.target_file_path}は新しいファイルです。少々お時間をいただきます。
{self.source_file_path} -> {self.target_file_path}
                  """)
            target = TargetCodeGenerator(self.source_file_path, self.target_file_path, self.past_source_file_path, self.source_hash)
            target.generate_target_code()
        else:
            print(f"""
{"検索結果生成中" if self.compiler_path is None else "要件定義書執筆中"}: {self.target_file_path}は新しいファイルです。少々お時間をいただきます。
                  """)
            generate_md_from_prompt(
                self.prompt,
                self.target_file_path,
                developer="anthropic",
                model_name="claude-3-haiku-20240307",
                # model_name="claude-3-opus-20240229",
                compiler_path=self.compiler_path,
                formatter_path=self.formatter_path,
                language=self.language,
                open_file=True
            )

    def propose_target_diff(self, target_file_path, prompt):
        """
        ターゲットファイルの変更差分を提案する関数

        Args:
            target_file_path (str): 現在のターゲットファイルのパス
            prompt (str): promptの内容
        """
        # プロンプトにターゲットファイルの内容を変数として追加
        with open(target_file_path, "r", encoding="utf-8") as target_file:
            current_target_code = target_file.read()

        prompt = f'''
現在のターゲットファイルの内容:
{current_target_code}
上記からpromptの内容:
{prompt}
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
        response = self.client.messages.create(
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
                self.apply_diff_to_target_file(target_file_path, target_diff)
                print(f"{target_file_path}に差分を自動で適用しました。")
                break
            elif choice == '2':
                print("手動で差分を適用してください。")
                break
            elif choice == '3':
                print("操作をキャンセルしました。")
                break
            else:
                print("無効な選択です。もう一度選択してください。")
                print("1. 自動で適用する")
                print("2. エディタで行う")
                print("3. 何もせず閉じる")
                choice = input("選択してください (1, 2, 3): ")

    def apply_diff_to_target_file(self, target_file_path, target_diff):
        """
        提案された差分をターゲットファイルに適用する関数

        Args:
            target_file_path (str): ターゲットファイルのパス
            target_diff (str): 適用する差分
        """
        # ターゲットファイルの現在の内容を読み込む
        with open(target_file_path, "r", encoding="utf-8") as file:
            current_content = file.read()

        # プロンプトを作成してAPIに送信し、修正された内容を取得
        prompt = f'''
現在のターゲットファイルの内容:
{current_content}
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
        modified_content = claude.generate_response("claude-3-sonnet-20240229", prompt, 2000, 0.3)

        # 修正後の内容をターゲットファイルに書き込む
        with open(target_file_path, "w", encoding="utf-8") as file:
            file.write(modified_content)

        print(f"{target_file_path}に修正を適用しました。")
