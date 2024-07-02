# React + FastAPI アプリケーションの要件定義書
## ゴール: チョコレート管理システム
本システムは、チョコレートの在庫管理と販売管理を行うアプリケーションです。店舗の従業員が、チョコレートの情報を登録・更新・削除し、在庫状況を確認できるようにします。また、顧客は自身の注文履歴を確認できるようにします。

## 1. 目的
本システムの目的は以下の通りです。

- チョコレートの在庫管理を効率的に行う
- チョコレートの販売管理を行う
- 顧客の注文履歴を管理する

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── ChocolateList.jsx
│   │   ├── ChocolateDetail.jsx
│   │   ├── OrderHistory.jsx
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.jsx
│   │   ├── ChocolatePage.jsx
│   │   ├── OrderPage.jsx
│   │   └── ...
│   ├── services/
│   │   ├── chocolateAPI.js
│   │   ├── orderAPI.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── utils/
│   │   ├── formatDate.js
│   │   └── ...
│   ├── App.jsx
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
│   │   │   ├── chocolate.py
│   │   │   ├── order.py
│   │   │   └── ...
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── ...
│   ├── models/
│   │   ├── chocolate.py
│   │   ├── order.py
│   │   └── ...
│   ├── schemas/
│   │   ├── chocolate.py
│   │   ├── order.py
│   │   └── ...
│   ├── main.py
│   └── __init__.py
├── tests/
│   ├── api/
│   │   ├── test_chocolate.py
│   │   ├── test_order.py
│   │   └── ...
│   └── conftest.py
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

### Chocolateエンドポイント
- `GET /api/v1/chocolates`: チョコレートの一覧を取得
- `GET /api/v1/chocolates/{id}`: 指定したIDのチョコレートの詳細を取得
- `POST /api/v1/chocolates`: 新しいチョコレートを登録
- `PUT /api/v1/chocolates/{id}`: 指定したIDのチョコレートを更新
- `DELETE /api/v1/chocolates/{id}`: 指定したIDのチョコレートを削除

### Orderエンドポイント
- `GET /api/v1/orders`: 注文の一覧を取得
- `GET /api/v1/orders/{id}`: 指定したIDの注文の詳細を取得
- `POST /api/v1/orders`: 新しい注文を作成
- `PUT /api/v1/orders/{id}`: 指定したIDの注文を更新
- `DELETE /api/v1/orders/{id}`: 指定したIDの注文を削除

## 4. データモデル

### Chocolate
- id: int
- name: str
- description: str
- price: float
- stock: int
- created_at: datetime
- updated_at: datetime

### Order
- id: int
- user_id: int
- chocolate_id: int
- quantity: int
- total_price: float
- status: str
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント

### ChocolateList
- 役割: チョコレートの一覧を表示する
- props: chocolates: Chocolate[]
- state: なし

### ChocolateDetail
- 役割: 選択したチョコレートの詳細を表示する
- props: chocolate: Chocolate
- state: なし

### OrderHistory
- 役割: 注文履歴を表示する
- props: orders: Order[]
- state: なし

### OrderForm
- 役割: 新規注文を作成する
- props: chocolates: Chocolate[]
- state: selectedChocolate: Chocolate, quantity: number

## 6. ユーザーインターフェース

### 画面遷移図
```
+----------+
|   Home   |
+----------+
     |
     v
+----------+
| Chocolate|
+----------+
     |
     v
+----------+
|  Details |
+----------+
     |
     v
+----------+
|   Order  |
+----------+
     |
     v
+----------+
| Order    |
| History  |
+----------+
```

### ワイヤーフレーム
- Home画面
  - チョコレートの一覧を表示
  - 詳細ボタンで ChocolateDetail 画面に遷移
  - 注文ボタンで OrderForm 画面に遷移
- ChocolateDetail 画面
  - 選択したチョコレートの詳細を表示
  - 注文ボタンで OrderForm 画面に遷移
- OrderForm 画面
  - 注文フォームを表示
  - 注文確定ボタンで Order 画面に遷移
- Order 画面
  - 注文の詳細を表示
- OrderHistory 画面
  - 注文履歴を一覧で表示