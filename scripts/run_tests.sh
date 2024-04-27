#!/bin/bash

set -e

# 仮想環境の作成と有効化
python -m venv venv
source venv/bin/activate

# 依存関係のインストール
pip install -r requirements.txt

# マークダウンファイルからPythonファイルを生成し、テストを実行
for md_file in requirements/*.md; do
    py_file="generated/$(basename "${md_file%.md}").py"
    zoltraak"$md_file" "$py_file"
    
    # Pythonファイルの実行
    python "$py_file"
    
    # テストの実行
    test_file="tests/test_$(basename "${md_file%.md}").py"
    if [ -f "$test_file" ]; then
        python -m unittest "$test_file"
    else
        echo "Test file not found: $test_file"
    fi
done

# 仮想環境の非活性化
deactivate