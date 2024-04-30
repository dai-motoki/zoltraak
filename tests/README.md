
![](https://raw.githubusercontent.com/Sunwood-ai-labs/zoltraak/celsius/assets/images/test_icon.jpeg)

# テスト方法

このプロジェクトでは、以下の2つの方法でテストを実行することができます。



## 1. `python`コマンドを使用したテスト

`python`コマンドを使用して、テストファイルを直接実行する方法です。

```bash
python tests/test_cli.py
```

この方法では、`if __name__ == '__main__':`ブロック内のコードが実行され、指定したテストクラスやテストメソッドが実行されます。テストの実行をカスタマイズしたい場合や、特定のテストクラスやテストメソッドだけを実行したい場合に適しています。

ただし、この方法を使用する場合は、`if __name__ == '__main__':`ブロック内のコードを適切に設定する必要があります。

## 2. `pytest`コマンドを使用したテスト

`pytest`コマンドを使用して、テストを実行する方法です。`pytest`は、テストの自動検出と実行を行うためのテストフレームワークです。

### テストクラスを指定してテストを実行

```bash
pytest tests/test_cli.py::TestzoltraakCommand
```

この方法では、`TestzoltraakCommand`クラス内のすべてのテストメソッドが実行されます。

### テストメソッドを指定してテストを実行

```bash
pytest tests/test_cli.py::TestzoltraakCommand::test_missing_md_file_argument
pytest tests/test_cli.py::TestzoltraakCommand::test_prompt_argument
pytest tests/test_cli.py::TestzoltraakCommand::test_text_input
```

この方法では、指定したテストメソッドだけが実行されます。複数のテストメソッドを指定することもできます。

`pytest`コマンドを使用する場合、テストファイル内の`if __name__ == '__main__':`ブロックは実行されません。`pytest`が自動的にテストを検出し、実行します。

## テストの実行方法の選択

プロジェクトの要件やテストの目的に応じて、適切なテストの実行方法を選択してください。

- カスタマイズされたテストの実行が必要な場合や、特定のテストクラスやテストメソッドだけを実行したい場合は、`python`コマンドを使用したテストが適しています。
- テストの自動検出と実行を行いたい場合や、テストの実行を簡単にしたい場合は、`pytest`コマンドを使用したテストが適しています。