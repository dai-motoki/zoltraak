# さるショップの管理システム 要件定義書

## 1. 目的
本システムは、さるショップの商品管理、注文管理、顧客管理を行うためのWebアプリケーションです。
ショップ運営者は、商品の追加・編集・削除、注文の確認・出荷、顧客情報の管理を行うことができます。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
さるショップ/
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Footer.js
│   │   ├── ProductList.js
│   │   ├── ProductDetail.js
│   │   ├── OrderList.js
│   │   ├── OrderDetail.js
│   │   ├── CustomerList.js
│   │   └── CustomerDetail.js
│   ├── pages/
│   │   ├── Home.js
│   │   ├── Products.js
│   │   ├── Orders.js
│   │   └── Customers.js
│   ├── utils/
│   │   └── api.js
│   ├── App.js
│   └── index.js
├── package.json
└── README.md
```

### バックエンド(FastAPI)
```
さるショップ/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

| HTTPメソッド | パス | 説明 |
| --- | --- | --- |
| GET | /products | 商品一覧の取得 |
| GET | /products/{product_id} | 商品詳細の取得 |
| POST | /products | 新規商品の登録 |
| PUT | /products/{product_id} | 商品情報の更新 |
| DELETE | /products/{product_id} | 商品の削除 |
| GET | /orders | 注文一覧の取得 |
| GET | /orders/{order_id} | 注文詳細の取得 |
| POST | /orders | 新規注文の登録 |
| PUT | /orders/{order_id} | 注文情報の更新 |
| DELETE | /orders/{order_id} | 注文の削除 |
| GET | /customers | 顧客一覧の取得 |
| GET | /customers/{customer_id} | 顧客詳細の取得 |
| POST | /customers | 新規顧客の登録 |
| PUT | /customers/{customer_id} | 顧客情報の更新 |
| DELETE | /customers/{customer_id} | 顧客の削除 |

## 4. データモデル

### Product
- id: int
- name: str
- description: str
- price: float
- stock: int
- created_at: datetime
- updated_at: datetime

### Order
- id: int
- customer_id: int
- product_id: int
- quantity: int
- total_price: float
- status: str
- created_at: datetime
- updated_at: datetime

### Customer
- id: int
- name: str
- email: str
- phone: str
- address: str
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント

### Header
- 役割: ヘッダーの表示
- props: なし
- state: なし

### Footer
- 役割: フッターの表示
- props: なし
- state: なし

### ProductList
- 役割: 商品一覧の表示
- props: products: Product[]
- state: searchQuery: str

### ProductDetail
- 役割: 商品詳細の表示
- props: product: Product
- state: なし

### OrderList
- 役割: 注文一覧の表示
- props: orders: Order[]
- state: searchQuery: str

### OrderDetail
- 役割: 注文詳細の表示
- props: order: Order
- state: なし

### CustomerList
- 役割: 顧客一覧の表示
- props: customers: Customer[]
- state: searchQuery: str

### CustomerDetail
- 役割: 顧客詳細の表示
- props: customer: Customer
- state: なし

## 6. ユーザーインターフェース

![さるショップ管理システムの画面遷移図](さるショップ管理システムの画面遷移図.png)

![さるショップ管理システムのホーム画面ワイヤーフレーム](さるショップ管理システムのホーム画面ワイヤーフレーム.png)