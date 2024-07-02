## 1. 目的
Motokiコーヒー顧客データ分析プロダクトv3は、Motokiコーヒーの顧客データを分析し、経営層に対して有益な洞察を提供することが目的である。
このシステムにより、Motokiコーヒーの売上や顧客動向、好みの傾向などの分析が可能となり、より効果的な経営判断につなげられるようになる。

## 2. ファイル・フォルダ構成
### フロントエンド(React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── Dashboard.js
│   │   ├── CustomerAnalytics.js
│   │   ├── ProductAnalytics.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── AnalyticsPage.js
│   │   └── ...
│   ├── services/
│   │   ├── apiService.js
│   │   └── ...
│   ├── utils/
│   │   ├── helpers.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── App.js
│   └── index.js
├── Dockerfile
└── docker-compose.yml
```

### バックエンド(FastAPI)
```
backend/
├── app/
│   ├── models/
│   │   ├── customer.py
│   │   ├── product.py
│   │   └── ...
│   ├── schemas/
│   │   ├── customer.py
│   │   ├── product.py
│   │   └── ...
│   ├── api/
│   │   ├── v1/
│   │   │   ├── customers.py
│   │   │   ├── products.py
│   │   │   └── ...
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── ...
│   ├── main.py
│   └── __init__.py
├── Dockerfile
└── docker-compose.yml
```

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 4. APIエンドポイント
- `GET /api/v1/customers`: 顧客一覧の取得
- `GET /api/v1/customers/{customer_id}`: 特定の顧客の詳細情報取得
- `POST /api/v1/customers`: 新規顧客の登録
- `PUT /api/v1/customers/{customer_id}`: 顧客情報の更新
- `DELETE /api/v1/customers/{customer_id}`: 顧客の削除
- `GET /api/v1/products`: 商品一覧の取得
- `GET /api/v1/products/{product_id}`: 特定の商品の詳細情報取得
- `POST /api/v1/products`: 新規商品の登録
- `PUT /api/v1/products/{product_id}`: 商品情報の更新
- `DELETE /api/v1/products/{product_id}`: 商品の削除
- `GET /api/v1/analytics/customers`: 顧客分析情報の取得
- `GET /api/v1/analytics/products`: 商品分析情報の取得

## 5. データモデル
### Customer
- id: int
- name: str
- email: str
- phone: str
- address: str
- created_at: datetime
- updated_at: datetime

### Product
- id: int
- name: str
- description: str
- price: float
- category: str
- created_at: datetime
- updated_at: datetime

## 6. Reactコンポーネント
### Dashboard
- 顧客数、売上、注文数などの全体的なKPIを表示
- propsとして、顧客数、売上、注文数などのデータを受け取る

### CustomerAnalytics
- 顧客の属性別(性別、年齢、地域など)の分析データを表示
- propsとして、顧客分析データを受け取る

### ProductAnalytics
- 商品の売れ筋、カテゴリ別の分析データを表示
- propsとして、商品分析データを受け取る

## 6. ユーザーインターフェース
![画面遷移図](diagrams/ui_flow.png)