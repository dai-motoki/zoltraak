## 1. 目的
本アプリケーションの目的は、猫の1日のデータを分析してグラフ化することです。ユーザーが猫の行動データを入力すると、それを可視化するためのシンプルなStreamlitアプリを作成します。

## 2. 環境構築方法

```python
# 仮想環境の作成
python -m venv streamlit_mini
# 仮想環境の有効化
source streamlit_mini/bin/activate
# 必要なライブラリのインストール
pip install streamlit pandas matplotlib
```

## 3. 実行方法

```python
# app.pyの実行
streamlit run app/app.py
```

## 4. ファイル・フォルダ構成

```
.
├── README.md
├── app
    └── app.py
```