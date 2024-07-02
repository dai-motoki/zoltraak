## 1. 目的
このシステムの目的は、wework顧客データを分析し、ビジネスインサイトを得ることです。React + FastAPIを使用したWebアプリケーションを開発し、ユーザーが顧客データを視覚化、分析できる機能を提供することが目的です。

## 2. ファイル・フォルダ構成
```
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── utils/
│   │   ├── App.js
│   │   ├── index.js
│   ├── Dockerfile
│   ├── package.json
│   └── docker-compose.yml
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── database.py
│   │   ├── main.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── docker-compose.yml
├── diagrams/
│   ├── app_architecture.png
│   ├── sequence.png
└── docker-compose.yml
```

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 4. APIエンドポイント
- GET /api/customers: 顧客データの一覧を取得
- GET /api/customers/{customer_id}: 指定した顧客IDの詳細情報を取得
- POST /api/customers: 新規顧客データを登録
- PUT /api/customers/{customer_id}: 顧客データを更新
- DELETE /api/customers/{customer_id}: 顧客データを削除
- GET /api/insights: 顧客データの分析結果を取得

## 5. データモデル
### Customer
- id: int
- name: str
- email: str
- company: str
- created_at: datetime
- updated_at: datetime

### Insight
- id: int
- title: str
- description: str
- data: json
- created_at: datetime

## 6. Reactコンポーネント
- App: メインのレイアウトコンポーネント
- CustomerList: 顧客データの一覧を表示
- CustomerDetail: 顧客の詳細情報を表示
- CustomerForm: 顧客データの登録/更新フォーム
- InsightList: 分析結果の一覧を表示
- InsightDetail: 分析結果の詳細情報を表示

## 7. ユーザーインターフェース
![ユーザーインターフェース](diagrams/ui_mockup.png)