# かぼちゃ管理システムの要件定義書

## 1. 目的
このシステムは、かぼちゃの生産者が自社のかぼちゃ在庫を管理し、出荷情報を記録することを目的としています。
生産者は、このシステムを使ってかぼちゃの在庫状況を把握し、出荷計画の立案と実績の記録ができるようになります。

## 2. ファイル・フォルダ構成

### フロントエンド (React)
```
my-app/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── Header.jsx
│   │   ├── Sidebar.jsx
│   │   ├── PumpkinList.jsx
│   │   ├── PumpkinDetail.jsx
│   │   ├── ShipmentForm.jsx
│   │   └── ...
│   ├── pages/
│   │   ├── Dashboard.jsx
│   │   ├── Inventory.jsx
│   │   ├── Shipments.jsx
│   │   └── ...
│   ├── utils/
│   │   ├── api.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── App.jsx
│   └── index.js
├── package.json
└── README.md
```

### バックエンド (FastAPI)
```
backend/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── pumpkins.py
│   │   ├── shipments.py
│   │   └── ...
│   ├── models/
│   │   ├── pumpkin.py
│   │   ├── shipment.py
│   │   └── ...
│   ├── schemas/
│   │   ├── pumpkin.py
│   │   ├── shipment.py
│   │   └── ...
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── ...
│   └── utils/
│       ├── auth.py
│       └── ...
├── tests/
│   ├── test_pumpkins.py
│   ├── test_shipments.py
│   └── ...
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

### 1. かぼちゃ管理
- GET `/pumpkins`: かぼちゃ一覧の取得
- POST `/pumpkins`: かぼちゃの新規登録
- GET `/pumpkins/{id}`: かぼちゃの詳細取得
- PUT `/pumpkins/{id}`: かぼちゃ情報の更新
- DELETE `/pumpkins/{id}`: かぼちゃの削除

### 2. 出荷管理
- GET `/shipments`: 出荷一覧の取得
- POST `/shipments`: 新規出荷の登録
- GET `/shipments/{id}`: 出荷の詳細取得
- PUT `/shipments/{id}`: 出荷情報の更新
- DELETE `/shipments/{id}`: 出荷の削除

## 4. データモデル

### Pumpkin
- id: int
- name: str
- variety: str
- weight: float
- quantity: int
- created_at: datetime
- updated_at: datetime

### Shipment
- id: int
- pumpkin_id: int
- quantity: int
- destination: str
- shipped_at: datetime
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント

### 1. Header
- 役割: アプリケーションのヘッダーを表示
- props: なし
- state: なし

### 2. Sidebar
- 役割: アプリケーションのサイドバーを表示
- props: なし
- state: なし

### 3. PumpkinList
- 役割: かぼちゃの一覧を表示
- props: pumpkins: Pumpkin[]
- state: selectedPumpkin: Pumpkin | null

### 4. PumpkinDetail
- 役割: 選択されたかぼちゃの詳細を表示
- props: pumpkin: Pumpkin
- state: なし

### 5. ShipmentForm
- 役割: 新規出荷の登録フォームを表示
- props: onSubmit: (shipment: Shipment) => void
- state: shipment: Shipment

## 6. ユーザーインターフェース

### 画面遷移図
```
+---------------+
|   Dashboard   |
+---------------+
       |
       v
+---------------+
|   Inventory   |
+---------------+
       |
       v
+---------------+
|   Shipments   |
+---------------+
       |
       v
+---------------+
| PumpkinDetail |
+---------------+
       |
       v
+---------------+
|  ShipmentForm |
+---------------+
```

### ワイヤーフレーム
- Dashboard: かぼちゃの在庫サマリーと直近の出荷情報を表示
- Inventory: かぼちゃの一覧と詳細情報を表示
- Shipments: 出荷の一覧と詳細情報を表示
- PumpkinDetail: 選択したかぼちゃの詳細情報を表示
- ShipmentForm: 新規出荷の登録フォームを表示