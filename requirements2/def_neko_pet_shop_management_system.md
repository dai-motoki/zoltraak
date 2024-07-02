# React + FastAPI アプリケーションの要件定義書
## ゴール: 猫ショップの猫管理システム

## 1. 目的
本システムは、猫ショップの猫の管理を効率的に行うことを目的としています。
猫の情報を一元管理し、在庫の把握や新規登録、販売管理などの機能を提供します。
これにより、猫ショップの業務の合理化と生産性の向上を図ります。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── CatList.js
│   │   ├── CatDetail.js
│   │   ├── CatForm.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── CatsPage.js
│   │   ├── AddCatPage.js
│   │   └── ...
│   ├── services/
│   │   └── api.js
│   ├── styles/
│   │   └── global.css
│   ├── utils/
│   │   └── helpers.js
│   ├── App.js
│   └── index.js
├── public/
│   ├── index.html
│   └── ...
├── package.json
└── README.md
```

### バックエンド(FastAPI)
```
backend/
├── app/
│   ├── models/
│   │   ├── cat.py
│   │   └── ...
│   ├── schemas/
│   │   ├── cat.py
│   │   └── ...
│   ├── routers/
│   │   ├── cats.py
│   │   └── ...
│   ├── database.py
│   └── main.py
├── tests/
│   ├── test_cats.py
│   └── ...
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

| HTTP メソッド | パス | 説明 |
| --- | --- | --- |
| GET | /cats | 全ての猫の情報を取得 |
| GET | /cats/{cat_id} | 指定した猫の詳細情報を取得 |
| POST | /cats | 新しい猫の情報を登録 |
| PUT | /cats/{cat_id} | 指定した猫の情報を更新 |
| DELETE | /cats/{cat_id} | 指定した猫の情報を削除 |

## 4. データモデル

### Cat
- id: int
- name: str
- breed: str
- age: int
- gender: str
- price: float
- in_stock: bool
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント

| コンポーネント名 | 役割 | props | state |
| --- | --- | --- | --- |
| CatList | 猫の一覧を表示 | cats: Cat[] | - |
| CatDetail | 猫の詳細情報を表示 | cat: Cat | - |
| CatForm | 猫の情報を登録/更新する | cat?: Cat, onSubmit: (cat: Cat) => void | cat: Cat |
| Header | アプリケーションのヘッダーを表示 | - | - |
| Footer | アプリケーションのフッターを表示 | - | - |

## 6. ユーザーインターフェース

### 画面遷移図
```
+----------+     +-------------+     +------------+
| HomePage |     | CatsPage    |     | AddCatPage |
+----------+     +-------------+     +------------+
     |                 |                    |
     v                 v                    v
+----------+     +-------------+     +------------+
| CatDetail |     | CatList     |     | CatForm    |
+----------+     +-------------+     +------------+
```

### ワイヤーフレーム
- [HomePage.png]
- [CatsPage.png]
- [AddCatPage.png]
- [CatDetail.png]
- [CatForm.png]