# React + FastAPI アプリケーションの要件定義書
## ゴール: 猫ショップの猫管理システム
本システムは、猫ショップの猫の情報を管理するためのシステムです。ショップ店主は、猫の登録、編集、削除、検索などの機能を利用できます。

## 1. 目的
本システムは、猫ショップの猫の情報を一元的に管理し、効率的な在庫管理と販売管理を実現することを目的とします。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
cat-shop-frontend/
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
│   ├── utils/
│   └── App.js
├── package.json
└── ...
```

### バックエンド(FastAPI)
```
cat-shop-backend/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── cats.py
│   │   └── ...
│   ├── models.py
│   ├── schemas.py
│   └── database.py
├── requirements.txt
└── ...
```

## 3. APIエンドポイント

### Cats API
- `GET /cats`: 猫の一覧を取得
- `GET /cats/{cat_id}`: 指定した猫の詳細を取得
- `POST /cats`: 新しい猫を登録
- `PUT /cats/{cat_id}`: 指定した猫の情報を更新
- `DELETE /cats/{cat_id}`: 指定した猫を削除

## 4. データモデル

### Cat
- `id`: 猫のID (primary key)
- `name`: 猫の名前
- `breed`: 品種
- `age`: 年齢
- `color`: 毛色
- `price`: 価格
- `is_available`: 販売可能かどうかのフラグ
- `created_at`: 登録日時
- `updated_at`: 更新日時

## 5. Reactコンポーネント

### CatList
- 猫の一覧を表示
- 各猫の情報(名前、品種、年齢、色、価格、販売可能フラグ)を表示
- 猫の詳細ページへのリンクを提供

### CatDetail
- 指定した猫の詳細情報を表示
- 猫の情報を編集できるフォームを提供

### CatForm
- 新規猫登録、または既存の猫情報を編集するためのフォーム
- 必要な入力項目(名前、品種、年齢、色、価格、販売可能フラグ)を含む

## 6. ユーザーインターフェース

### 画面遷移図
```
+----------+    +------------+    +------------+
|  HomePage|    |   CatsPage  |    |  AddCatPage|
+----------+    +------------+    +------------+
     |                |                   |
     |                |                   |
+----------+    +------------+    +------------+
| CatDetail |    |   CatForm  |    |            |
+----------+    +------------+    +------------+
```

### ワイヤーフレーム
- [猫一覧ページのワイヤーフレーム](wireframe-cat-list.png)
- [猫詳細ページのワイヤーフレーム](wireframe-cat-detail.png)
- [猫登録/編集ページのワイヤーフレーム](wireframe-cat-form.png)