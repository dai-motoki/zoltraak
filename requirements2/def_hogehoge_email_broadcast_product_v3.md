# 簡易アプリの要件定義書
## ゴール: 塾生メール一斉送信プロダクトv3 に関するStreamlitの簡易アプリをローカルに作る
上記のゴールを満たす超最低限のStreamlitアプリケーションの要件を記述する

## 1. 目的
- 塾生メール一斉送信プロダクトv3 の基本機能を簡易的に実装したStreamlitアプリケーションを作成する
- ローカル環境でアプリを起動し、動作確認ができるようにする

## 2. 環境構築方法
```
# 仮想環境の作成
python -m venv streamlit_mini

# 仮想環境の有効化
source streamlit_mini/bin/activate

# 必要なライブラリのインストール
pip install streamlit
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