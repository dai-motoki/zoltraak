# 簡易アプリの要件定義書

## ゴール: 顧客分析プロダクトv1 に関するStreamlitの簡易アプリをローカルに作る
上記のゴールを満たす超最低限のStreamlitアプリケーションの要件を記述する。

## 1. 目的
- 顧客分析プロダクトv1 の機能を最小限に実装したStreamlitアプリを作成する
- ユーザーが簡単に使えるインターフェイスを提供する
- 開発者が手軽にアプリを修正・拡張できるようにする

## 2. 環境構築方法
仮想環境の立ち上げ:
```
python -m venv streamlit_mini
source streamlit_mini/bin/activate
```

パッケージのインストール:
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