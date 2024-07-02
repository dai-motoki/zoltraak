## 目的
- Motokiコーヒー顧客データ分析プロダクトv4のStreamlitアプリケーションを作成する
- ユーザーが簡単にデータ分析結果を確認できるようにする

## 環境構築方法
```
# 仮想環境の作成
python -m venv streamlit_mini
# 仮想環境の有効化
source streamlit_mini/bin/activate
# 必要なライブラリのインストール
pip install streamlit pandas matplotlib
```

## 実行方法
```
# アプリケーションの実行
streamlit run app/app.py
```

## ファイル・フォルダ構成
```
.
├── README.md
├── app
    └── app.py
```