# Streamlit 簡易アプリの要件定義書
## ゴール: スライド資料作成プロダクトv4 に関するStreamlitの簡易アプリをローカルに作る
上記のゴールを満たす超最低限のStreamlitアプリケーションの要件を記述する

## 1. 目的
- スライド資料作成プロダクトv4の機能を簡易的に実装したStreamlitアプリケーションを作成する
- ローカル環境でアプリケーションを動作させることができる

## 2. 環境構築方法
- 仮想環境 `streamlit_mini` を立ち上げる
```
python -m venv streamlit_mini
source streamlit_mini/bin/activate
pip install streamlit
```

## 3. 実行方法
- `app.py` ファイルを実行する
```
streamlit run app.py
```

## 4. ファイル・フォルダ構成
```
.
├── README.md
├── app
    └── app.py
```