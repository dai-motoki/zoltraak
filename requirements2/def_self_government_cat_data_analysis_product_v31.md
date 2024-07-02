## 1. 目的
自治体の管理する猫の情報を一元的に管理し、データ分析を行うことで、地域の猫の現状を把握し、適切な対策を立てることを目的とする。猫の健康状態、飼育状況、地域分布などのデータを収集・分析し、自治体の政策立案や地域住民への情報提供に活用する。

## 2. ファイル・フォルダ構成
### フロントエンド(React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── CatList.js
│   │   ├── CatDetail.js
│   │   ├── DataAnalysis.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── CatsPage.js
│   │   ├── AnalysisPage.js
│   │   └── ...
│   ├── utils/
│   ├── styles/
│   ├── App.js
│   └── index.js
├── public/
├── package.json
└── README.md
```

### バックエンド(FastAPI)
```
backend/
├── app/
│   ├── models/
│   │   ├── cat.py
│   │   ├── owner.py
│   │   └── ...
│   ├── schemas/
│   │   ├── cat.py
│   │   ├── owner.py
│   │   └── ...
│   ├── api/
│   │   ├── v1/
│   │   │   ├── cats.py
│   │   │   ├── owners.py
│   │   │   └── ...
│   │   └── __init__.py
│   ├── db.py
│   ├── main.py
│   └── utils.py
├── tests/
├── requirements.txt
└── README.md
```

![アプリケーションインターフェイス](diagrams/app_architecture.png)
![シーケンス図](diagrams/sequence.png)

## 3. APIエンドポイント
### Cats API
- GET /api/v1/cats: 猫の一覧を取得
- GET /api/v1/cats/{cat_id}: 猫の詳細情報を取得
- POST /api/v1/cats: 新規猫を登録
- PUT /api/v1/cats/{cat_id}: 猫の情報を更新
- DELETE /api/v1/cats/{cat_id}: 猫の情報を削除

### Owners API
- GET /api/v1/owners: 飼い主の一覧を取得
- GET /api/v1/owners/{owner_id}: 飼い主の詳細情報を取得
- POST /api/v1/owners: 新規飼い主を登録
- PUT /api/v1/owners/{owner_id}: 飼い主の情報を更新
- DELETE /api/v1/owners/{owner_id}: 飼い主の情報を削除

## 4. データモデル
### Cat
- id: int
- name: str
- age: int
- breed: str
- sex: str
- health_status: str
- location: str
- owner_id: int
- created_at: datetime
- updated_at: datetime

### Owner
- id: int
- name: str
- address: str
- phone: str
- email: str
- cats: List[Cat]
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント
### ホーム画面
- `HomePage`: アプリの概要と機能を紹介するトップページ

### 猫管理
- `CatList`: 猫の一覧を表示
- `CatDetail`: 猫の詳細情報を表示
- `CatForm`: 猫の登録/編集フォーム

### 飼い主管理
- `OwnerList`: 飼い主の一覧を表示
- `OwnerDetail`: 飼い主の詳細情報を表示
- `OwnerForm`: 飼い主の登録/編集フォーム

### データ分析
- `DataAnalysis`: 猫の分布、健康状態、飼育状況などのデータ分析結果を表示

## 6. ユーザーインターフェース
![アプリケーションの画面遷移図](diagrams/app_flow.png)

ホーム画面からは、猫の一覧、飼い主の一覧、データ分析結果の各ページに遷移できる。
猫や飼い主の詳細情報ページでは、編集や削除の機能を提供する。
データ分析ページでは、グラフや表を使って猫の状況を視覚的に表現する。