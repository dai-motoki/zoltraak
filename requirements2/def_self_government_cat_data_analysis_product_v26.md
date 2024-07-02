# [システム名]の要件定義書
## ゴール: 自治体猫データ分析プロダクトv25

## 1. 目的
本システムは、自治体が保有する猫に関するデータを収集、分析し、
自治体の政策立案や市民サービスの向上に役立てることを目的とする。

## 2. ファイル・フォルダ構成
```
- frontend/
  - index.html
  - app.js
  - components/
    - CatList.vue
    - CatDetails.vue
    - SearchBar.vue
- backend/
  - app.py
  - models.py
  - controllers.py
  - services.py
- tests/
  - test_app.py
  - test_models.py
  - test_controllers.py
  - test_services.py
- assets/
  - images/
    - class.png
    - sequence.png
```

## 3. クラス図
```
+-------------+          +-------------+
|   CatData   |          |   CatInfo   |
+-------------+          +-------------+
| - id: int   |          | - id: int   |
| - name: str |          | - name: str |
| - age: int  |          | - breed: str|
| - breed: str|          | - age: int  |
| - location: str|       | - sex: str  |
+-------------+          +-------------+
       |                        |
       |                        |
+-------------+          +-------------+
|  CatService |          |CatController|
+-------------+          +-------------+
| + getCats() |          |+ listCats() |
| + getCatById()|         |+ getCatDetails()|
| + saveCat() |          |+ searchCats()|
+-------------+          +-------------+
       |                        |
       |                        |
+-------------+          +-------------+
|   CatApp    |          |   CatRepo   |
+-------------+          +-------------+
| - service   |          |+ getAllCats()|
| - controller|          |+ getCatById()|
| - repo      |          |+ saveCat()  |
+-------------+          +-------------+
```

## 4. クラスの詳細
### CatData
- 説明: 自治体が保有する猫の基本情報を表すクラス
- 属性:
  - id: int - 猫のID
  - name: str - 猫の名前
  - age: int - 猫の年齢
  - breed: str - 猫の品種
  - location: str - 猫の居住地
- 操作:
  - なし

### CatInfo
- 説明: 猫の詳細情報を表すクラス
- 属性:
  - id: int - 猫のID
  - name: str - 猫の名前
  - breed: str - 猫の品種
  - age: int - 猫の年齢
  - sex: str - 猫の性別
- 操作:
  - なし

### CatService
- 説明: 猫データに関する業務ロジックを提供するクラス
- 属性:
  - なし
- 操作:
  - getCats(): List[CatData] - 全ての猫データを取得する
  - getCatById(id: int): CatInfo - 指定したIDの猫の詳細情報を取得する
  - saveCat(cat: CatData): None - 猫データを保存する

### CatController
- 説明: ユーザーからの要求を受け取り、適切なサービスを呼び出すクラス
- 属性:
  - なし
- 操作:
  - listCats(): List[CatData] - 全ての猫データの一覧を返す
  - getCatDetails(id: int): CatInfo - 指定したIDの猫の詳細情報を返す
  - searchCats(query: str): List[CatData] - 検索クエリに基づいて猫データを検索する

### CatApp
- 説明: システム全体を統括するクラス
- 属性:
  - service: CatService - 猫データ操作に関するサービス
  - controller: CatController - ユーザーリクエストの受け付けと応答を行うコントローラー
  - repo: CatRepo - 猫データの永続化を担当するリポジトリ
- 操作:
  - なし

### CatRepo
- 説明: 猫データの永続化を担当するクラス
- 属性:
  - なし
- 操作:
  - getAllCats(): List[CatData] - 全ての猫データを取得する
  - getCatById(id: int): CatData - 指定したIDの猫データを取得する
  - saveCat(cat: CatData): None - 猫データを保存する

## 5. ユースケース
1. 猫の一覧表示
   - 関連クラス: CatController, CatService, CatRepo
   - 関連メソッド: listCats(), getCats(), getAllCats()

2. 猫の詳細情報表示
   - 関連クラス: CatController, CatService, CatRepo
   - 関連メソッド: getCatDetails(), getCatById(), getCatById()

3. 猫の検索
   - 関連クラス: CatController, CatService, CatRepo
   - 関連メソッド: searchCats(), getCats(), getAllCats()

4. 猫データの登録
   - 関連クラス: CatController, CatService, CatRepo
   - 関連メソッド: saveCat(), saveCat()

## 6. シーケンス図
### ユースケース1: 猫の一覧表示
```
+----------+------------+------------+------------+
|  Client  | CatController| CatService |  CatRepo   |
+----------+------------+------------+------------+
|          |  listCats() |            |            |
|          |----------->|            |            |
|          |            |  getCats() |            |
|          |            |----------->|            |
|          |            |            | getAllCats()|
|          |            |            |----------->|
|          |            |<-----------|   cats     |
|          |<-----------|   cats     |            |
|   cats   |            |            |            |
+----------+------------+------------+------------+
```

### ユースケース2: 猫の詳細情報表示
```
+----------+------------+------------+------------+
|  Client  | CatController| CatService |  CatRepo   |
+----------+------------+------------+------------+
|          | getCatDetails(id)|        |            |
|          |--------------->|            |            |
|          |                |getCatById(id)|         |
|          |                |------------>|            |
|          |                |            |getCatById(id)|
|          |                |            |------------>|
|          |                |<------------|   catInfo  |
|          |                |   catInfo  |            |
|          |<---------------|            |            |
|   catInfo|                |            |            |
+----------+------------+------------+------------+
```

### ユースケース3: 猫の検索
```
+----------+------------+------------+------------+
|  Client  | CatController| CatService |  CatRepo   |
+----------+------------+------------+------------+
|          |  searchCats(query)|        |            |
|          |----------------->|            |            |
|          |                  |  getCats()|            |
|          |                  |---------->|            |
|          |                  |           |getAllCats()|
|          |                  |           |---------->|
|          |                  |<----------|    cats    |
|          |                  |    cats   |            |
|          |<-----------------|            |            |
|    cats  |                  |            |            |
+----------+------------+------------+------------+
```

### ユースケース4: �猫データの登録
```
+----------+------------+------------+------------+
|  Client  | CatController| CatService |  CatRepo   |
+----------+------------+------------+------------+
|          |   saveCat(cat)   |           |            |
|          |------------------>|           |            |
|          |                  |saveCat(cat)|           |
|          |                  |---------->|saveCat(cat)|
|          |                  |<----------|            |
|          |<------------------|           |            |
+----------+------------+------------+------------+
```