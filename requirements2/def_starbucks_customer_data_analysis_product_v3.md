## Streamlit 簡易アプリの要件定義書
## ゴール: スタバ顧客分析プロダクトv3 Streamlit の簡易アプリをローカルに作る

## 1. 目的
スタバ顧客分析プロダクトv3上記のゴールを満たすStreamlitアプリケーションの要件定義を記述してください:
    - ペルソナ
        - 30代後半の会社員
        - 週2回以上スタバに通うコーヒー愛好家
        - 新商品やキャンペーンに興味がある
        - データ分析に興味がある
    - ユーザーストーリー
        - 新商品情報を素早く確認したい
        - 自分の利用傾向を可視化して分析したい
        - スタバの顧客動向を把握したい

## 2. ファイル・フォルダ構成
```
├── app.py
├── utils.py
├── templates/
│   ├── header.py
│   ├── sidebar.py
│   └── footer.py
├── data/
│   └── sample_data.csv
└── requirements.txt
```

## 4. Streamlitコンポーネント
- st.title(): アプリケーションのタイトルを表示
- st.sidebar.title(): サイドバーのタイトルを表示
- st.sidebar.selectbox(): サイドバーのドロップダウンメニューを表示
- st.line_chart(): 折れ線グラフを表示
- st.bar_chart(): 棒グラフを表示
- st.dataframe(): データフレームを表示

## 5. データの流れ
1. ユーザーがサイドバーのドロップダウンメニューから選択肢を選ぶ
2. 選択された項目に応じて、utils.pyの関数を呼び出し、データを処理
3. 処理結果をStreamlitコンポーネントを使って画面に表示

## 6. ユーザーインターフェース
![画面遷移図](https://example.com/app_flow.png)
![ワイヤーフレーム](https://example.com/wireframe.png)
ユーザーはサイドバーのドロップダウンメニューから選択肢を選ぶことで、対応するデータ分析結果を表示することができる。

## 7. 開発環境
- Python 3.9
- Streamlit 1.11.0
- Pandas 1.3.5
- Matplotlib 3.5.1
- 仮想環境 venv を使用

## 8. テスト
- ユニットテストでは、各関数の入出力をチェックする
- 主要な機能については、以下のテストケースを用意
    - サイドバーのドロップダウンメニューが正しく表示される
    - 選択した項目に応じて適切なグラフが表示される
    - 表示されるデータフレームの内容が正しい
- サンプルデータ sample_data.csv を使ってテストを行う