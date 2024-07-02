# Streamlit 簡易アプリの要件定義書

## ゴール: 猫の1日のデータを分析してグラフにするプロダクトをつくりたい

Streamlitの簡易アプリをローカルに作る

## 1. 目的
猫の1日のデータを収集し、Streamlitを使ってグラフ化する簡易アプリを作成する。

## 2. 環境構築方法
仮想環境を立ち上げる

```
python3 -m venv streamlit_mini
source streamlit_mini/bin/activate
pip install streamlit
```

## 3. 実行方法
アプリを実行する

```
streamlit run app/app.py
```

## 4. ファイル・フォルダ構成

```
.
├── README.md
├── app
    └── app.py
```