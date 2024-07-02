# めがね管理システム 要件定義書

## 1. 目的
本システムは、ユーザーがめがねの管理を容易に行えるようにするためのWebアプリケーションである。ユーザーは自身のめがねの情報を登録・編集・削除できるほか、めがねの在庫管理や貸出管理を行うことができる。

## 2. ファイル・フォルダ構成

### フロントエンド (React)
```
my-app/
├── public/
│   ├── index.html
│   └── ...
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── GlassesTable.js
│   │   ├── GlassesForm.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── GlassesPage.js
│   │   ├── LendingPage.js
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
├── .gitignore
├── package.json
└── README.md
```

### バックエンド (FastAPI)
```
backend/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── glasses.py
│   │   │   ├── lending.py
│   │   │   └── ...
│   │   └── __init__.py
│   ├── crud/
│   │   ├── glasses.py
│   │   ├── lending.py
│   │   └── ...
│   ├── db/
│   │   ├── base.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── main.py
│   └── __init__.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 3. APIエンドポイント

| HTTPメソッド | パス | 説明 |
| --- | --- | --- |
| GET | /api/v1/glasses | 登録されためがねの一覧を取得 |
| POST | /api/v1/glasses | 新しいめがねを登録 |
| GET | /api/v1/glasses/{id} | 指定したIDのめがねの詳細を取得 |
| PUT | /api/v1/glasses/{id} | 指定したIDのめがねの情報を更新 |
| DELETE | /api/v1/glasses/{id} | 指定したIDのめがねを削除 |
| GET | /api/v1/lending | 貸出記録の一覧を取得 |
| POST | /api/v1/lending | 新しい貸出記録を登録 |
| GET | /api/v1/lending/{id} | 指定したIDの貸出記録の詳細を取得 |
| PUT | /api/v1/lending/{id} | 指定したIDの貸出記録の情報を更新 |
| DELETE | /api/v1/lending/{id} | 指定したIDの貸出記録を削除 |

## 4. データモデル

### Glassesモデル
- id: int (主キー)
- name: str (めがねの名称)
- brand: str (ブランド)
- frame_color: str (フレームの色)
- lens_color: str (レンズの色)
- purchase_date: datetime (購入日)
- price: float (価格)
- is_available: bool (貸出可能かどうか)

### Lendingモデル
- id: int (主キー)
- glasses_id: int (外部キー: Glassesモデル)
- user_name: str (借りた人の名前)
- lend_date: datetime (貸出日)
- return_date: datetime (返却日)

## 5. Reactコンポーネント

### Header
- 役割: アプリケーションのヘッダーを表示
- props: なし
- state: なし

### GlassesTable
- 役割: 登録されためがねの一覧を表示
- props: glasses: 登録されためがねのリスト
- state: なし

### GlassesForm
- 役割: めがねの登録・編集フォームを表示
- props: 
  - glasses: 編集対象のめがねの情報 (新規登録時は空)
  - onSubmit: フォーム送信時のコールバック関数
- state:
  - formData: フォームの入力値

### LendingTable
- 役割: 貸出記録の一覧を表示
- props: lendings: 貸出記録のリスト
- state: なし  

### LendingForm
- 役割: 貸出記録の登録・編集フォームを表示
- props:
  - lending: 編集対象の貸出記録 (新規登録時は空)
  - onSubmit: フォーム送信時のコールバック関数
- state:
  - formData: フォームの入力値

## 6. ユーザーインターフェース

### 画面遷移図
```
+------------+
|    Home    |
+------------+
       |
       v
+------------+
|   Glasses  |
+------------+
       |
       v
+------------+
|   Lending  |
+------------+
```

### ワイヤーフレーム
1. ホーム画面
   - アプリケーションの概要を表示
   - めがねの登録と貸出管理へのリンク

2. めがね一覧画面
   - 登録されためがねの一覧を表示
   - 新規登録、編集、削除の機能

3. 貸出管理画面
   - 貸出記録の一覧を表示
   - 新規貸出、返却の機能