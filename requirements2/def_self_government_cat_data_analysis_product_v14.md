# [システム名]の要件定義書
## ゴール: 自治体猫データ分析プロダクトv14

## 1. 目的
本システムは、自治体が保有する猫の情報を収集・分析し、地域猫対策に役立てることを目的としている。
収集した猫の情報を可視化・分析することで、地域の猫の実態を把握し、適切な対策を立てることができる。

## 2. ファイル・フォルダ構成
```
- frontend/
    - components/
        - CatCard.vue
        - CatList.vue
        - Header.vue
    - pages/
        - CatListPage.vue
        - CatDetailPage.vue
        - DashboardPage.vue
    - router.js
    - App.vue
    - main.js
- backend/
    - controllers/
        - CatController.js
        - UserController.js
    - models/
        - Cat.js
        - User.js
    - routes/
        - cat.js
        - user.js
    - app.js
- tests/
    - unit/
        - CatController.spec.js
        - CatModel.spec.js
    - e2e/
        - cat-list.spec.js
        - cat-detail.spec.js
- assets/
    - images/
        - cat1.png
        - cat2.png
        - cat3.png
- README.md
```

## 3. クラス図
```
+---------------+        +---------------+
|     Cat       |        |     User      |
+---------------+        +---------------+
| - id: string  |        | - id: string  |
| - name: string|        | - name: string|
| - age: number |        | - email: string|
| - breed: string|        +---------------+
| - location: string|     ^
| - image: string|        |
+---------------+        |
       ^                 |
       |                 |
+---------------+        |
|CatController  |        |
+---------------+        |
| + getAll(): Cat[]|      |
| + getById(id: string): Cat|
| + create(cat: Cat): Cat|
| + update(id: string, cat: Cat): Cat|
| + delete(id: string): void|
+---------------+        |
       ^                 |
       |                 |
+---------------+        |
|UserController |        |
+---------------+        |
| + getAll(): User[]|     |
| + getById(id: string): User|
| + create(user: User): User|
| + update(id: string, user: User): User|
| + delete(id: string): void|
+---------------+
```

## 4. クラスの詳細
### Cat
- 説明: 猫の情報を表すクラス
- 属性:
    - id: string - 猫のID
    - name: string - 猫の名前
    - age: number - 猫の年齢
    - breed: string - 猫の品種
    - location: string - 猫の所在地
    - image: string - 猫の画像ファイルパス
- 操作:
    - なし

### User
- 説明: ユーザー情報を表すクラス
- 属性:
    - id: string - ユーザーのID
    - name: string - ユーザー名
    - email: string - ユーザーのメールアドレス
- 操作:
    - なし

### CatController
- 説明: 猫の情報を管理するコントローラークラス
- 属性:
    - なし
- 操作:
    - getAll(): Cat[] - 全ての猫の情報を取得する
    - getById(id: string): Cat - 指定したIDの猫の情報を取得する
    - create(cat: Cat): Cat - 新しい猫の情報を作成する
    - update(id: string, cat: Cat): Cat - 指定したIDの猫の情報を更新する
    - delete(id: string): void - 指定したIDの猫の情報を削除する

### UserController
- 説明: ユーザー情報を管理するコントローラークラス
- 属性:
    - なし
- 操作:
    - getAll(): User[] - 全てのユーザー情報を取得する
    - getById(id: string): User - 指定したIDのユーザー情報を取得する
    - create(user: User): User - 新しいユーザー情報を作成する
    - update(id: string, user: User): User - 指定したIDのユーザー情報を更新する
    - delete(id: string): void - 指定したIDのユーザー情報を削除する

## 4. ユースケース
1. 猫の一覧表示
    - 関連クラス: CatController, Cat
    - 関連メソッド: getAll()
2. 猫の詳細表示
    - 関連クラス: CatController, Cat
    - 関連メソッド: getById()
3. 猫の新規登録
    - 関連クラス: CatController, Cat
    - 関連メソッド: create()
4. 猫の情報更新
    - 関連クラス: CatController, Cat
    - 関連メソッド: update()
5. 猫の情報削除
    - 関連クラス: CatController, Cat
    - 関連メソッド: delete()

## 5. シーケンス図
### ユースケース1: 猫の一覧表示
```
+---------------+         +---------------+
|CatListPage    |         |CatController  |
+---------------+         +---------------+
     |                           |
     |-- getAll() --------------->
     |                           |
     |<-- Cat[] ------------------|
     |                           |
     |-- render(cats) ------------|
     |                           |
```

### ユースケース2: 猫の詳細表示
```
+---------------+         +---------------+
|CatDetailPage  |         |CatController  |
+---------------+         +---------------+
     |                           |
     |-- getById(id) -------------->
     |                           |
     |<-- Cat -------------------|
     |                           |
     |-- render(cat) --------------|
     |                           |
```

### ユースケース3: 猫の新規登録
```
+---------------+         +---------------+
|CatListPage    |         |CatController  |
+---------------+         +---------------+
     |                           |
     |-- create(newCat) ---------->
     |                           |
     |<-- Cat -------------------|
     |                           |
     |-- addToList(newCat) --------|
     |                           |
```

### ユースケース4: 猫の情報更新
```
+---------------+         +---------------+
|CatDetailPage  |         |CatController  |
+---------------+         +---------------+
     |                           |
     |-- update(id, updatedCat) --->
     |                           |
     |<-- Cat -------------------|
     |                           |
     |-- render(updatedCat) -------|
     |                           |
```

### ユースケース5: 猫の情報削除
```
+---------------+         +---------------+
|CatListPage    |         |CatController  |
+---------------+         +---------------+
     |                           |
     |-- delete(id) --------------->
     |                           |
     |<-- void ------------------|
     |                           |
     |-- removeFromList(id) -------|
     |                           |
```