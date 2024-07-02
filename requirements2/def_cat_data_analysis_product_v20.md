# Streamlit 簡易アプリの要件定義書

## ゴール: 猫の1日のデータを分析してグラフにするプロダクトをつくりたい

上記のゴールを満たす超最低限のStreamlitアプリケーションの要件を記述する

## 1. 目的
- 猫の1日のデータを分析し、グラフ化することで、猫の1日の行動パターンを可視化する

## 2. 環境構築方法
```
# 仮想環境の作成
python -m venv streamlit_mini
# 仮想環境の有効化
source streamlit_mini/bin/activate
# Streamlitのインストール
pip install streamlit
```

## 3. 実行方法
```
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