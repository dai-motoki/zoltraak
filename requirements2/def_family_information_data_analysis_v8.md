# React + FastAPI アプリケーションの要件定義書
## ゴール: かぞく情報データ分析v8

## 1. 目的
本システムは、家族情報の管理と分析を行うことを目的としている。
ユーザーは家族メンバーの情報を登録・編集し、家族構成の可視化や分析レポートの生成などの機能を利用できる。

## 2. ファイル・フォルダ構成

### フロントエンド (React)
```
my-app/
├── src/
│   ├── components/
│   │   ├── FamilyMember.js
│   │   ├── FamilyTree.js
│   │   ├── ReportGenerator.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── FamilyPage.js
│   │   ├── ReportsPage.js
│   │   └── ...
│   ├── services/
│   │   └── api.js
│   ├── styles/
│   │   └── global.css
│   ├── utils/
│   │   └── helpers.js
│   ├── App.js
│   └── index.js
├── package.json
└── README.md
```

### バックエンド (FastAPI)
```
backend/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── family_members.py
│   │   │   ├── reports.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── models/
│   │   ├── family_member.py
│   │   ├── report.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── family_member.py
│   │   ├── report.py
│   │   └── __init__.py
│   ├── main.py
│   └── __init__.py
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

### 家族メンバー管理
- `GET /api/v1/family-members`: 家族メンバーの一覧を取得
- `POST /api/v1/family-members`: 新しい家族メンバーを作成
- `GET /api/v1/family-members/{id}`: 特定の家族メンバーの詳細を取得
- `PUT /api/v1/family-members/{id}`: 家族メンバーの情報を更新
- `DELETE /api/v1/family-members/{id}`: 家族メンバーを削除

### レポート管理
- `GET /api/v1/reports`: 生成されたレポートの一覧を取得
- `POST /api/v1/reports`: 新しいレポートを生成
- `GET /api/v1/reports/{id}`: 特定のレポートの詳細を取得
- `DELETE /api/v1/reports/{id}`: レポートを削除

## 4. データモデル

### FamilyMember
- id: int
- first_name: str
- last_name: str
- date_of_birth: date
- gender: str
- relationship: str
- parent_id: int (nullable)

### Report
- id: int
- title: str
- description: str
- created_at: datetime
- updated_at: datetime
- family_tree_image: str (base64-encoded)
- analysis_data: json

## 5. Reactコンポーネント

### FamilyMember
- 役割: 個別の家族メンバーの情報を表示・編集する
- props: familyMember (FamilyMember型)
- state: なし

### FamilyTree
- 役割: 家族構成をツリー状に表示する
- props: familyMembers (FamilyMember型の配列)
- state: selectedMember (FamilyMember型)

### ReportGenerator
- 役割: レポートの生成と表示を行う
- props: なし
- state: reportData (Report型)

## 6. ユーザーインターフェース

### 画面遷移図
```
+----------+     +----------+     +----------+
|  HomePage|---->|FamilyPage|---->|ReportsPage|
+----------+     +----------+     +----------+
```

### ワイヤーフレーム
- HomePage
  - 家族メンバーの一覧
  - 新規メンバー登録ボタン
- FamilyPage
  - 家族構成のツリー表示
  - 個別メンバーの詳細表示・編集
- ReportsPage
  - 生成済みレポートの一覧
  - 新規レポート生成ボタン
  - レポートの詳細表示