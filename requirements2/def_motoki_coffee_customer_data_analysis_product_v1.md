# React + FastAPI アプリケーションの要件定義書
## ゴール: Motokiコーヒー顧客データ分析プロダクトv1
上記のゴールを満たすReact + FastAPIアプリケーションの要件を記述する

オブジェクト指向の原則に従って、以下の要件を含めて要件定義書を作成する

## 1. 目的
Motokiコーヒーの顧客データを分析し、顧客の嗜好や購買行動を可視化することで、
マーケティング施策の立案や店舗運営の改善につなげる

## 2. ファイル・フォルダ構成
```
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── utils/
│   │   ├── App.js
│   │   └── index.js
│   ├── Dockerfile
│   └── docker-compose.yml
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── crud/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── utils/
│   │   ├── main.py
│   │   └── __init__.py
│   ├── Dockerfile
│   └── docker-compose.yml
├── diagrams/
│   ├── app_architecture.png
│   └── sequence.png
```

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 4. APIエンドポイント
- GET /customers: 顧客一覧を取得
- GET /customers/{customer_id}: 指定した顧客の詳細情報を取得
- POST /customers: 新規顧客を登録
- PUT /customers/{customer_id}: 指定した顧客情報を更新
- DELETE /customers/{customer_id}: 指定した顧客を削除
- GET /sales: 売上データを取得
- GET /sales/trends: 売上推移を取得

## 5. データモデル
### Customer
- id: int
- name: str
- email: str
- phone: str
- purchase_history: List[Sale]

### Sale
- id: int
- customer_id: int
- product_id: int
- quantity: int
- total_amount: float
- purchase_date: datetime

## 6. Reactコンポーネント
### CustomerList
- 顧客一覧を表示
- 検索、ソート、ページネーション機能を持つ

### CustomerDetail
- 選択した顧客の詳細情報を表示
- 顧客情報の編集、削除機能を持つ

### SalesChart
- 売上データを可視化したグラフを表示
- 期間指定、商品別表示などの機能を持つ

## 7. ユーザーインターフェース
![ユーザーインターフェース](diagrams/ui_mockup.png)