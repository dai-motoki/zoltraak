import unittest
import subprocess

class MinimumTestCase(unittest.TestCase):
    def test_zoltraak_only(self):
        """
        zoltraakコマンドをmdファイルの引数なしで実行した場合、正しいエラーメッセージが表示されることを確認します。
        実行例: `zoltraak` コマンドを引数なしで実行した場合、"エラー: 入力ファイルまたはテキストが指定されていません。"というエラーメッセージが表示されるべきです。
        """
        result = subprocess.run(['zoltraak'], capture_output=True, text=True)  # zoltraakコマンドを引数なしで実行し、その結果をresultに格納します。
        print("STDOUT:", result.stdout)  # 標準出力の内容を出力
        print("STDERR:", result.stderr)  # 標準エラーの内容を出力
        self.assertIn("エラー: 入力ファイルまたはテキストが指定されていません。", result.stderr)  # エラーメッセージは標準エラー出力に含まれているはずなので、result.stderrをチェックするように修正

    # def test_zoltraak_with_compiler(self):
    #     """zoltraak "〜したい" -cコマンドのテスト"""
    #     result = subprocess.run(["zoltraak", "テストしたい", "-c", "コンパイラ"], capture_output=True, text=True)
    #     self.assertEqual(result.returncode, 0)
    #     self.assertIn("コンパイル結果", result.stdout)

    # def test_zoltraak_without_compiler(self):
    #     """zoltraak "〜したい" -cコマンド（コンパイラなし）のテスト"""
    #     result = subprocess.run(["zoltraak", "テストしたい", "-c"], capture_output=True, text=True)
    #     self.assertNotEqual(result.returncode, 0)
    #     self.assertIn("エラー: 入力ファイルまたはテキストが指定されていません。", result.stderr)

    # def test_zoltraak_with_custom_compiler(self):
    #     """zoltraak "〜したい" -cc自作コンパイラのテスト"""
    #     result = subprocess.run(["zoltraak", "テストしたい", "-cc", "自作コンパイラ"], capture_output=True, text=True)
    #     self.assertEqual(result.returncode, 0)
    #     self.assertIn("自作コンパイラの結果", result.stdout)