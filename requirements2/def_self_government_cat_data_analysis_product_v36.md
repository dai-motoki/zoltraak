## 1. 目的
このシステムの目的は、自治体の飼育猫データを収集・分析し、地域の猫対策に役立てることです。猫の個体数、健康状態、避妊・去勢状況などの情報を可視化し、自治体の施策立案を支援することが目的です。

## 2. ファイル・フォルダ構成
### フロントエンド(React)
```
frontend/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── Header.jsx
│   │   ├── Sidebar.jsx
│   │   ├── CatList.jsx
│   │   ├── CatDetail.jsx
│   │   └── ...
│   ├── pages/
│   │   ├── Dashboard.jsx
│   │   ├── CatManagement.jsx
│   │   ├── Statistics.jsx
│   │   └── ...
│   ├── utils/
│   │   ├── api.js
│   │   ├── helpers.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
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
│   ├── models/
│   │   ├── cat.py
│   │   ├── owner.py
│   │   └── ...
│   ├── routers/
│   │   ├── cats.py
│   │   ├── owners.py
│   │   └── ...
│   ├── schemas/
│   │   ├── cat.py
│   │   ├── owner.py
│   │   └── ...
│   ├── database.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── test_cats.py
│   ├── test_owners.py
│   └── ...
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント
### Cats
- GET /cats: 猫の一覧を取得
- GET /cats/{cat_id}: 特定の猫の詳細情報を取得
- POST /cats: 新しい猫の情報を登録
- PUT /cats/{cat_id}: 猫の情報を更新
- DELETE /cats/{cat_id}: 猫の情報を削除

### Owners
- GET /owners: 飼い主の一覧を取得
- GET /owners/{owner_id}: 特定の飼い主の詳細情報を取得
- POST /owners: 新しい飼い主の情報を登録
- PUT /owners/{owner_id}: 飼い主の情報を更新
- DELETE /owners/{owner_id}: 飼い主の情報を削除

## 4. データモデル
### Cat
- id: 猫のID
- name: 猫の名前
- age: 猫の年齢
- sex: 猫の性別
- breed: 猫の品種
- color: 猫の毛色
- is_neutered: 避妊・去勢の有無
- owner_id: 飼い主のID
- created_at: 登録日時
- updated_at: 更新日時

### Owner
- id: 飼い主のID
- name: 飼い主の名前
- address: 飼い主の住所
- phone: 飼い主の電話番号
- email: 飼い主のメールアドレス
- cats: 飼っている猫のリスト
- created_at: 登録日時
- updated_at: 更新日時

## 5. Reactコンポーネント
### Header
- 画面上部に表示されるヘッダーコンポーネント
- アプリケーションのタイトルと主要なナビゲーションリンクを含む

### Sidebar
- 画面左側に表示されるサイドバーコンポーネント
- 主要な機能へのリンクを含む

### CatList
- 登録されている猫の一覧を表示するコンポーネント
- 猫の基本情報(名前、年齢、性別など)を一覧で表示
- 個々の猫の詳細ページへのリンクを含む

### CatDetail
- 特定の猫の詳細情報を表示するコンポーネント
- 猫の情報(名前、年齢、性別、品種、毛色、避妊・去勢状況など)を表示
- 飼い主の情報も表示

### Dashboard
- アプリケーションのトップページ
- 全体の統計情報(猫の総数、避妊・去勢率、飼い主数など)を表示

### CatManagement
- 猫の登録、編集、削除を行うページ
- CatListとCatDetailコンポーネントを使用

### Statistics
- 猫の情報に基づいた各種統計を表示するページ
- 品種、性別、年齢などの分布グラフを表示

## 6. ユーザーインターフェース
![アプリケーションの画面遷移図](diagrams/app_architecture.png)

![アプリケーションのシーケンス図](diagrams/sequence.png)