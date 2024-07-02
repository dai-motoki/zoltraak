## 1. 目的
自治体が管理する猫の情報を一元的に管理し、データ分析を行うことで、地域猫対策の施策立案や効果検証に役立てることを目的とします。

## 2. ファイル・フォルダ構造
### フロントエンド(React)
```
my-app/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── CatList.js
│   │   ├── CatDetail.js
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
├── package.json
└── README.md
```

### バックエンド(FastAPI)
```
my-api/
├── app/
│   ├── models/
│   │   ├── cat.py
│   │   ├── location.py
│   │   └── ...
│   ├── routers/
│   │   ├── cats.py
│   │   ├── locations.py
│   │   └── ...
│   ├── schemas/
│   │   ├── cat.py
│   │   ├── location.py
│   │   └── ...
│   ├── database.py
│   ├── main.py
│   └── __init__.py
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント
### Cats
- GET /cats: 猫の一覧を取得
- GET /cats/{cat_id}: 猫の詳細情報を取得
- POST /cats: 新しい猫を登録
- PUT /cats/{cat_id}: 猫の情報を更新
- DELETE /cats/{cat_id}: 猫の情報を削除

### Locations
- GET /locations: 場所の一覧を取得
- GET /locations/{location_id}: 場所の詳細情報を取得
- POST /locations: 新しい場所を登録
- PUT /locations/{location_id}: 場所の情報を更新
- DELETE /locations/{location_id}: 場所の情報を削除

## 4. データモデル
### Cat
- id: int
- name: str
- age: int
- sex: str
- color: str
- location_id: int
- location: Location

### Location
- id: int
- name: str
- address: str
- latitude: float
- longitude: float
- cats: List[Cat]

## 5. Reactコンポーネント
### Header
- 役割: アプリケーションのヘッダーを表示
- props: なし
- state: なし

### CatList
- 役割: 猫の一覧を表示
- props: cats: List[Cat]
- state: selectedCat: Cat | null

### CatDetail
- 役割: 選択された猫の詳細情報を表示
- props: cat: Cat
- state: なし

### LocationList
- 役割: 場所の一覧を表示
- props: locations: List[Location]
- state: selectedLocation: Location | null

### LocationDetail
- 役割: 選択された場所の詳細情報を表示
- props: location: Location
- state: なし

## 6. ユーザーインターフェース
![アプリケーション画面遷移図](https://example.com/app-flowchart.png)

![猫一覧画面のワイヤーフレーム](https://example.com/cat-list-wireframe.png)