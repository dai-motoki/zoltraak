# Streamlit 簡易アプリの要件定義書
## ゴール: 猫の1日のデータを分析してグラフにするプロダクトをつくりたいv5 に関するStreamlitの簡易アプリをローカルに作る
上記のゴールを満たす超最低限のStreamlitアプリケーションの要件を記述する

## 1. 目的
- 猫の1日のデータを分析し、グラフ化する
- Streamlitを使ったローカルアプリケーションを作成する

## 2. 環境構築方法
```
# 仮想環境の作成
python3 -m venv env
source env/bin/activate

# パッケージのインストール
pip install streamlit
```

## 3. 実行方法
```
# アプリの起動
streamlit run app/app.py
```

## 4. ファイル・フォルダ構成

**以下のみ**
.
├── README.md
├── app
    └── app.py（これは詳細に記載）