# カスタネットのネットショップ顧客管理システム

## 1. 目的
このシステムは、カスタネットのネットショップの顧客管理を行うことを目的としています。顧客情報の管理、注文履歴の管理、商品情報の管理などの機能を提供し、ショップの運営を支援します。

## 2. ファイル・フォルダ構成
```
.
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com
│   │   │       └── castanets
│   │   │           ├── customer
│   │   │           │   ├── Customer.java
│   │   │           │   ├── CustomerRepository.java
│   │   │           │   └── CustomerService.java
│   │   │           ├── order
│   │   │           │   ├── Order.java
│   │   │           │   ├── OrderRepository.java
│   │   │           │   └── OrderService.java
│   │   │           ├── product
│   │   │           │   ├── Product.java
│   │   │           │   ├── ProductRepository.java
│   │   │           │   └── ProductService.java
│   │   │           └── CastanetsShopApplication.java
│   │   └── resources
│   └── test
│       └── java
│           └── com
│               └── castanets
│                   ├── customer
│                   │   ├── CustomerRepositoryTest.java
│                   │   └── CustomerServiceTest.java
│                   ├── order
│                   │   ├── OrderRepositoryTest.java
│                   │   └── OrderServiceTest.java
│                   └── product
│                       ├── ProductRepositoryTest.java
│                       └── ProductServiceTest.java
├── build.gradle
└── README.md
```

## 3. クラス図
```
+---------------+      +---------------+
|   Customer    |      |    Product    |
+---------------+      +---------------+
| - id: int     |      | - id: int     |
| - name: String|      | - name: String|
| - email: String|      | - description: String|
| - address: String|   | - price: double|
+---------------+      +---------------+
      ^                        ^
      |                        |
+---------------+      +---------------+
|  CustomerService  |  |  ProductService|
+---------------+      +---------------+
| + createCustomer() | | + createProduct()|
| + updateCustomer() | | + updateProduct()|
| + deleteCustomer() | | + deleteProduct()|
| + getCustomer()    | | + getProduct()   |
+---------------+      +---------------+
      ^                        ^
      |                        |
+---------------+      +---------------+
|  OrderService   |      |     Order     |
+---------------+      +---------------+
| + placeOrder()  |      | - id: int     |
| + cancelOrder() |      | - customerId: int|
| + getOrders()   |      | - productId: int|
+---------------+      | - quantity: int |
                       | - orderDate: Date|
                       +---------------+
```

## 4. クラスの詳細
### Customer
- **クラス名**: Customer
- **説明**: 顧客情報を表すクラス
- **属性（フィールド）**:
  - `id: int` - 顧客ID
  - `name: String` - 顧客名
  - `email: String` - 顧客メールアドレス
  - `address: String` - 顧客住所
- **操作（メソッド）**:
  - 存在しない

### CustomerService
- **クラス名**: CustomerService
- **説明**: 顧客情報を管理するサービスクラス
- **属性（フィールド）**: 
  - 存在しない
- **操作（メソッド）**:
  - `createCustomer(Customer customer)` - 新規顧客を作成する
  - `updateCustomer(int id, Customer updatedCustomer)` - 既存の顧客情報を更新する
  - `deleteCustomer(int id)` - 顧客情報を削除する
  - `getCustomer(int id)` - 顧客情報を取得する

### Product
- **クラス名**: Product
- **説明**: 商品情報を表すクラス
- **属性（フィールド）**:
  - `id: int` - 商品ID
  - `name: String` - 商品名
  - `description: String` - 商品説明
  - `price: double` - 商品価格
- **操作（メソッド）**:
  - 存在しない
  
### ProductService  
- **クラス名**: ProductService
- **説明**: 商品情報を管理するサービスクラス
- **属性（フィールド）**:
  - 存在しない
- **操作（メソッド）**:
  - `createProduct(Product product)` - 新規商品を作成する
  - `updateProduct(int id, Product updatedProduct)` - 既存の商品情報を更新する
  - `deleteProduct(int id)` - 商品情報を削除する
  - `getProduct(int id)` - 商品情報を取得する

### Order
- **クラス名**: Order
- **説明**: 注文情報を表すクラス
- **属性（フィールド）**:
  - `id: int` - 注文ID
  - `customerId: int` - 顧客ID
  - `productId: int` - 商品ID
  - `quantity: int` - 注文数量
  - `orderDate: Date` - 注文日
- **操作（メソッド）**:
  - 存在しない

### OrderService
- **クラス名**: OrderService
- **説明**: 注文情報を管理するサービスクラス
- **属性（フィールド）**:
  - 存在しない
- **操作（メソッド）**:
  - `placeOrder(Order order)` - 新規注文を作成する
  - `cancelOrder(int id)` - 注文をキャンセルする
  - `getOrders()` - 全ての注文情報を取得する

## 5. ユースケース
1. 顧客管理
   - 顧客の新規登録
   - 顧客情報の更新
   - 顧客情報の削除
   - 顧客情報の参照

2. 商品管理
   - 商品の新規登録
   - 商品情報の更新
   - 商品情報の削除
   - 商品情報の参照

3. 注文管理
   - 新規注文の作成
   - 注文のキャンセル
   - 注文履歴の参照

## 6. シーケンス図
### 顧客の新規登録
```
+---------------+    +---------------+    +---------------+
| CustomerClient|    |CustomerService|    |     Customer   |
+---------------+    +---------------+    +---------------+
       |                     |                     |
       | createCustomer()    |                     |
       |-------------------->|                     |
       |                     | new Customer()      |
       |                     |-------------------->|
       |                     |                     | save()
       |                     |-------------------->|
       |                     |                     |
       |<--------------------|                     |
       |     Customer        |                     |
       |                     |                     |
```

### 商品の新規登録
```
+---------------+    +---------------+    +---------------+
|  ProductClient|    | ProductService|    |     Product    |
+---------------+    +---------------+    +---------------+
       |                     |                     |
       | createProduct()     |                     |
       |-------------------->|                     |
       |                     | new Product()       |
       |                     |-------------------->|
       |                     |                     | save()
       |                     |-------------------->|
       |                     |                     |
       |<--------------------|                     |
       |     Product         |                     |
       |                     |                     |
```

### 新規注文の作成
```
+---------------+    +---------------+    +---------------+    +---------------+
|   OrderClient |    |  OrderService |    |     Customer   |    |    Product    |
+---------------+    +---------------+    +---------------+    +---------------+
       |                     |                     |                     |
       | placeOrder()        |                     |                     |
       |-------------------->|                     |                     |
       |                     | getCustomer()       |                     |
       |                     |-------------------->|                     |
       |                     |                     | getCustomer()       |
       |                     |<--------------------|                     |
       |                     |                     |                     |
       |                     | getProduct()        |                     |
       |                     |-------------------->|                     |
       |                     |                     | getProduct()        |
       |                     |<--------------------|                     |
       |                     | new Order()         |                     |
       |                     |-------------------->|                     |
       |                     |                     | save()             |
       |                     |-------------------->|                     |
       |                     |                     |                     |
       |<--------------------|                     |                     |
       |     Order           |                     |                     |
       |                     |                     |                     |
```