## ゴール: スライド資料作成プロダクトv18 Streamlit の簡易アプリをローカルに作る

## 1. 目的
スライド資料作成プロダクトv18上記のゴールを満たすStreamlitアプリケーションの要件定義を記述する:
    - ペルソナ
        - 研究職の人
        - 発表資料作成に時間がかかる
        - Powerpoint操作に不慣れ
    - ユーザーストーリー
        - 研究者は、手軽にスライド資料を作成したい
        - 入力したデータからスライドを自動生成したい
        - 簡単な操作でスライドをカスタマイズしたい

## 2. ファイル・フォルダ構成
    - Markdown形式で省略なしのファイル・フォルダ構成:
        ├── app.py
        ├── utils.py
        ├── templates/
        │   ├── header.py
        │   ├── sidebar.py
        │   └── footer.py
        ├── data/
        │   └── sample_data.csv
        └── requirements.txt

## 4. Streamlitコンポーネント
    - st.title(): アプリケーションのタイトル
    - st.sidebar.file_uploader(): CSVファイルのアップロード
    - st.dataframe(): アップロードしたCSVデータの表示
    - st.button(): スライド自動生成ボタン
    - st.download_button(): 生成したスライドのダウンロード

## 5. データの流れ
    - ユーザーがCSVファイルをアップロード
    - CSVデータを読み込み、Streamlitのデータフレームで表示
    - ユーザーが「スライド生成」ボタンをクリック
    - 入力データからスライドを自動生成
    - 生成したスライドをダウンロードリンクで提供

## 6. ユーザーインターフェース
    - 画面遷移図
        - ホーム画面 -> スライド生成画面
    - ホーム画面のワイヤーフレーム
        - タイトル
        - サイドバーにCSVアップロード
        - データプレビュー
        - スライド生成ボタン
    - スライド生成画面のワイヤーフレーム
        - 生成したスライドのプレビュー
        - ダウンロードボタン

## 7. 開発環境
    - Python 3.9
    - Streamlit
    - pandas
    - venv仮想環境を構築

## 8. テスト
    - ユニットテスト
        - CSVデータの正常な読み込み
        - スライド生成の正常動作
        - ダウンロード機能の確認
    - テストデータ
        - sample_data.csv