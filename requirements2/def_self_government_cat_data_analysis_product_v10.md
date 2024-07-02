# React + FastAPI アプリケーションの要件定義書
## ゴール: 自治体猫データ分析プロダクトv10

## 1. 目的
本システムは、自治体が保有する猫の情報を一元的に管理し、データ分析を行うことで、自治体の猫対策に役立てることを目的としています。自治体職員や市民が、猫の情報を確認したり、分析結果を閲覧できるWebアプリケーションを提供します。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Footer.js
│   │   ├── CatList.js
│   │   ├── CatDetail.js
│   │   ├── DataAnalysis.js
│   │   └── ...
│   ├── pages/
│   │   ├── Home.js
│   │   ├── CatManagement.js
│   │   ├── Analysis.js
│   │   └── ...
│   ├── utils/
│   │   ├── api.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── App.js
│   └── index.js
├── package.json
└── README.md

### バックエンド(FastAPI)
```
backend/
├── app/
│   ├── models/
│   │   ├── cat.py
│   │   ├── location.py
│   │   └── ...
│   ├── schemas/
│   │   ├── cat.py
│   │   ├── location.py
│   │   └── ...
│   ├── routers/
│   │   ├── cats.py
│   │   ├── locations.py
│   │   └── ...
│   ├── database.py
│   ├── main.py
│   └── ...
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── README.md
├── tests/
│   ├── test_cats.py
│   ├── test_locations.py
│   └── ...
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

### Cats
- GET `/api/cats`: 猫の一覧を取得
- GET `/api/cats/{cat_id}`: 指定した猫の詳細を取得
- POST `/api/cats`: 新しい猫の情報を登録
- PUT `/api/cats/{cat_id}`: 指定した猫の情報を更新
- DELETE `/api/cats/{cat_id}`: 指定した猫の情報を削除

### Locations
- GET `/api/locations`: 場所の一覧を取得
- GET `/api/locations/{location_id}`: 指定した場所の詳細を取得
- POST `/api/locations`: 新しい場所の情報を登録
- PUT `/api/locations/{location_id}`: 指定した場所の情報を更新
- DELETE `/api/locations/{location_id}`: 指定した場所の情報を削除

### 分析
- GET `/api/analysis/cat-count-by-location`: 場所ごとの猫の数を取得
- GET `/api/analysis/cat-age-distribution`: 猫の年齢分布を取得
- GET `/api/analysis/cat-health-status`: 猫の健康状態の割合を取得

## 4. データモデル

### Cat
- id: int
- name: str
- age: int
- sex: str
- color: str
- health_status: str
- location_id: int
- created_at: datetime
- updated_at: datetime

### Location
- id: int
- name: str
- address: str
- latitude: float
- longitude: float
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント

### Header
- 役割: アプリケーションのヘッダーを表示
- props: なし
- state: なし

### CatList
- 役割: 猫の一覧を表示
- props: cats: List[Cat]
- state: searchText: str

### CatDetail
- 役割: 選択した猫の詳細を表示
- props: cat: Cat
- state: なし

### DataAnalysis
- 役割: 猫データの分析結果を表示
- props: analysisData: AnalysisData
- state: activeTab: str

## 6. ユーザーインターフェース

![アプリケーションの画面遷移図](app-flow.png)

### 画面1. ホーム画面
- 猫の一覧を表示
- 検索機能
- 猫の詳細を表示するリンク

### 画面2. 猫管理画面
- 猫の情報を登録/編集/削除できる
- 場所の情報を登録/編集/削除できる

### 画面3. 分析画面
- 場所ごとの猫の数
- 猫の年齢分布
- 猫の健康状態の割合
を表示する