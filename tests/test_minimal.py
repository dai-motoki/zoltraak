import unittest
import subprocess

class MinimumTestCase(unittest.TestCase):
    def test_zoltraak(self):
        """zoltraakコマンドの基本的な動作テスト"""
        result = subprocess.run(["zoltraak"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Zoltraak", result.stdout)

    def test_zoltraak_with_compiler(self):
        """zoltraak "〜したい" -cコマンドのテスト"""
        result = subprocess.run(["zoltraak", "テストしたい", "-c", "コンパイラ"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("コンパイル結果", result.stdout)

    def test_zoltraak_without_compiler(self):
        """zoltraak "〜したい" -cコマンド（コンパイラなし）のテスト"""
        result = subprocess.run(["zoltraak", "テストしたい", "-c"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("エラー", result.stderr)

    def test_zoltraak_with_custom_compiler(self):
        """zoltraak "〜したい" -cc自作コンパイラのテスト"""
        result = subprocess.run(["zoltraak", "テストしたい", "-cc", "自作コンパイラ"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("自作コンパイラの結果", result.stdout)