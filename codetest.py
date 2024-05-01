code = """
はい、app.pyに対するユニットテストを作成しましょう。ここでは、Python標準のunittestモジュールを使用して、簡単な例を示します。

まず、app.pyというファイルを作成し、以下のようなコードを書きます:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

次に、app_test.pyというファイルを作成し、以下のようなユニットテストを書きます:

```python
import unittest
from app import add, subtract

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 1), -1)

if __name__ == '__main__':
    unittest.main()
```

このテストケースでは、`add`関数と`subtract`関数の動作を確認しています。

`test_add`メソッドでは、`add`関数の結果が期待値と一致することを確認しています。

`test_subtract`メソッドでは、`subtract`関数の結果が期待値と一致することを確認しています。

最後に、`if __name__ == '__main__':`ブロックで`unittest.main()`を呼び出すことで、このテストモジュールを直接実行できるようにしています。

これらのファイルを同じディレクトリに保存し、コマンドラインから以下のように実行すると、テストが実行されます:

```
python app_test.py
```

テストが成功すれば、以下のような出力が得られます:

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

これは、app.pyの`add`関数と`subtract`関数が期待通りに動作していることを示しています。

このように、ユニットテストを書くことで、アプリケーションの個々の部分が正しく動作することを確認できます。これは、ソフトウェア開発の品質を高め、バグを早期に発見するのに役立ちます。
"""

def process_text(text):
    lines = text.split('\n')
    inside_code_block = False
    result = []

    for i, line in enumerate(lines):
        if line.startswith('```'):
            inside_code_block = not inside_code_block
        else:
            if inside_code_block:
                result.append(line)
            else:
                result.append('# ' + line)

    return '\n'.join(result)
def process_text2(text, language=None):
    lines = text.split('\n')
    inside_code_block = False
    result = []

    for i, line in enumerate(lines):
        if line.startswith('```'):
            if not inside_code_block:
                inside_code_block = True
                if language is not None and language.lower() not in line.lower():
                    inside_code_block = False
            else:
                inside_code_block = False
        else:
            if inside_code_block:
                result.append(line)
            else:
                result.append('# ' + line)

    return '\n'.join(result)

aaa = process_text2(code, "python")
print(aaa)