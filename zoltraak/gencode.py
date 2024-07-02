import os
import shutil
import subprocess
import zoltraak
import zoltraak.llms.claude as claude
import zoltraak.llms.gemini as gemini
from zoltraak.utils.prompt_import import load_prompt
from zoltraak.llms.claude import generate_response
class TargetCodeGenerator:
    def __init__(self, source_file_path, target_file_path, past_source_file_path, source_hash):
        self.source_file_path = source_file_path
        self.target_file_path = target_file_path
        self.past_source_file_path = past_source_file_path
        self.source_hash = source_hash

    def generate_target_code(self):
        """
        ソースファイルからターゲットファイルを生成するメソッド
        """
        # 1. 準備
        create_domain_grimoire, target_dir = self.prepare_generation()

        # 2. ソースファイルの読み込みと変数の作成
        source_content, source_file_name, variables = self.load_source_and_create_variables()
        
        # 3. プロンプトの読み込みとコード生成
        prompt, code = self.load_prompt_and_generate_code(create_domain_grimoire, variables)
        
        # 4. 生成されたコードの処理
        self.process_generated_code(code)
            
        # 5. 結果の出力
        self.output_results()
        
    def prepare_generation(self, step_n=2):
        """
        ターゲットコード生成の準備を行うメソッド
        
        Args:
            step_n (int): ステップ番号。デフォルトは2。
        """
        create_domain_grimoire = "grimoires/architect/architect_claude.md"       # 領域術式（要件定義書）のパスを指定
        target_dir = (                                                            # target_file_pathからdevと.mdを省いて、generated/ の下につなげたものをtarget_dirに設定
            f"generated/{os.path.splitext(os.path.basename(self.target_file_path))[0]}"
        )
        
        if step_n == 2:
            self.print_step2_info(create_domain_grimoire, target_dir)             # ステップ2の情報を出力
        elif step_n == 3:
            self.print_step3_info(target_dir)                                     # ステップ3の情報を出力

        if self.past_source_file_path is not None:                                # 過去のソースファイルパスが指定されている場合
            self.save_current_source_as_past()                                    # - 現在のソースファイルを過去のソースファイルとして保存
        
        return create_domain_grimoire, target_dir
    
    def print_step2_info(self, create_domain_grimoire, target_dir):
        """
        ステップ2の情報を出力するメソッド
        """
        print(                                                                    
            f"""

==============================================================
ステップ2. 魔法術式を用いて領域術式を実行する
\033[32m領域術式\033[0m                      : {create_domain_grimoire}
\033[32m実行術式\033[0m                      : {self.target_file_path}
\033[32m領域対象\033[0m (ディレクトリパス)    : {target_dir}
==============================================================
        """
        )

    def print_step3_info(self, target_dir):
        """
        ステップ3の情報を出力するメソッド
        """
        print(
            f"""

==============================================================
ステップ3. 展開術式を実行する  
\033[32m展開対象\033[0m (ディレクトリパス)    : {target_dir}
==============================================================
        """
        )
    def load_source_and_create_variables(self):
        """
        ソースファイルの読み込みと変数の作成を行うメソッド
        """
        source_content   = self.read_source_file()                                # ソースファイルの内容を読み込む
        source_file_name = self.get_source_file_name()                            # ソースファイルのファイル名（拡張子なし）を取得
        variables        = self.create_variables_dict(source_content, source_file_name)  # 変数の辞書を作成
        
        return source_content, source_file_name, variables

    def load_prompt_and_generate_code(self, create_domain_grimoire, variables):
        """
        プロンプトの読み込みとコード生成を行うメソッド
        """
        prompt = self.load_prompt_with_variables(create_domain_grimoire, variables)  # 領域術式（要件定義書）からプロンプトを読み込み、変数を埋め込む
        print(prompt)
        code   = self.generate_code_with_claude(prompt)                           # Claudeを使用してコードを生成
        # print(code)
        
        return prompt, code

    def process_generated_code(self, code):
        """
        生成されたコードの処理を行うメソッド
        """
        self.write_code_to_target_file(code)                                      # 生成されたコードをターゲットファイルに書き込む
        
        if self.source_hash is not None:                                          # ソースファイルのハッシュ値が指定されている場合
            self.append_source_hash_to_target_file()                              # - ソースファイルのハッシュ値をターゲットファイルに追記
            
        if self.target_file_path.endswith(".py"):                                 # ターゲットファイルがPythonファイルの場合
            self.try_execute_generated_code(code)                                 # - 生成されたコードを実行
        else:                                                                     # ターゲットファイルがマークダウンファイルの場合
            return code                                                           # - 生成されたコードを返す

    def output_results(self):
        """
        結果の出力を行うメソッド  
        """
        self.print_target_file_path()                                             # ターゲットファイルのパスを出力
        self.open_target_file_in_vscode()                                         # ターゲットファイルをVS Codeで開く
        
        # if self.target_file_path.endswith(".py"):                                 # ターゲットファイルがPythonファイルの場合
        #     self.run_python_file()                                                # - Pythonファイルを実行
            

    def save_current_source_as_past(self):
        """
        現在のソースファイルを過去のソースファイルとして保存するメソッド
        """
        shutil.copy(self.source_file_path, self.past_source_file_path)                  
        
    def read_source_file(self):
        """
        ソースファイルの内容を読み込むメソッド
        """
        with open(self.source_file_path, "r", encoding="utf-8") as source_file:        
            source_content = source_file.read()                                   
        return source_content

    def get_source_file_name(self):
        """
        ソースファイルのファイル名（拡張子なし）を取得するメソッド
        """
        source_file_name = os.path.splitext(os.path.basename(self.source_file_path))[0]
        if source_file_name.startswith("def_"):                                   
            source_file_name = source_file_name[4:]                               
        return source_file_name

    def create_variables_dict(self, source_content, source_file_name):
        """
        変数の辞書を作成するメソッド
        """
        variables = {                                                             
            "source_file_path": self.source_file_path,                                 
            "source_file_name": source_file_name,                                 
            "source_content": source_content,                                     
        }
        return variables

    def load_prompt_with_variables(self, create_domain_grimoire, variables):
        """
        領域術式（要件定義書）からプロンプトを読み込み、変数を埋め込むメソッド
        """
        zoltraak_dir = os.path.dirname(zoltraak.__file__)                         
        prompt = load_prompt(f"{zoltraak_dir}/{create_domain_grimoire}", variables)
        return prompt

    def generate_code_with_claude(self, prompt):
        """
        Claudeを使用してコードを生成するメソッド
        """
        # print("geminiを使用してコードを生成します")
        # code = gemini.generate_response(
        #     "gemini-1.5-pro"
        #     , prompt, 8192, 1
        # )
        code = claude.generate_response(                                          
            # "claude-3-haiku-20240307"
            # "claude-3-opus-20240229"
            "claude-3-5-sonnet-20240620"
            , prompt, 4000, 0.3                          
        )
        code = code.replace("```python", "").replace("```", "")                   
        return code

    def write_code_to_target_file(self, code):
        """
        生成されたコードをターゲットファイルに書き込むメソッド
        """
        os.makedirs(os.path.dirname(self.target_file_path), exist_ok=True)             
        with open(self.target_file_path, "w", encoding="utf-8") as target_file:        
            target_file.write(code)                                               

    def append_source_hash_to_target_file(self):
        """
        ソースファイルのハッシュ値をターゲットファイルに追記するメソッド
        """
        with open(self.target_file_path, "a", encoding="utf-8") as target_file:    
            target_file.write(f"\n# HASH: {self.source_hash}\n")                   
        print(f"ターゲットファイルにハッシュ値を埋め込みました: {self.source_hash}")           

    def try_execute_generated_code(self, code):
        """
        生成されたコードを実行するメソッド
        """
        while True:
            try:
                exec(code)
                break
            except Exception as e:
                print(f"Pythonファイルの実行中にエラーが発生しました。")
                print(f"\033[91mエラーメッセージ: {str(e)}\033[0m")
                print(f"エラーが発生したPythonファイルのパス: \033[33m{self.target_file_path}\033[0m")
                
                while True:
                    prompt = f"""
                    以下のPythonコードにエラーがあります。修正してください。
                    コード: {code}
                    エラーメッセージ: {str(e)}
                    プログラムコードのみ記載してください。
                    """
                    code = generate_response(
                        model="claude-3-haiku-20240307",
                        # model="claude-3-opus-20240229",
                        prompt=prompt,
                        max_tokens=4000,
                        temperature=0.3
                    )
                    code = code.replace("```python", "").replace("```", "")
                    
                    print("修正したコードを再実行します。")
                    try:
                        exec(code)
                        print("コードの実行が成功しました。")
                        break
                    except Exception as e:
                        print(f"修正後のコードでもエラーが発生しました。再度修正を試みます。")
                        print(f"\033[91m修正後のエラーメッセージ: {str(e)}\033[0m")
                
                with open(self.target_file_path, "w", encoding="utf-8") as target_file:
                    target_file.write(code)

            # except Exception as e:
            #     print(f"Pythonファイルの実行中にエラーが発生しました。")
            #     print(f"\033[91mエラーメッセージ: {str(e)}\033[0m")
            #     print(f"エラーが発生したPythonファイルのパス: \033[33m{self.target_file_path}\033[0m")
                
            #     prompt = f"""
            #     Pythonファイルの実行中に以下のエラーが発生しました。
            #     ファイルの内容: {code}
            #     エラーメッセージ: {str(e)}
            #     考えられるエラーの原因と解決方法を教えてください。
            #     """
            #     response = generate_response(
            #         model="claude-3-haiku-20240307",
            #         prompt=prompt,
            #         max_tokens=1000,
            #         temperature=0.7
            #     )
            #     print(f"\033[33m{response}\033[0m")
            #     print("")
                
            #     user_input = input("コードを再実行しますか？ (y/n): ")
            #     if user_input.lower() != 'y':
            #         break
            #     else:
            #         prompt = f"""
            #         以下のPythonコードにエラーがあります。修正してください。
            #         コード: {code}
            #         エラーメッセージ: {str(e)}
            #         プログラムコードのみ記載してください。
            #         """
            #         code = generate_response(
            #             model="claude-3-haiku-20240307",
            #             prompt=prompt,
            #             max_tokens=4000,
            #             temperature=0.3
            #         )
            #         code = code.replace("```python", "").replace("```", "")
                
            #     print("次のコードを実行してください:")
            #     print(f"python {self.target_file_path}")
            #     import pyperclip
            #     pyperclip.copy(f"python {self.target_file_path}")
            #     print("コードをクリップボードにコピーしました。")
    def print_target_file_path(self):
        """
        ターゲットファイルのパスを出力するメソッド
        """
        print(f"ターゲットファイルのパス: {self.target_file_path}")                           

    def open_target_file_in_vscode(self):
        """
        ターゲットファイルをVS Codeで開くメソッド
        """
        os.system(f"code {self.target_file_path}")                                     

    def run_python_file(self):
        """
        Pythonファイルを実行するメソッド
        """
        print(f"Pythonファイルを実行します: {self.target_file_path}")                    
        subprocess.run(["python", self.target_file_path])                          
