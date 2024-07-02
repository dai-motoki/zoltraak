# React + FastAPI アプリケーションの要件定義書
## ゴール: かぞく情報データ分析v7

## 1. 目的
このシステムは、家族情報の収集と分析を目的としています。
ユーザーは、家族構成、家族の年齢分布、家族の収入などのデータを入力し、
それらのデータを可視化して分析することができます。
これにより、家族の状況を把握し、適切な支援を行うことが可能になります。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
react-app/
├── src/
│   ├── components/
│   │   ├── FamilyForm.js
│   │   ├── FamilyList.js
│   │   ├── FamilyChart.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── FamilyPage.js
│   │   └── ...
│   ├── utils/
│   │   ├── api.js
│   │   └── ...
│   ├── App.js
│   └── index.js
├── package.json
└── README.md
```

### バックエンド(FastAPI)
```
fastapi-app/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── family.py
│   │   └── ...
│   ├── models/
│   │   ├── family.py
│   │   └── ...
│   ├── schemas/
│   │   ├── family.py
│   │   └── ...
│   └── database.py
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

| HTTPメソッド | パス | 説明 |
| --- | --- | --- |
| GET | /api/families | 登録された家族情報の一覧を取得 |
| POST | /api/families | 新しい家族情報を登録 |
| GET | /api/families/{id} | 指定のIDの家族情報を取得 |
| PUT | /api/families/{id} | 指定のIDの家族情報を更新 |
| DELETE | /api/families/{id} | 指定のIDの家族情報を削除 |

## 4. データモデル

### Family
- id: int
- name: str
- members: List[FamilyMember]
- income: float
- expenses: float

### FamilyMember
- id: int
- family_id: int
- name: str
- age: int
- relationship: str

## 5. Reactコンポーネント

### FamilyForm
- 新規の家族情報を入力するためのフォーム
- propsとして、onSubmit関数を受け取る
- stateとして、family情報を持つ

### FamilyList
- 登録された家族情報の一覧を表示
- propsとして、familyデータを受け取る
- 各家族情報をクリックすると、FamilyPageに遷移する

### FamilyChart
- 家族情報の可視化を行う
- propsとして、familyデータを受け取る
- 年齢分布、収支状況などをグラフ化して表示する

### HomePage
- アプリケーションのトップページ
- FamilyFormとFamilyListを表示する

### FamilyPage
- 個別の家族情報の詳細ページ
- propsとして、familyデータを受け取る
- 家族構成、収支状況などの詳細を表示する

## 6. ユーザーインターフェース

### 画面遷移図
```
+----------+       +----------+       +----------+
|  HomePage|------>|FamilyPage|------>|FamilyForm|
+----------+       +----------+       +----------+
     |
     |
+----------+
|FamilyList|
+----------+
     |
     |
+----------+
|FamilyChart|
+----------+
```

### ワイヤーフレーム
- HomePage
  - 家族情報一覧
  - 新規登録ボタン
- FamilyPage
  - 家族構成
  - 収支状況
  - 編集ボタン
- FamilyForm
  - 家族情報入力フォーム
  - 登録ボタン
- FamilyChart
  - 年齢分布グラフ
  - 収支状況グラフ