# React + FastAPI アプリケーションの要件定義書
## ゴール: 猫ショップの猫管理システム

## 1. 目的
本システムは、猫ショップの運営者が猫の在庫管理、販売管理、顧客管理を効率的に行えるようにするためのものである。
猫の情報の登録、編集、削除、検索、購入履歴の確認などの機能を提供する。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── CatList.js
│   │   ├── CatDetails.js
│   │   ├── CustomerList.js
│   │   ├── CustomerDetails.js
│   │   ├── SalesHistory.js
│   │   └── ...
│   ├── pages/
│   │   ├── CatManagement.js
│   │   ├── CustomerManagement.js
│   │   ├── SalesHistory.js
│   │   └── ...
│   ├── utils/
│   │   ├── api.js
│   │   └── ...
│   ├── App.js
│   ├── index.js
│   └── ...
├── package.json
└── ...

### バックエンド(FastAPI)
backend/
├── app/
│   ├── models/
│   │   ├── cat.py
│   │   ├── customer.py
│   │   ├── sales.py
│   │   └── ...
│   ├── routers/
│   │   ├── cats.py
│   │   ├── customers.py
│   │   ├── sales.py
│   │   └── ...
│   ├── schemas/
│   │   ├── cat.py
│   │   ├── customer.py
│   │   ├── sales.py
│   │   └── ...
│   ├── database.py
│   ├── main.py
│   └── ...
├── requirements.txt
└── ...
```

## 3. APIエンドポイント

### Cats
- `GET /cats`: 猫の一覧を取得
- `GET /cats/{cat_id}`: 指定した猫の詳細を取得
- `POST /cats`: 新しい猫を登録
- `PUT /cats/{cat_id}`: 指定した猫の情報を更新
- `DELETE /cats/{cat_id}`: 指定した猫を削除

### Customers
- `GET /customers`: 顧客の一覧を取得
- `GET /customers/{customer_id}`: 指定した顧客の詳細を取得
- `POST /customers`: 新しい顧客を登録
- `PUT /customers/{customer_id}`: 指定した顧客の情報を更新
- `DELETE /customers/{customer_id}`: 指定した顧客を削除

### Sales
- `GET /sales`: 売上履歴の一覧を取得
- `GET /sales/{sale_id}`: 指定した売上の詳細を取得
- `POST /sales`: 新しい売上を記録
- `PUT /sales/{sale_id}`: 指定した売上の情報を更新
- `DELETE /sales/{sale_id}`: 指定した売上を削除

## 4. データモデル

### Cat
- id: 猫のID
- name: 猫の名前
- breed: 猫の品種
- age: 猫の年齢
- gender: 猫の性別
- price: 猫の価格
- description: 猫の説明
- image: 猫の画像

### Customer
- id: 顧客のID
- name: 顧客の名前
- email: 顧客のメールアドレス
- phone: 顧客の電話番号
- address: 顧客の住所

### Sale
- id: 売上のID
- cat_id: 売れた猫のID
- customer_id: 購入した顧客のID
- sale_date: 売上日
- price: 売上金額

## 5. Reactコンポーネント

### CatList
- 猫の一覧を表示
- 猫の検索、並び替え、ページネーションなどの機能を提供
- 各猫の詳細ページへのリンクを提供

### CatDetails
- 選択された猫の詳細情報を表示
- 猫の情報の編集、削除機能を提供

### CustomerList
- 顧客の一覧を表示
- 顧客の検索、並び替え、ページネーションなどの機能を提供
- 各顧客の詳細ページへのリンクを提供

### CustomerDetails
- 選択された顧客の詳細情報を表示
- 顧客の情報の編集、削除機能を提供

### SalesHistory
- 売上履歴の一覧を表示
- 売上の検索、並び替え、ページネーションなどの機能を提供
- 各売上の詳細ページへのリンクを提供

## 6. ユーザーインターフェース

### 画面遷移図
![Screen Transition Diagram](screen_transition_diagram.png)

### ワイヤーフレーム
- [CatList ワイヤーフレーム](cat_list_wireframe.png)
- [CatDetails ワイヤーフレーム](cat_details_wireframe.png)
- [CustomerList ワイヤーフレーム](customer_list_wireframe.png)
- [CustomerDetails ワイヤーフレーム](customer_details_wireframe.png)
- [SalesHistory ワイヤーフレーム](sales_history_wireframe.png)