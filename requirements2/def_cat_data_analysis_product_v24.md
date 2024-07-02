# 簡易Streamlitアプリの要件定義書

## ゴール
猫の1日のデータを分析してグラフにするプロダクトをつくりたい

## 1. 目的
- 猫の1日のデータを可視化し、飼い主がより良いケアができるようにする

## 2. 環境構築方法
仮想環境の立ち上げ:
```
python3 -m venv streamlit_mini
source streamlit_mini/bin/activate
```
必要なライブラリのインストール:
```
pip install streamlit
```

## 3. 実行方法
アプリの起動:
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