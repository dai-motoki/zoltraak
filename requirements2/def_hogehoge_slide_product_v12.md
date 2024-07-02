# 簡易アプリの要件定義書

## ゴール: スライド資料作成プロダクトv12 に関するStreamlitの簡易アプリをローカルに作る
上記のゴールを満たす超最低限のStreamlitアプリケーションの要件を記述する

## 1. 目的
- スライド資料作成プロダクトv12 の簡単な機能を Streamlit で実装する
- ローカル環境で手軽に利用できるアプリを作成する

## 2. 環境構築方法
仮想環境の作成と必要なライブラリのインストールを行う

```
# 仮想環境の作成
python -m venv streamlit_mini
# 仮想環境の有効化
source streamlit_mini/bin/activate
# 必要なライブラリのインストール
pip install streamlit
```

## 3. 実行方法
作成した app.py ファイルを Streamlit で実行する

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