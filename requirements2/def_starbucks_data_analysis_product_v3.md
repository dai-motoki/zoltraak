## 1. 目的
本システムの目的は、スタバの店舗データを分析し、店舗運営やマーケティングに役立つ洞察を提供することです。ユーザーは店舗の売上、顧客動向、商品ラインナップなどを可視化・分析することができ、経営改善につなげることができます。

## 2. ファイル・フォルダ構成
```
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── store/
│   │   ├── styles/
│   │   ├── utils/
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   ├── package.json
│   └── docker/
│       └── Dockerfile
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── crud/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── main.py
│   │   └── __init__.py
│   ├── tests/
│   ├── requirements.txt
│   └── docker/
│       └── Dockerfile
├── diagrams/
│   ├── app_architecture.png
│   └── sequence.png
├── docker-compose.yml
└── README.md
```

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 4. APIエンドポイント
- `GET /stores`: 全店舗の情報を取得
- `GET /stores/{store_id}`: 指定した店舗の詳細情報を取得
- `POST /stores`: 新しい店舗情報を登録
- `PUT /stores/{store_id}`: 指定した店舗情報を更新
- `DELETE /stores/{store_id}`: 指定した店舗情報を削除
- `GET /sales`: 全店舗の売上データを取得
- `GET /sales/{store_id}`: 指定した店舗の売上データを取得
- `GET /customers`: 全顧客の情報を取得
- `GET /customers/{customer_id}`: 指定した顧客の詳細情報を取得

## 5. データモデル
```python
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    sales = relationship("Sale", back_populates="store")

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"))
    date = Column(DateTime, index=True)
    revenue = Column(Float)
    customers = Column(Integer)
    store = relationship("Store", back_populates="sales")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    purchases = relationship("Sale", backref="customer")
```

## 6. Reactコンポーネント
- `StoreList`: 全店舗のリストを表示
- `StoreDetail`: 個別の店舗の詳細情報を表示
- `SalesChart`: 店舗の売上データをグラフで表示
- `CustomerList`: 全顧客のリストを表示
- `CustomerDetail`: 個別の顧客の詳細情報を表示
- `Navbar`: アプリケーションのナビゲーションバー

## 7. ユーザーインターフェース
![画面遷移図](diagrams/app_flow.png)