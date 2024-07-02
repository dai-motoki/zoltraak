# りんご管理システムの要件定義書

## 1. 目的
本システムは、りんごの在庫管理、受発注、販売管理など、りんご関連の業務をデジタル化し、
効率的な業務運営を実現することを目的とする。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
my-app/
├── src/
│   ├── components/
│   │   ├── AppleList.js
│   │   ├── AppleDetail.js
│   │   ├── OrderForm.js
│   │   ├── SalesReport.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── OrderPage.js
│   │   ├── SalesPage.js
│   │   └── ...
│   ├── services/
│   │   ├── apiClient.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── utils/
│   │   ├── helpers.js
│   │   └── ...
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
│   │   │   ├── endpoints.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   └── __init__.py
│   ├── db/
│   │   ├── base.py
│   │   ├── models.py
│   │   └── __init__.py
│   ├── main.py
│   └── __init__.py
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

| HTTPメソッド | パス                  | 説明                     |
|--------------|----------------------|--------------------------|
| GET          | /api/v1/apples        | りんごの一覧を取得        |
| GET          | /api/v1/apples/{id}   | りんごの詳細を取得        |
| POST         | /api/v1/apples        | りんごを新規作成          |
| PUT          | /api/v1/apples/{id}   | りんごの情報を更新        |
| DELETE       | /api/v1/apples/{id}   | りんごを削除              |
| GET          | /api/v1/orders        | 注文の一覧を取得          |
| POST         | /api/v1/orders        | 注文を新規作成            |
| GET          | /api/v1/sales         | 売上の一覧を取得          |

## 4. データモデル

### Apple
- id: int
- name: str
- description: str
- price: float
- stock: int
- created_at: datetime
- updated_at: datetime

### Order
- id: int
- customer_name: str
- customer_address: str
- items: List[Apple]
- total_amount: float
- status: str
- created_at: datetime
- updated_at: datetime

### SalesReport
- id: int
- apple_id: int
- quantity_sold: int
- total_revenue: float
- created_at: datetime

## 5. Reactコンポーネント

### AppleList
- 役割: りんごの一覧を表示する
- props: apples: List[Apple]
- state: なし

### AppleDetail
- 役割: りんごの詳細を表示する
- props: apple: Apple
- state: なし

### OrderForm
- 役割: 注文フォームを表示する
- props: onSubmit: (order: Order) => void
- state: customer_name: str, customer_address: str, items: List[Apple]

### SalesReport
- 役割: 売上の一覧を表示する
- props: reports: List[SalesReport]
- state: なし

## 6. ユーザーインターフェース

### 画面遷移図
```
+-----------+
|   Home    |
+-----------+
     |
     v
+-----------+
|  りんご一覧  |
+-----------+
     |
     v
+-----------+
|りんご詳細画面|
+-----------+
     |
     v
+-----------+
|   注文画面  |
+-----------+
     |
     v
+-----------+
|   売上画面  |
+-----------+
```

### ワイヤーフレーム
- [Home画面のワイヤーフレーム](home_wireframe.png)
- [りんご一覧画面のワイヤーフレーム](apple_list_wireframe.png)
- [りんご詳細画面のワイヤーフレーム](apple_detail_wireframe.png)
- [注文画面のワイヤーフレーム](order_wireframe.png)
- [売上画面のワイヤーフレーム](sales_wireframe.png)