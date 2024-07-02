# React + FastAPI アプリケーションの要件定義書
## ゴール: かぞく情報データ分析v4

## 1. 目的
本アプリケーションは、家族情報を管理し、データ分析を行うことを目的としています。
ユーザーは家族情報を登録・編集できるほか、家族構成の変化や年代別の人数変化などの分析を行うことができます。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
src/
├── components/
│   ├── FamilyForm.js
│   ├── FamilyList.js
│   ├── FamilyChart.js
│   └── ...
├── pages/
│   ├── FamilyPage.js
│   ├── AnalysisPage.js
│   └── ...
├── services/
│   ├── familyService.js
│   └── analysisService.js
├── utils/
│   ├── formatters.js
│   └── validators.js
├── App.js
├── index.js
└── ...
```

### バックエンド(FastAPI)
```
app/
├── api/
│   ├── routes/
│   │   ├── family.py
│   │   ├── analysis.py
│   │   └── ...
│   └── __init__.py
├── models/
│   ├── family.py
│   └── ...
├── schemas/
│   ├── family.py
│   └── ...
├── database.py
├── main.py
└── ...
```

## 3. APIエンドポイント

### Family API
- `GET /api/families`: 家族情報一覧を取得
- `POST /api/families`: 新しい家族情報を登録
- `GET /api/families/{id}`: 指定した家族情報を取得
- `PUT /api/families/{id}`: 家族情報を更新
- `DELETE /api/families/{id}`: 家族情報を削除

### Analysis API
- `GET /api/analysis/family-composition`: 家族構成の変化を取得
- `GET /api/analysis/age-distribution`: 年代別の人数変化を取得

## 4. データモデル

### Family
- id: int
- name: str
- relation: str
- age: int
- gender: str
- user_id: int

### User
- id: int
- username: str
- email: str
- password: str

## 5. Reactコンポーネント

### FamilyForm
- 家族情報の登録・編集を行うフォームコンポーネント
- propsとして家族情報を受け取り、stateで管理する

### FamilyList
- 家族情報の一覧を表示するコンポーネント
- propsとして家族情報の配列を受け取る

### FamilyChart
- 家族構成の変化や年代別の人数変化を表示するチャートコンポーネント
- propsとして分析結果のデータを受け取る

### AnalysisPage
- 分析結果を表示するページコンポーネント
- FamilyChartコンポーネントを含む

### FamilyPage
- 家族情報の管理を行うページコンポーネント
- FamilyFormコンポーネントとFamilyListコンポーネントを含む

## 6. ユーザーインターフェース

### 画面遷移図
![画面遷移図](https://example.com/wireframe.png)

### ワイヤーフレーム
- [FamilyPage](https://example.com/family-page-wireframe.png)
- [AnalysisPage](https://example.com/analysis-page-wireframe.png)