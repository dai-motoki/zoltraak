# カレーのネットショップのペットと顧客管理システム

## 1. 目的
本システムは、カレーのネットショップの顧客管理と、ペット管理を行うことを目的としています。顧客情報の管理、ペットの情報管理、注文管理など、ショップ運営に必要な機能を提供します。

## 2. ファイル・フォルダ構成
```
root/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── company/
│   │   │           ├── models/
│   │   │           │   ├── Customer.java
│   │   │           │   ├── Order.java
│   │   │           │   ├── Pet.java
│   │   │           │   └── Product.java
│   │   │           ├── repositories/
│   │   │           │   ├── CustomerRepository.java
│   │   │           │   ├── OrderRepository.java
│   │   │           │   ├── PetRepository.java
│   │   │           │   └── ProductRepository.java
│   │   │           ├── services/
│   │   │           │   ├── CustomerService.java
│   │   │           │   ├── OrderService.java
│   │   │           │   ├── PetService.java
│   │   │           │   └── ProductService.java
│   │   │           └── CurrieShopApp.java
│   │   └── resources/
│   └── test/
│       └── java/
│           └── com/
│               └── company/
│                   ├── models/
│                   ├── repositories/
│                   ├── services/
│                   └── CurrieShopAppTest.java
├── build.gradle
└── README.md
```

## 3. クラス図
```
+---------------+        +---------------+
|    Customer   |        |     Order     |
+---------------+        +---------------+
| - id: int     |        | - id: int     |
| - name: String|        | - customerId: int
| - email: String|        | - productId: int
| - address: String|     | - quantity: int
| - phone: String|        | - orderDate: Date
+---------------+        +---------------+
       ^                         ^
       |                         |
+---------------+        +---------------+
|      Pet      |        |   Product     |
+---------------+        +---------------+
| - id: int     |        | - id: int     |
| - customerId: int|     | - name: String|
| - name: String|        | - description: String|
| - species: String|     | - price: double|
| - age: int    |        +---------------+
+---------------+
       ^
       |
+---------------+
|CurrieShopApp |
+---------------+
| + main(): void|
+---------------+

Relationships:
Customer -- 1..* --> Order
Customer -- 1..* --> Pet
Order -- 1 --> Product
```

## 4. クラスの詳細
### Customer
- **説明**: 顧客情報を管理するクラス
- **属性**:
  - `id: int` - 顧客ID
  - `name: String` - 顧客名
  - `email: String` - 顧客メールアドレス
  - `address: String` - 顧客住所
  - `phone: String` - 顧客電話番号
- **操作**:
  - `getCustomerInfo(): Map<String, String>` - 顧客情報を取得する
  - `updateCustomerInfo(Map<String, String>)` - 顧客情報を更新する
  - `placeOrder(Order)` - 注文を行う

### Pet
- **説明**: 顧客のペット情報を管理するクラス
- **属性**:
  - `id: int` - ペットID
  - `customerId: int` - 顧客ID
  - `name: String` - ペット名
  - `species: String` - ペットの種類
  - `age: int` - ペットの年齢
- **操作**:
  - `getPetInfo(): Map<String, String>` - ペット情報を取得する
  - `updatePetInfo(Map<String, String>)` - ペット情報を更新する

### Order
- **説明**: 注文情報を管理するクラス
- **属性**:
  - `id: int` - 注文ID
  - `customerId: int` - 顧客ID
  - `productId: int` - 商品ID
  - `quantity: int` - 注文数量
  - `orderDate: Date` - 注文日
- **操作**:
  - `getOrderDetails(): Map<String, Object>` - 注文詳細を取得する
  - `updateOrderStatus(String)` - 注文ステータスを更新する

### Product
- **説明**: 商品情報を管理するクラス
- **属性**:
  - `id: int` - 商品ID
  - `name: String` - 商品名
  - `description: String` - 商品説明
  - `price: double` - 商品価格
- **操作**:
  - `getProductInfo(): Map<String, Object>` - 商品情報を取得する
  - `updateProductInfo(Map<String, Object>)` - 商品情報を更新する

### CurrieShopApp
- **説明**: アプリケーションの起点となるクラス
- **操作**:
  - `main(String[])` - アプリケーションのエントリーポイント

## 5. ユースケース
1. 顧客の登録と管理
   - 関連クラス: `Customer`, `CustomerRepository`, `CustomerService`
   - 関連メソッド: `getCustomerInfo()`, `updateCustomerInfo()`
2. ペットの登録と管理
   - 関連クラス: `Pet`, `PetRepository`, `PetService`
   - 関連メソッド: `getPetInfo()`, `updatePetInfo()`
3. 注文の管理
   - 関連クラス: `Order`, `OrderRepository`, `OrderService`
   - 関連メソッド: `getOrderDetails()`, `updateOrderStatus()`
4. 商品の管理
   - 関連クラス: `Product`, `ProductRepository`, `ProductService`
   - 関連メソッド: `getProductInfo()`, `updateProductInfo()`

## 6. シーケンス図
### 顧客の新規登録
```
+-------------+    +---------------+    +-----------------+
| CustomerApp |    | CustomerService|    | CustomerRepository|
+-------------+    +---------------+    +-----------------+
       |                  |                       |
       | createCustomer() |                       |
       |---------------->|                       |
       |                  | saveCustomer()        |
       |                  |-------------------->|
       |                  |                       |
       |                  |<--------------------|
       |                  |                       |
       |<-----------------|                       |
       |                  |                       |
```

### 注文の作成
```
+-------------+    +---------------+    +-----------------+    +---------------+
|   OrderApp  |    |   OrderService|    |  OrderRepository|    |  ProductService|
+-------------+    +---------------+    +-----------------+    +---------------+
       |                  |                       |                       |
       | placeOrder()     |                       |                       |
       |---------------->|                       |                       |
       |                  | getProduct()          |                       |
       |                  |-------------------->|                       |
       |                  |<--------------------|                       |
       |                  | calculateTotal()     |                       |
       |                  |-------------------->|                       |
       |                  | saveOrder()          |                       |
       |                  |-------------------->|                       |
       |                  |<--------------------|                       |
       |<-----------------|                       |                       |
```

### 顧客情報の更新
```
+-------------+    +---------------+    +-----------------+
| CustomerApp |    | CustomerService|    | CustomerRepository|
+-------------+    +---------------+    +-----------------+
       |                  |                       |
       | updateCustomer() |                       |
       |---------------->|                       |
       |                  | getCustomer()         |
       |                  |-------------------->|
       |                  |<--------------------|
       |                  | updateCustomer()     |
       |                  |-------------------->|
       |                  |<--------------------|
       |<-----------------|                       |
```