# React + FastAPI 猫ショップ管理システムの要件定義書

## 1. 目的
このシステムは、猫ショップの猫の在庫管理を行うことを目的とする。ショップ店主は、猫の情報の登録・編集・削除を行い、在庫状況を確認できる。また、顧客は猫の一覧を閲覧し、気に入った猫を予約することができる。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
cat-shop-frontend/
├── src/
│   ├── components/
│   │   ├── CatList.js
│   │   ├── CatDetails.js
│   │   ├── CatForm.js
│   │   └── Header.js
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── CatListPage.js
│   │   └── CatDetailPage.js
│   ├── services/
│   │   └── api.js
│   ├── utils/
│   └── App.js
├── package.json
└── README.md
```

### バックエンド(FastAPI)
```
cat-shop-backend/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── routers/
│       ├── cats.py
│       └── users.py
├── tests/
│   ├── test_main.py
│   └── test_cats.py
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

### Cats
- `GET /cats`: 猫の一覧を取得
- `GET /cats/{cat_id}`: 特定の猫の詳細を取得
- `POST /cats`: 新しい猫を登録
- `PUT /cats/{cat_id}`: 特定の猫の情報を更新
- `DELETE /cats/{cat_id}`: 特定の猫を削除

### Users
- `POST /users`: 新しい顧客を登録
- `POST /users/login`: ログイン
- `GET /users/me`: 自身の情報を取得

## 4. データモデル

### Cat
- id: int
- name: str
- breed: str
- age: int
- gender: str
- price: float
- description: str
- image_url: str
- created_at: datetime
- updated_at: datetime

### User
- id: int
- username: str
- email: str
- hashed_password: str
- is_active: bool
- is_superuser: bool
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント

### CatList
- 猫の一覧を表示する
- 猫の基本情報(名前、品種、性別、価格)を表示
- 個別の猫の詳細ページに遷移できる

### CatDetails
- 選択した猫の詳細情報を表示する
- 猫の画像、説明、年齢などを表示
- 猫の予約ができる

### CatForm
- 新規猫の登録、既存猫の編集ができる
- 猫の情報(名前、品種、性別、価格、説明、画像)を入力できる

### Header
- アプリケーションのヘッダーを表示する
- ログイン/ログアウト、猫の一覧/登録ページへのリンクを持つ

## 6. ユーザーインターフェース

### 画面遷移図
```
+----------+     +-------------+     +-------------+
|  HomePage|     |  CatListPage|     |CatDetailPage|
+----------+     +-------------+     +-------------+
     |                  |                     |
     |                  |                     |
+----------+     +-------------+     +-------------+
|  CatForm |     |   LoginPage |     |   RegisterPage|
+----------+     +-------------+     +-------------+
```

### ワイヤーフレーム
- HomePage
  - 猫ショップの紹介と最新の猫情報を表示
  - 猫一覧ページへのリンク
- CatListPage
  - 猫の一覧を表示
  - 猫の詳細ページへのリンク
  - 新規猫登録ページへのリンク
- CatDetailPage
  - 選択した猫の詳細情報を表示
  - 猫の予約ができる
- CatFormPage
  - 新規猫の登録フォーム
  - 既存猫の編集フォーム
- LoginPage
  - ユーザーのログインフォーム
- RegisterPage
  - 新規ユーザー登録フォーム

[追加の情報]
- 猫ショップの運営者は、猫の情報を管理できる必要がある
- 顧客は、猫の一覧を閲覧し、気に入った猫を予約できる必要がある
- ログイン機能を実装し、ユーザー情報の管理ができる必要がある