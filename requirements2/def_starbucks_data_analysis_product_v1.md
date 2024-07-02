## 1. 目的
このシステムの目的は、スターバックスのデータを分析し、店舗の運営や戦略立案に役立つ洞察を提供することです。React + FastAPIを使用したウェブアプリケーションを開発し、ユーザーが店舗データを視覚化し、分析できるようにします。

## 2. ファイル・フォルダ構成
### フロントエンド(React)
```
frontend/
├── public/
│   ├── index.html
│   └── static/
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Sidebar.js
│   │   ├── Dashboard.js
│   │   ├── StoreList.js
│   │   └── StoreDetail.js
│   ├── pages/
│   │   ├── Home.js
│   │   └── Analyze.js
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

### バックエンド(FastAPI)
```
backend/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── stores.py
│   │   │   │   └── analytics.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── base.py
│   │   ├── models.py
│   │   └── session.py
│   ├── schemas/
│   │   ├── store.py
│   │   └── analytics.py
│   ├── services/
│   │   ├── store_service.py
│   │   └── analytics_service.py
│   ├── main.py
│   └── __init__.py
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── README
├── requirements.txt
└── README.md
```

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 4. APIエンドポイント
- GET /api/v1/stores: 店舗一覧を取得
- GET /api/v1/stores/{store_id}: 店舗の詳細情報を取得
- POST /api/v1/stores: 新しい店舗を登録
- GET /api/v1/analytics/sales: 売上データの分析結果を取得
- GET /api/v1/analytics/customer_count: 来店客数の分析結果を取得

## 5. データモデル
### Store
- id: int
- name: str
- address: str
- latitude: float
- longitude: float
- sales_data: List[SalesData]
- customer_data: List[CustomerData]

### SalesData
- id: int
- store_id: int
- date: datetime
- revenue: float

### CustomerData
- id: int
- store_id: int
- date: datetime
- customer_count: int

## 6. Reactコンポーネント
### Header
- 画面上部に表示されるヘッダーコンポーネント
- アプリケーションのタイトルと、ナビゲーションメニューを含む

### Sidebar
- 画面左側に表示されるサイドバーコンポーネント
- 店舗一覧、分析機能へのリンクを含む

### Dashboard
- 店舗の売上や来店客数などの分析結果を表示するダッシュボードコンポーネント
- グラフやチャートを使用して視覚化する

### StoreList
- 店舗一覧を表示するコンポーネント
- 店舗の基本情報を一覧で表示する

### StoreDetail
- 個別の店舗の詳細情報を表示するコンポーネント
- 売上推移、来店客数の推移などを表示する

## 7. ユーザーインターフェース
![ユーザーインターフェース](diagrams/ui_mockup.png)