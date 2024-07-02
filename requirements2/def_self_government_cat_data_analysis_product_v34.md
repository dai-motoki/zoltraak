## 1. 目的
本システムは、自治体の猫の情報を集約・分析し、猫の適正飼育を推進することを目的としている。自治体の職員や猫の飼い主、獣医師などが利用し、猫の健康状態や飼育状況の把握、適正な飼育方法の提案などを行う。

## 2. ファイル・フォルダ構成
### フロントエンド(React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── CatList.js
│   │   ├── CatDetails.js
│   │   ├── CreateCatForm.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── CatListPage.js
│   │   ├── CatDetailsPage.js
│   │   └── ...
│   ├── utils/
│   │   ├── api.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── App.js
│   └── index.js
├── public/
│   ├── index.html
│   └── ...
├── package.json
└── ...
```

### バックエンド(FastAPI)
```
backend/
├── app/
│   ├── models/
│   │   ├── cat.py
│   │   ├── owner.py
│   │   └── ...
│   ├── schemas/
│   │   ├── cat.py
│   │   ├── owner.py
│   │   └── ...
│   ├── routers/
│   │   ├── cats.py
│   │   ├── owners.py
│   │   └── ...
│   ├── database.py
│   ├── main.py
│   └── ...
├── tests/
│   ├── test_cats.py
│   ├── test_owners.py
│   └── ...
├── requirements.txt
└── ...
```

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 3. APIエンドポイント
- `GET /cats`: 登録されている猫の一覧を取得
- `GET /cats/{cat_id}`: 指定したIDの猫の詳細情報を取得
- `POST /cats`: 新しい猫の情報を登録
- `PUT /cats/{cat_id}`: 指定したIDの猫の情報を更新
- `DELETE /cats/{cat_id}`: 指定したIDの猫の情報を削除
- `GET /owners`: 登録されている飼い主の一覧を取得
- `GET /owners/{owner_id}`: 指定したIDの飼い主の詳細情報を取得
- `POST /owners`: 新しい飼い主の情報を登録
- `PUT /owners/{owner_id}`: 指定したIDの飼い主の情報を更新
- `DELETE /owners/{owner_id}`: 指定したIDの飼い主の情報を削除

## 4. データモデル
### Cat
- id: int
- name: str
- age: int
- breed: str
- sex: str
- health_status: str
- owner_id: int
- created_at: datetime
- updated_at: datetime

### Owner
- id: int
- name: str
- address: str
- phone: str
- email: str
- cats: List[Cat]
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント
### CatList
- 役割: 登録されている猫の一覧を表示する
- props: cats: List[Cat]
- state: searchQuery: str

### CatDetails
- 役割: 指定した猫の詳細情報を表示する
- props: cat: Cat
- state: -

### CreateCatForm
- 役割: 新しい猫の情報を登録する
- props: onSubmit: function
- state: name: str, age: int, breed: str, sex: str, health_status: str, owner_id: int

## 6. ユーザーインターフェース
![ユーザーインターフェース](diagrams/wireframe.png)