# 簡易Streamlitアプリの要件定義書

## ゴール
Motokiコーヒー顧客データ分析プロダクトv5 に関するStreamlitの簡易アプリをローカルに作る

上記のゴールを満たす超最低限のStreamlitアプリケーションの要件を記述する

## 1. 目的
- Motokiコーヒーの顧客データを可視化し、基本的な分析を行うこと
- Streamlitを使ったシンプルなアプリケーションの開発経験を得ること

## 2. 環境構築方法
```
# 仮想環境の作成
python -m venv streamlit_mini
# 仮想環境の有効化
source streamlit_mini/bin/activate
# 必要なライブラリのインストール
pip install streamlit pandas matplotlib
```

## 3. 実行方法
```
# アプリの起動
streamlit run app/app.py
```

## 4. ファイル・フォルダ構成
```
.
├── README.md
├── app
    └── app.py
```