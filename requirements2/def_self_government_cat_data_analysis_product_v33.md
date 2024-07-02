## 1. 目的
自治体が管理する猫の情報を収集・分析し、地域の猫対策に役立てることが本システムの目的です。自治体職員や市民が猫の位置情報、個体識別情報、健康状態などを入力・共有し、データ分析を行うことで、地域の猫の実態を把握し、適切な対応策を検討できるようにします。

## 2. ファイル・フォルダ構成
### フロントエンド (React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Map.js
│   │   ├── CatList.js
│   │   ├── CatDetails.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── MapPage.js
│   │   ├── CatListPage.js
│   │   └── ...
│   ├── utils/
│   ├── styles/
│   ├── App.js
│   └── index.js
├── public/
│   ├── index.html
│   └── ...
├── package.json
└── ...
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
│       ├── cats.py
│       ├── users.py
│       └── ...
├── tests/
│   ├── test_main.py
│   └── ...
├── requirements.txt
└── ...
```

![アプリケーションインターフェイス](diagrams/app_architecture.png)
![シーケンス図](diagrams/sequence.png)

## 3. APIエンドポイント
- `GET /cats`: 猫の一覧を取得
- `POST /cats`: 新しい猫を登録
- `GET /cats/{cat_id}`: 特定の猫の詳細を取得
- `PUT /cats/{cat_id}`: 猫の情報を更新
- `DELETE /cats/{cat_id}`: 猫の情報を削除
- `GET /users`: ユーザーの一覧を取得
- `POST /users`: 新しいユーザーを登録
- `GET /users/{user_id}`: 特定のユーザーの詳細を取得

## 4. データモデル
### Cat
- id: int
- name: str
- age: int
- gender: str
- location: str
- health_status: str
- owner_id: int
- created_at: datetime
- updated_at: datetime

### User
- id: int
- name: str
- email: str
- role: str
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント
### Header
- 機能: アプリのヘッダーを表示
- props: なし
- state: なし

### Map
- 機能: 猫の位置情報を地図上に表示
- props: cats: Cat[]
- state: selectedCat: Cat | null

### CatList
- 機能: 登録された猫の一覧を表示
- props: cats: Cat[]
- state: searchText: string

### CatDetails
- 機能: 選択した猫の詳細情報を表示
- props: cat: Cat
- state: なし

## 6. ユーザーインターフェース
![画面遷移図](diagrams/app_flow.png)

- **ホーム画面**: 猫の一覧を表示し、検索・追加ができる
- **地図画面**: 猫の位置情報を地図上に表示
- **猫詳細画面**: 選択した猫の詳細情報を表示