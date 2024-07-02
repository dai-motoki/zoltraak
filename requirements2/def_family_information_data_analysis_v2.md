# React + FastAPI アプリケーションの要件定義書
## ゴール: かぞく情報データ分析v2

## 1. 目的
本システムの目的は、家族情報の管理と分析を行うことです。
ユーザーは家族構成や家族の属性情報を登録・編集でき、
それらのデータを視覚的に分析することができます。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
frontend/
├── components/
│   ├── FamilyForm.js
│   ├── FamilyList.js
│   ├── FamilyChart.js
│   └── ...
├── pages/
│   ├── HomePage.js
│   ├── FamilyPage.js
│   └── ...
├── utils/
│   ├── api.js
│   └── ...
├── App.js
└── index.js
```

### バックエンド(FastAPI)
```
backend/
├── api/
│   ├── routers/
│   │   ├── family.py
│   │   └── ...
│   └── __init__.py
├── models/
│   ├── family.py
│   └── ...
├── database.py
├── main.py
└── requirements.txt
```

## 3. APIエンドポイント

| HTTPメソッド | パス | 説明 |
| --- | --- | --- |
| GET | /api/families | 家族情報の一覧を取得 |
| POST | /api/families | 新しい家族情報を登録 |
| GET | /api/families/{id} | 指定したIDの家族情報を取得 |
| PUT | /api/families/{id} | 指定したIDの家族情報を更新 |
| DELETE | /api/families/{id} | 指定したIDの家族情報を削除 |

## 4. データモデル

### Family
- id: int
- name: str
- relationship: str
- age: int
- gender: str
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント

- `FamilyForm`: 家族情報の登録・編集フォーム
  - props: onSubmit, initialValues
  - state: formData
- `FamilyList`: 家族情報の一覧表示
  - props: families
  - state: なし
- `FamilyChart`: 家族情報のグラフ表示
  - props: families
  - state: chartData

## 6. ユーザーインターフェース

### 画面遷移図
```
+----------+
|  Home    |
|  Page    |
+----------+
     |
     v
+----------+
|  Family  |
|  Page    |
+----------+
     |
     +-- Family Form
     +-- Family List
     +-- Family Chart
```

### ワイヤーフレーム
- Home Page
  - 家族情報の一覧表示
  - 新規登録ボタン
- Family Page
  - 家族情報の登録・編集フォーム
  - 家族情報の一覧表示
  - 家族情報のグラフ表示