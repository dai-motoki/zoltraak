## 1. 目的
このシステムは、自治体の飼い猫データを収集・分析し、地域の猫の現状を可視化することを目的としています。地域の猫の健康状態や飼育状況を把握し、適切な対策を立てることで、猫の福祉向上と地域の共生を目指します。

## 2. ファイル・フォルダ構成
### フロントエンド(React)
```
frontend/
├── package.json
├── src/
│   ├── components/
│   │   ├── CatList.js
│   │   ├── CatDetail.js
│   │   ├── Header.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── CatListPage.js
│   │   ├── CatDetailPage.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── utils/
│   │   ├── api.js
│   │   └── ...
│   ├── App.js
│   └── index.js
├── Dockerfile
└── docker-compose.yml
```

### バックエンド(FastAPI)
```
backend/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routers/
│       ├── cats.py
│       └── ...
├── tests/
│   ├── test_main.py
│   └── ...
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 4. APIエンドポイント
- `GET /cats`: 猫の一覧を取得
- `GET /cats/{cat_id}`: 指定した猫の詳細を取得
- `POST /cats`: 新しい猫を登録
- `PUT /cats/{cat_id}`: 指定した猫の情報を更新
- `DELETE /cats/{cat_id}`: 指定した猫を削除

## 5. データモデル
### Cat
- id: int
- name: str
- age: int
- breed: str
- sex: str
- neutered: bool
- health_status: str
- location: str
- owner_id: int
- created_at: datetime
- updated_at: datetime

### Owner
- id: int
- name: str
- email: str
- phone: str
- address: str
- cats: List[Cat]

## 6. Reactコンポーネント
### CatList
- 猫の一覧を表示
- propsとして猫のデータを受け取る
- stateとして表示順序や表示件数などを管理

### CatDetail
- 猫の詳細情報を表示
- propsとして選択された猫のデータを受け取る

### Header
- アプリケーションのヘッダーを表示
- ナビゲーションリンクを含む

## 7. ユーザーインターフェース
![ユーザーインターフェース](diagrams/ui_wireframe.png)