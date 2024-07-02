# React + FastAPI アプリケーションの要件定義書
## ゴール: かぞく情報データ分析v65

## 1. 目的
本アプリケーションの目的は、家族情報の管理と分析を行うことです。
ユーザーは家族構成や家族の属性情報を登録・更新し、
それらのデータを分析することで、家族の状況を把握し、
より良い家族運営につなげることができます。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
src/
├── components/
│   ├── FamilyList.js
│   ├── FamilyDetail.js
│   ├── FamilyForm.js
│   └── Navbar.js
├── pages/
│   ├── HomePage.js
│   ├── FamilyPage.js
│   └── AnalysisPage.js
├── services/
│   └── familyApi.js
├── utils/
│   └── formatters.js
├── App.js
└── index.js
```

### バックエンド(FastAPI)
```
app/
├── models/
│   ├── family.py
│   └── user.py
├── routers/
│   ├── family.py
│   └── user.py
├── schemas/
│   ├── family.py
│   └── user.py
├── database.py
├── main.py
└── requirements.txt
```

## 3. APIエンドポイント

### Family API
- `GET /families`: 家族一覧を取得
- `GET /families/{family_id}`: 特定の家族の詳細情報を取得
- `POST /families`: 新しい家族を登録
- `PUT /families/{family_id}`: 家族情報を更新
- `DELETE /families/{family_id}`: 家族情報を削除

### User API
- `POST /users`: 新しいユーザーを登録
- `GET /users/me`: 現在のユーザー情報を取得
- `PUT /users/me`: ユーザー情報を更新

## 4. データモデル

### Family
- id: int
- name: str
- address: str
- members: List[User]
- created_at: datetime
- updated_at: datetime

### User
- id: int
- name: str
- email: str
- password_hash: str
- families: List[Family]
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント

### FamilyList
- 家族一覧を表示
- 各家族の基本情報(名称、住所など)を表示
- 家族の詳細ページへのリンクを提供

### FamilyDetail
- 選択された家族の詳細情報を表示
- 家族メンバーの一覧を表示
- 家族情報の編集機能を提供

### FamilyForm
- 新規家族の登録や、既存家族の情報編集を行う
- 家族情報(名称、住所など)を入力
- 家族メンバーの追加・削除を行う

### Navbar
- アプリケーションのナビゲーションバーを提供
- ホーム、家族一覧、分析ページへのリンクを表示

## 6. ユーザーインターフェース

### 画面遷移図
```
+----------+     +------------+     +------------+
|  ホーム   |---->|  家族一覧  |---->|  家族詳細  |
+----------+     +------------+     +------------+
                        |
                        |
                    +------------+
                    |   分析   |
                    +------------+
```

### ワイヤーフレーム
- ホーム画面: 家族一覧の概要を表示
- 家族一覧画面: 登録されている家族の一覧を表示
- 家族詳細画面: 選択された家族の詳細情報を表示
- 分析画面: 家族データの分析結果を表示