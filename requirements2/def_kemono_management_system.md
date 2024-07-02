# けもの管理システムの要件定義書

## 1. 目的
本システムは、飼育動物(以下、"けもの")の管理を目的とする。飼育施設の管理者は、本システムを使用してけものの登録、検索、更新、削除を行うことができる。また、飼育状況の記録や、餌やり、病状の管理などの機能を備える。

## 2. ファイル・フォルダ構成

### フロントエンド(React)
```
frontend/
├── src/
│   ├── components/
│   │   ├── AnimalList.js
│   │   ├── AnimalDetail.js
│   │   ├── AnimalForm.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── ManagementPage.js
│   │   └── ...
│   ├── services/
│   │   └── animalService.js
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
│   │   ├── animal.py
│   │   ├── feeding.py
│   │   ├── health.py
│   │   └── ...
│   ├── routers/
│   │   ├── animals.py
│   │   ├── feedings.py
│   │   ├── healths.py
│   │   └── ...
│   ├── schemas/
│   │   ├── animal.py
│   │   ├── feeding.py
│   │   ├── health.py
│   │   └── ...
│   ├── database.py
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── test_animals.py
│   ├── test_feedings.py
│   └── test_healths.py
├── requirements.txt
└── README.md
```

## 3. APIエンドポイント

### Animals
- `GET /animals`: けものの一覧を取得
- `POST /animals`: けものを新規登録
- `GET /animals/{id}`: 指定したidのけものの詳細を取得
- `PUT /animals/{id}`: 指定したidのけものの情報を更新
- `DELETE /animals/{id}`: 指定したidのけものを削除

### Feedings
- `GET /feedings`: けものの餌やり記録の一覧を取得
- `POST /feedings`: けものの餌やり記録を新規登録
- `GET /feedings/{id}`: 指定したidの餌やり記録の詳細を取得
- `PUT /feedings/{id}`: 指定したidの餌やり記録を更新
- `DELETE /feedings/{id}`: 指定したidの餌やり記録を削除

### Healths
- `GET /healths`: けものの健康記録の一覧を取得
- `POST /healths`: けものの健康記録を新規登録
- `GET /healths/{id}`: 指定したidの健康記録の詳細を取得
- `PUT /healths/{id}`: 指定したidの健康記録を更新
- `DELETE /healths/{id}`: 指定したidの健康記録を削除

## 4. データモデル

### Animal
- id: 整数
- name: 文字列
- species: 文字列
- age: 整数
- gender: 文字列
- location: 文字列
- feedings: 1対多の関係でFeedingモデルと紐づく
- healths: 1対多の関係でHealthモデルと紐づく

### Feeding
- id: 整数
- date: 日付
- amount: 浮動小数点数
- note: 文字列
- animal_id: 整数 (Animalモデルとの外部キー)

### Health
- id: 整数
- date: 日付
- symptom: 文字列
- diagnosis: 文字列
- treatment: 文字列
- note: 文字列
- animal_id: 整数 (Animalモデルとの外部キー)

## 5. Reactコンポーネント

### AnimalList
- 役割: けものの一覧を表示する
- props: animals(けものの配列)
- state: なし

### AnimalDetail
- 役割: 選択したけものの詳細情報を表示する
- props: animal(けもののオブジェクト)
- state: なし

### AnimalForm
- 役割: けものの新規登録/更新を行う
- props: animal(けもののオブジェクト), onSubmit(登録/更新時のコールバック)
- state: name, species, age, gender, location

### FeedingList
- 役割: 選択したけものの餌やり記録の一覧を表示する
- props: feedings(餌やり記録の配列), animalId(けもののID)
- state: なし

### FeedingForm
- 役割: 餌やり記録の新規登録/更新を行う
- props: feeding(餌やり記録のオブジェクト), onSubmit(登録/更新時のコールバック), animalId(けもののID)
- state: date, amount, note

### HealthList
- 役割: 選択したけものの健康記録の一覧を表示する
- props: healths(健康記録の配列), animalId(けもののID)
- state: なし

### HealthForm
- 役割: 健康記録の新規登録/更新を行う
- props: health(健康記録のオブジェクト), onSubmit(登録/更新時のコールバック), animalId(けもののID)
- state: date, symptom, diagnosis, treatment, note

## 6. ユーザーインターフェース

### 画面遷移図
![ユーザー画面遷移図](user-flow.png)

### ワイヤーフレーム
- [けものの一覧ページ](wireframe-animal-list.png)
- [けものの詳細ページ](wireframe-animal-detail.png)
- [けものの登録/編集ページ](wireframe-animal-form.png)
- [餌やり記録の一覧ページ](wireframe-feeding-list.png)
- [餌やり記録の登録/編集ページ](wireframe-feeding-form.png)
- [健康記録の一覧ページ](wireframe-health-list.png)
- [健康記録の登録/編集ページ](wireframe-health-form.png)