## 1. 目的
猫の1日のデータを分析し、グラフとして表示することを目的としたStreamlitアプリケーションを作成する

## 2. 環境構築方法
仮想環境の立ち上げ
```
python -m venv streamlit_mini
source streamlit_mini/bin/activate
```

必要なライブラリのインストール
```
pip install streamlit pandas matplotlib
```

## 3. 実行方法
アプリケーションの起動
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

`app.py`には、Streamlitアプリケーションの詳細な実装を記述する