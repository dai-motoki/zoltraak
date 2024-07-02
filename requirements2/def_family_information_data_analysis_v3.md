# React + FastAPI アプリケーションの要件定義書
## ゴール: かぞく情報データ分析v3

## 1. 目的
本アプリケーションの目的は、家族情報の管理と分析を行うことです。
ユーザーは、家族構成や家族の詳細情報を登録・編集できます。
また、登録された情報をもとに、家族の構成や属性などについての分析結果を確認できます。

## 2. ファイル・フォルダ構成

### フロントエンド (React)
```
my-app/
├── src/
│   ├── components/
│   │   ├── FamilyList.js
│   │   ├── FamilyDetail.js
│   │   ├── FamilyForm.js
│   │   ├── AnalysisChart.js
│   │   └── ...
│   ├── pages/
│   │   ├── FamilyPage.js
│   │   ├── AnalysisPage.js
│   │   └── ...
│   ├── services/
│   │   ├── familyApi.js
│   │   └── analysisApi.js
│   ├── utils/
│   │   ├── helpers.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── App.js
│   └── index.js
├── package.json
└── README.md
```

### バックエンド (FastAPI)
```
backend/
├── app/
│   ├── models/
│   │   ├── family.py
│   │   ├── analysis.py
│   │   └── ...
│   ├── schemas/
│   │   ├── family.py
│   │   ├── analysis.py
│   │   └── ...
│   ├── api/
│   │   ├── family.py
│   │   ├── analysis.py
│   │   └── ...
│   ├── database.py
│   ├── main.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

### Family API
- `GET /api/families`: 家族情報の一覧を取得
- `GET /api/families/{id}`: 特定の家族情報を取得
- `POST /api/families`: 新しい家族情報を作成
- `PUT /api/families/{id}`: 特定の家族情報を更新
- `DELETE /api/families/{id}`: 特定の家族情報を削除

### Analysis API
- `GET /api/analysis/family-composition`: 家族構成の分析結果を取得
- `GET /api/analysis/family-attributes`: 家族属性の分析結果を取得

## 4. データモデル

### Family Model
- id: int
- name: str
- members: List[FamilyMember]
- created_at: datetime
- updated_at: datetime

### FamilyMember Model
- id: int
- family_id: int
- name: str
- age: int
- gender: str
- relationship: str

### Analysis Model
- id: int
- family_composition: dict
- family_attributes: dict
- created_at: datetime

## 5. Reactコンポーネント

### FamilyList
- 家族情報の一覧を表示
- 新規作成ボタンを提供

### FamilyDetail
- 特定の家族情報の詳細を表示
- 編集・削除機能を提供

### FamilyForm
- 家族情報の作成・編集フォームを提供

### AnalysisChart
- 家族構成と属性の分析結果をグラフで表示

## 6. ユーザーインターフェース

### 画面遷移図
```
+----------+    +------------+    +------------+
|  Family  |    |  Analysis  |    |   Home     |
|  Page    |    |   Page     |    |   Page     |
+----------+    +------------+    +------------+
     |                |                  |
     |                |                  |
+----------+    +------------+    +------------+
| Family   |    | Analysis   |    |            |
| List     |    | Chart      |    |            |
+----------+    +------------+    +------------+
     |                |                  |
     |                |                  |
+----------+    +------------+    +------------+
| Family   |    |            |    |            |
| Detail   |    |            |    |            |
+----------+    +------------+    +------------+
     |                |                  |
     |                |                  |
+----------+    +------------+    +------------+
| Family   |    |            |    |            |
| Form     |    |            |    |            |
+----------+    +------------+    +------------+
```

### ワイヤーフレーム
各画面のワイヤーフレームは別途添付します。