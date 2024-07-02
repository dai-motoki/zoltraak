# ペットショップ管理システム

## ゴール: 猫のペットショップのペットと顧客管理システムを作りたい

## 1. 目的
本システムは、ペットショップの店舗運営を効率化するため、ペットの在庫管理、顧客管理、販売管理などの機能を提供することを目的とする。店舗の生産性向上と顧客サービスの向上を目指す。

## 2. ファイル・フォルダ構造
```
ペットショップ管理システム/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── petshop/
│   │   │           ├── model/
│   │   │           ├── service/
│   │   │           └── ui/
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── petshop/
│       └── resources/
├── docs/
│   ├── requirements.md
│   └── design.md
├── build.gradle
└── README.md
```

## 3. クラス図
```
+-------------+        +-------------+
|    Pet      |        | PetCategory |
+-------------+        +-------------+
| - id: int   |        | - id: int   |
| - name: str |        | - name: str |
| - breed: str|        +-------------+
| - age: int  |                ^
| - price: int|                |
| - category: |                |
|   PetCategory|               |
+-------------+                |
       ^                       |
       |                       |
+-------------+        +-------------+
|   Customer  |        |  PetShop    |
+-------------+        +-------------+
| - id: int   |        | - id: int   |
| - name: str |        | - name: str |
| - email: str|        | - address: str|
| - phone: str|        | - inventory: |
+-------------+        |   Map<Pet, int>|
       ^               | - customers: |
       |               |   Set<Customer>|
       |               | - sales: Map<|
+-------------+        |   Customer, |
|   SaleOrder |        |   List<Pet>>|
+-------------+        +-------------+
| - id: int   |                ^
| - customer: |                |
|   Customer  |                |
| - pets: List|                |
|   <Pet>     |                |
| - date: Date|                |
| - total: int|                |
+-------------+                |
                               |
                    +-------------+
                    |  SalesReport|
                    +-------------+
                    | - totalSales:|
                    |   int       |
                    | - topSelling:|
                    |   Map<Pet, int>|
                    +-------------+
```

## 4. クラスの詳細

### Pet
- **説明**: ペットの情報を管理するクラス
- **属性**:
  - `id`: int - ペットのID
  - `name`: str - ペットの名前
  - `breed`: str - ペットの品種
  - `age`: int - ペットの年齢
  - `price`: int - ペットの価格
  - `category`: PetCategory - ペットのカテゴリ
- **操作**:
  - `getPetInfo()`: str - ペットの詳細情報を返す

### PetCategory
- **説明**: ペットのカテゴリを管理するクラス
- **属性**:
  - `id`: int - カテゴリのID
  - `name`: str - カテゴリの名称
- **操作**:
  - `getCategoryName()`: str - カテゴリ名を返す

### Customer
- **説明**: 顧客の情報を管理するクラス
- **属性**:
  - `id`: int - 顧客のID
  - `name`: str - 顧客の名前
  - `email`: str - 顧客のメールアドレス
  - `phone`: str - 顧客の電話番号
- **操作**:
  - `getCustomerInfo()`: str - 顧客の詳細情報を返す

### PetShop
- **説明**: ペットショップの情報を管理するクラス
- **属性**:
  - `id`: int - ペットショップのID
  - `name`: str - ペットショップの名称
  - `address`: str - ペットショップの住所
  - `inventory`: Map<Pet, int> - ペットの在庫情報
  - `customers`: Set<Customer> - 登録された顧客情報
  - `sales`: Map<Customer, List<Pet>> - 顧客ごとの購買履歴
- **操作**:
  - `addPet(Pet pet, int quantity)`: void - ペットの在庫を追加する
  - `removePet(Pet pet, int quantity)`: void - ペットの在庫を減らす
  - `registerCustomer(Customer customer)`: void - 新規顧客を登録する
  - `recordSale(Customer customer, List<Pet> pets)`: void - 販売履歴を記録する
  - `generateSalesReport()`: SalesReport - 売上レポートを生成する

### SaleOrder
- **説明**: 販売オーダーの情報を管理するクラス
- **属性**:
  - `id`: int - 販売オーダーのID
  - `customer`: Customer - 注文した顧客
  - `pets`: List<Pet> - 注文されたペットのリスト
  - `date`: Date - 注文日
  - `total`: int - 注文合計金額
- **操作**:
  - `getOrderDetails()`: str - 注文の詳細情報を返す

### SalesReport
- **説明**: 売上レポートを管理するクラス
- **属性**:
  - `totalSales`: int - 総売上
  - `topSelling`: Map<Pet, int> - 売れ筋ペットランキング
- **操作**:
  - `getTotalSales()`: int - 総売上を返す
  - `getTopSellingPets()`: Map<Pet, int> - 売れ筋ペットランキングを返す

## 5. ユースケース

1. **ペットの在庫管理**
   - 関連クラス: PetShop, Pet
   - 関連メソッド: `addPet()`, `removePet()`

2. **顧客管理**
   - 関連クラス: PetShop, Customer
   - 関連メソッド: `registerCustomer()`

3. **販売管理**
   - 関連クラス: PetShop, SaleOrder, Customer, Pet
   - 関連メソッド: `recordSale()`, `getOrderDetails()`

4. **売上レポート生成**
   - 関連クラス: PetShop, SalesReport
   - 関連メソッド: `generateSalesReport()`, `getTotalSales()`, `getTopSellingPets()`

## 6. シーケンス図

### ペットの在庫追加
```
+-------------+    +-------------+
|   PetShop   |    |     Pet     |
+-------------+    +-------------+
     addPet()           new()
         |                |
         |--------------->|
         |   create Pet   |
         |<---------------|
         |    store Pet   |
         |    in inventory|
         |--------------->|
         |   return void  |
         |<---------------|
```

### 顧客登録
```
+-------------+    +-------------+
|   PetShop   |    |   Customer  |
+-------------+    +-------------+
registerCustomer()      new()
         |                |
         |--------------->|
         |   create Customer|
         |<---------------|
         |  store Customer |
         |    in customers |
         |--------------->|
         |   return void   |
         |<---------------|
```

### 販売記録
```
+-------------+    +-------------+    +-------------+
|   PetShop   |    |  SaleOrder  |    |   Customer  |
+-------------+    +-------------+    +-------------+
  recordSale()           new()              new()
         |                |                    |
         |--------------->|                    |
         |   create SaleOrder|                |
         |<---------------|                    |
         |   create Customer|                  |
         |<--------------|------------------->|
         |   store SaleOrder|                  |
         |   in sales history|                |
         |   update inventory|                |
         |--------------->|                    |
         |   return void   |                    |
         |<---------------|                    |
```

### 売上レポート生成
```
+-------------+    +-------------+
|   PetShop   |    |SalesReport |
+-------------+    +-------------+
generateSalesReport()    new()
         |                |
         |--------------->|
         |   calculate total sales|
         |   and top selling pets|
         |<---------------|
         |   return SalesReport|
         |<---------------|
```