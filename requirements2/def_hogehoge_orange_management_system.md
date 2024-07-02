# オレンジ管理システムの要件定義書

## 1. 目的
本システムは、オレンジの生産、在庫、出荷の管理を行い、オレンジ農家の業務効率化と収益向上を支援することを目的とする。

## 2. ファイル・フォルダ構成

### フロントエンド (React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Sidebar.js
│   │   ├── OrangeList.js
│   │   ├── OrangeDetail.js
│   │   ├── Inventory.js
│   │   └── Shipment.js
│   ├── pages/
│   │   ├── Dashboard.js
│   │   ├── Oranges.js
│   │   ├── Inventory.js
│   │   └── Shipments.js
│   ├── services/
│   │   └── api.js
│   ├── styles/
│   │   └── global.css
│   ├── utils/
│   └── App.js
├── package.json
└── README.md
```

### バックエンド (FastAPI)
```
backend/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routers/
│       ├── oranges.py
│       ├── inventory.py
│       └── shipments.py
├── tests/
│   ├── test_main.py
│   └── test_routers.py
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

### オレンジ管理
- `GET /oranges`: オレンジ一覧を取得
- `GET /oranges/{id}`: 指定したオレンジの詳細を取得
- `POST /oranges`: 新規オレンジを登録
- `PUT /oranges/{id}`: 指定したオレンジを更新
- `DELETE /oranges/{id}`: 指定したオレンジを削除

### 在庫管理
- `GET /inventory`: 在庫一覧を取得
- `GET /inventory/{id}`: 指定した在庫の詳細を取得
- `POST /inventory`: 新規在庫を登録
- `PUT /inventory/{id}`: 指定した在庫を更新
- `DELETE /inventory/{id}`: 指定した在庫を削除

### 出荷管理
- `GET /shipments`: 出荷一覧を取得
- `GET /shipments/{id}`: 指定した出荷の詳細を取得
- `POST /shipments`: 新規出荷を登録
- `PUT /shipments/{id}`: 指定した出荷を更新
- `DELETE /shipments/{id}`: 指定した出荷を削除

## 4. データモデル

### Orange
- id: int
- name: str
- variety: str
- harvest_date: datetime
- weight: float
- grade: str
- price: float

### Inventory
- id: int
- orange_id: int
- quantity: int
- location: str
- created_at: datetime

### Shipment
- id: int
- orange_id: int
- quantity: int
- destination: str
- shipped_at: datetime

## 5. Reactコンポーネント

### Header
- 役割: アプリケーションのヘッダーを表示
- props: なし
- state: なし

### Sidebar
- 役割: アプリケーションのサイドバーを表示
- props: なし
- state: なし

### OrangeList
- 役割: オレンジの一覧を表示
- props: oranges: Orange[]
- state: selectedOrange: Orange | null

### OrangeDetail
- 役割: 選択したオレンジの詳細を表示
- props: orange: Orange
- state: なし

### Inventory
- 役割: 在庫の一覧を表示
- props: inventory: Inventory[]
- state: selectedInventory: Inventory | null

### Shipment
- 役割: 出荷の一覧を表示
- props: shipments: Shipment[]
- state: selectedShipment: Shipment | null

## 6. ユーザーインターフェース

### 画面遷移図
![ユーザー画面遷移図](user-flow.png)

### ワイヤーフレーム
- [Dashboard](dashboard-wireframe.png)
- [Oranges](oranges-wireframe.png)
- [Inventory](inventory-wireframe.png)
- [Shipments](shipments-wireframe.png)