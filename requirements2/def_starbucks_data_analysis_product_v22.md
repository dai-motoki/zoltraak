# Streamlit 簡易アプリの要件定義書
## ゴール: スタバデータ分析プロダクトv22 Streamlit の超最低限の簡易アプリをローカルに作る
Streamlit 
上記のゴールを満たす超最低限のStreamlitアプリケーションの要件を記述する

## 1. 目的
Streamlitを使用して、ローカル環境で超最低限のWebアプリケーションを開発する。
アプリケーションの目的は、ユーザーがデータを入力し、それに基づいた結果を表示することである。

## 2. 環境構築方法
- Anacondaなどのパッケージマネージャを使用して、Pythonとstreamlit環境を構築する
- `pip install streamlit`コマンドでstreamlitをインストールする

## 3. 実行方法
- ターミナルから`streamlit run app/app.py`コマンドを実行する

## 4. ファイル・フォルダ構成
```
.
├── README.md
├── app
    └── app.py
```