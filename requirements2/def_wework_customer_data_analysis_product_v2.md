## 1. 目的
本システムは、wework顧客データを分析し、企業の意思決定を支援するためのWebアプリケーションである。顧客データの可視化、分析レポートの作成、予測分析などの機能を提供し、企業の成長戦略立案に活用できるようにする。

## 2. ファイル・フォルダ構成
```
wework-customer-analytics/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── utils/
│   │   ├── App.js
│   │   └── index.js
│   ├── tests/
│   ├── Dockerfile
│   └── docker-compose.yml
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── crud/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── main.py
│   │   └── __init__.py
│   ├── tests/
│   ├── Dockerfile
│   └── docker-compose.yml
├── diagrams/
│   ├── app_architecture.png
│   └── sequence.png
├── .gitignore
└── README.md
```

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 4. APIエンドポイント
- GET /api/customers: 顧客一覧を取得
- GET /api/customers/{customer_id}: 指定した顧客の詳細情報を取得
- POST /api/customers: 新規顧客を登録
- PUT /api/customers/{customer_id}: 顧客情報を更新
- DELETE /api/customers/{customer_id}: 顧客を削除
- GET /api/reports: 分析レポートの一覧を取得
- POST /api/reports: 新規分析レポートを作成
- GET /api/predictions: 予測分析の結果を取得

## 5. データモデル
```python
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    company = Column(String)
    industry = Column(String)
    employee_count = Column(Integer)
    revenue = Column(Float)
    created_at = Column(DateTime)

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", backref="reports")
    created_at = Column(DateTime)
```

## 6. Reactコンポーネント
- `CustomerList`: 顧客一覧を表示
- `CustomerDetail`: 顧客の詳細情報を表示
- `CustomerForm`: 顧客の新規登録/更新フォーム
- `ReportList`: 分析レポートの一覧を表示
- `ReportDetail`: 分析レポートの詳細を表示
- `ReportForm`: 分析レポートの作成/編集フォーム
- `PredictionResult`: 予測分析の結果を表示

## 7. ユーザーインターフェース
![ユーザーインターフェース](diagrams/ui_mockup.png)