# 猫システム要件定義書

## 1. 目的
本システムは、ユーザーが飼育している猫の情報を管理し、猫の健康状態の把握や飼育管理を支援することを目的としています。

## 2. ファイル・フォルダ構成
```
猫システム/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── Cat.java
│   │   │           ├── Owner.java
│   │   │           ├── CatManager.java
│   │   │           └── CatClinic.java
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── example/
│       │           ├── CatTest.java
│       │           ├── OwnerTest.java
│       │           ├── CatManagerTest.java
│       │           └── CatClinicTest.java
│       └── resources/
└── README.md
```

## 3. クラス図
```
+---------------+         +---------------+
|     Owner     |         |     Cat      |
+---------------+         +---------------+
| - name: String|         | - name: String|
| - address: String|      | - age: int    |
| - phone: String|        | - breed: String|
| - email: String|        | - weight: double|
| + addCat(Cat) |         | - health: String|
| + removeCat(Cat)|        | + checkHealth()|
| + getCats(): List<Cat>| | + feed()      |
+---------------+         | + groom()     |
                          +---------------+
                                  |
                                  |
                          +---------------+
                          | CatManager    |
                          +---------------+
                          | - owners: List<Owner>|
                          | + addOwner(Owner)|
                          | + removeOwner(Owner)|
                          | + getOwners(): List<Owner>|
                          | + addCat(Cat, Owner)|
                          | + removeCat(Cat, Owner)|
                          +---------------+
                                  |
                                  |
                          +---------------+
                          | CatClinic     |
                          +---------------+
                          | - cats: List<Cat>|
                          | + checkIn(Cat)|
                          | + checkOut(Cat)|
                          | + treatCat(Cat)|
                          +---------------+
```

## 4. クラスの詳細

### Owner
- **説明**: ユーザーを表すクラスです。
- **属性**:
  - `name: String` - 飼い主の名前
  - `address: String` - 飼い主の住所
  - `phone: String` - 飼い主の電話番号
  - `email: String` - 飼い主のメールアドレス
- **操作**:
  - `addCat(Cat)` - 飼育する猫を追加する
  - `removeCat(Cat)` - 飼育する猫を削除する
  - `getCats(): List<Cat>` - 飼育している猫のリストを取得する

### Cat
- **説明**: 飼育する猫を表すクラスです。
- **属性**:
  - `name: String` - 猫の名前
  - `age: int` - 猫の年齢
  - `breed: String` - 猫の品種
  - `weight: double` - 猫の体重
  - `health: String` - 猫の健康状態
- **操作**:
  - `checkHealth()` - 猫の健康状態を確認する
  - `feed()` - 猫に餌を与える
  - `groom()` - 猫の毛づくろいを行う

### CatManager
- **説明**: 飼い主と猫の情報を管理するクラスです。
- **属性**:
  - `owners: List<Owner>` - 飼い主のリスト
- **操作**:
  - `addOwner(Owner)` - 新しい飼い主を追加する
  - `removeOwner(Owner)` - 飼い主を削除する
  - `getOwners(): List<Owner>` - 登録されている飼い主のリストを取得する
  - `addCat(Cat, Owner)` - 飼い主に猫を追加する
  - `removeCat(Cat, Owner)` - 飼い主から猫を削除する

### CatClinic
- **説明**: 猫の診療を行うクリニックを表すクラスです。
- **属性**:
  - `cats: List<Cat>` - 診療中の猫のリスト
- **操作**:
  - `checkIn(Cat)` - 猫をクリニックに入院させる
  - `checkOut(Cat)` - 猫をクリニックから退院させる
  - `treatCat(Cat)` - 猫の治療を行う

## 5. ユースケース
1. **猫の登録**
   - 関連クラス: `Owner`, `Cat`, `CatManager`
   - 関連メソッド: `Owner.addCat(Cat)`, `CatManager.addCat(Cat, Owner)`

2. **猫の情報管理**
   - 関連クラス: `Owner`, `Cat`, `CatManager`
   - 関連メソッド: `Owner.getCats()`, `Cat.checkHealth()`, `Cat.feed()`, `Cat.groom()`

3. **猫の診療**
   - 関連クラス: `Cat`, `CatClinic`
   - 関連メソッド: `CatClinic.checkIn(Cat)`, `CatClinic.treatCat(Cat)`, `CatClinic.checkOut(Cat)`

4. **飼い主の管理**
   - 関連クラス: `Owner`, `CatManager`
   - 関連メソッド: `CatManager.addOwner(Owner)`, `CatManager.removeOwner(Owner)`, `CatManager.getOwners()`

## 6. シーケンス図

### 猫の登録
```
+----------+  +----------+  +-------------+
| Owner    |  | Cat      |  | CatManager  |
+----------+  +----------+  +-------------+
     |              |              |
 addCat(cat)        |              |
     |------------->|              |
     |              |  addCat(cat, owner)
     |              |------------->|
     |              |              |
     |<--------------|              |
     |              |              |
```

### 猫の健康状態の確認
```
+----------+  +----------+
| Owner    |  | Cat      |
+----------+  +----------+
     |              |
 getCats()          |
     |------------->|
     |              |   checkHealth()
     |              |------------->|
     |              |              |
     |<--------------|              |
     |              |              |
```

### 猫の診療
```
+----------+  +-------------+  +--------------+
| Owner    |  | Cat         |  | CatClinic    |
+----------+  +-------------+  +--------------+
     |              |                 |
     |              |   checkIn(cat)  |
     |              |---------------->|
     |              |                 |
     |              |   treatCat(cat) |
     |              |---------------->|
     |              |                 |
     |              |   checkOut(cat) |
     |              |<-----------------|
     |              |                 |
```