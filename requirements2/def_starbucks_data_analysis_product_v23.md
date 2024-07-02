# 要件定義書

## ゴール
Streamlit の超最低限の簡易アプリをローカルに作る

## 1. 目的
Streamlit を使用して、ローカル環境で超最低限の Web アプリケーションを開発する
アプリケーションの目的は、ユーザーがデータを入力し、それに基づいた結果を表示すること

## 2. 環境構築方法
- Anaconda などのパッケージマネージャを使用して、Python と streamlit 環境を構築する
- `pip install streamlit` コマンドで streamlit をインストールする

## 3. 実行方法
- ターミナルから `streamlit run app/app.py` コマンドを実行する

## 4. ファイル・フォルダ構成
```
.
├── README.md
├── app
    └── app.py
```