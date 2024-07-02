# React + FastAPI アプリケーションの要件定義書
## ゴール: かぞく情報データ分析v6

## 1. 目的
本システムは、家族情報の管理と分析を目的としたウェブアプリケーションです。
ユーザーは家族構成、家族の属性、家族関係などのデータを登録・編集できます。
また、登録されたデータを分析し、視覚化された情報を表示することで、
ユーザーの家族情報の理解を深めることができます。

## 2. ファイル・フォルダ構成

### フロントエンド (React)
```
family-data-app/
├── src/
│   ├── components/
│   │   ├── FamilyMemberForm.js
│   │   ├── FamilyTree.js
│   │   ├── Dashboard.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── FamilyPage.js
│   │   ├── AnalysisPage.js
│   │   └── ...
│   ├── services/
│   │   ├── familyService.js
│   │   └── analysisService.js
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── utils/
│   │   ├── helpers.js
│   │   └── ...
│   ├── App.js
│   └── index.js
├── package.json
└── ...
```

### バックエンド (FastAPI)
```
family-data-api/
├── app/
│   ├── models/
│   │   ├── family.py
│   │   ├── member.py
│   │   └── ...
│   ├── routers/
│   │   ├── family.py
│   │   ├── member.py
│   │   └── analysis.py
│   ├── schemas/
│   │   ├── family.py
│   │   ├── member.py
│   │   └── ...
│   ├── services/
│   │   ├── family_service.py
│   │   ├── member_service.py
│   │   └── analysis_service.py
│   ├── utils/
│   │   ├── database.py
│   │   └── ...
│   ├── main.py
│   └── ...
├── requirements.txt
└── ...
```

## 3. APIエンドポイント

### Family API
- `GET /families`: 家族一覧を取得
- `GET /families/{family_id}`: 特定の家族の詳細を取得
- `POST /families`: 新しい家族を登録
- `PUT /families/{family_id}`: 家族情報を更新
- `DELETE /families/{family_id}`: 家族情報を削除

### Member API
- `GET /members`: 家族構成メンバー一覧を取得
- `GET /members/{member_id}`: 特定のメンバーの詳細を取得
- `POST /members`: 新しいメンバーを登録
- `PUT /members/{member_id}`: メンバー情報を更新
- `DELETE /members/{member_id}`: メンバー情報を削除

### Analysis API
- `GET /analysis/family-tree`: 家族関係のツリー構造を取得
- `GET /analysis/demographics`: 家族構成の人口統計情報を取得
- `GET /analysis/relationships`: 家族間の関係性分析結果を取得

## 4. データモデル

### Family Model
- id: int
- name: str
- address: str
- created_at: datetime
- updated_at: datetime
- members: List[Member]

### Member Model
- id: int
- family_id: int
- first_name: str
- last_name: str
- gender: Gender
- birth_date: date
- relationship: Relationship
- created_at: datetime
- updated_at: datetime
- family: Family

## 5. Reactコンポーネント

### FamilyMemberForm
- 家族メンバーの新規登録・編集を行うフォームコンポーネント
- propsとして、family_id、member_data(オプション)を受け取る
- stateとして、フォームの入力値を管理する

### FamilyTree
- 家族関係の階層構造をツリー状に表示するコンポーネント
- propsとして、family_id、family_data(オプション)を受け取る
- stateとして、ツリー構造のデータを管理する

### Dashboard
- 家族情報の概要を表示するダッシュボードコンポーネント
- propsとして、family_data、analysis_data(オプション)を受け取る
- stateとして、表示するグラフやチャートのデータを管理する

## 6. ユーザーインターフェース

### 画面遷移図
![Family Data App Wireframe](family-data-app-wireframe.png)

### ワイヤーフレーム
- HomePage: 家族情報の一覧表示と新規登録
- FamilyPage: 特定の家族の詳細情報と家族構成の表示
- AnalysisPage: 家族情報の分析結果の表示