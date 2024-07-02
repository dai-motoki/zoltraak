# React + FastAPI アプリケーションの要件定義書
## ゴール: 自治体猫データ分析プロダクトv9

## 1. 目的
このシステムは、自治体が保有する猫の情報を一元的に管理し、データ分析を行うことで、効果的な猫対策を立案するためのツールを提供することを目的としている。自治体職員は本システムを使うことで、地域ごとの猫の個体数、性別、年齢分布などを把握し、適切な猫の引き取りや地域猫活動の支援などの施策を立案できるようになる。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Footer.js
│   │   ├── CatList.js
│   │   ├── CatDetail.js
│   │   ├── DataAnalysis.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── CatsPage.js
│   │   ├── AnalysisPage.js
│   │   └── ...
│   ├── services/
│   │   ├── api.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── utils/
│   │   ├── helpers.js
│   │   └── ...
│   ├── App.js
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
│   └── utils.py
├── tests/
│   ├── test_cats.py
│   ├── test_locations.py
│   └── ...
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

### Cats
- `GET /cats`: 猫の一覧を取得
- `GET /cats/{id}`: 指定したIDの猫の詳細情報を取得
- `POST /cats`: 新しい猫の情報を登録
- `PUT /cats/{id}`: 指定したIDの猫の情報を更新
- `DELETE /cats/{id}`: 指定したIDの猫の情報を削除

### Locations
- `GET /locations`: 地域の一覧を取得
- `GET /locations/{id}`: 指定したIDの地域の詳細情報を取得
- `POST /locations`: 新しい地域の情報を登録
- `PUT /locations/{id}`: 指定したIDの地域の情報を更新
- `DELETE /locations/{id}`: 指定したIDの地域の情報を削除

### Analytics
- `GET /analytics/cats`: 猫の情報に基づいたデータ分析結果を取得
- `GET /analytics/locations`: 地域の情報に基づいたデータ分析結果を取得

## 4. データモデル

### Cat
- id: int
- name: str
- age: int
- gender: str
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
- 役割: アプリケーションのヘッダーを表示する
- props: なし
- state: なし

### CatList
- 役割: 猫の一覧を表示する
- props: cats: List[Cat]
- state: selectedCat: Cat | null

### CatDetail
- 役割: 選択された猫の詳細情報を表示する
- props: cat: Cat
- state: なし

### DataAnalysis
- 役割: 猫と地域のデータ分析結果を表示する
- props: catAnalytics: CatAnalytics, locationAnalytics: LocationAnalytics
- state: なし

## 6. ユーザーインターフェース

### 画面遷移図
```
+----------+
|  HomePage|
+----------+
     |
     v
+----------+
|  CatsPage |
+----------+
     |
     v
+----------+
|CatDetail |
+----------+
     |
     v
+----------+
|AnalysisPage|
+----------+
```

### ワイヤーフレーム
- HomePage
  - アプリケーションの説明
  - 猫の一覧へのリンク
  - データ分析ページへのリンク
- CatsPage
  - 猫の一覧表示
  - 猫の詳細ページへのリンク
  - 新規登録ボタン
- CatDetail
  - 選択された猫の詳細情報の表示
  - 猫の情報編集ボタン
  - 猫の削除ボタン
- AnalysisPage
  - 猫の情報に基づくデータ分析結果の表示
  - 地域の情報に基づくデータ分析結果の表示