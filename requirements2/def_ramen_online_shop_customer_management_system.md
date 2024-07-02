# ラーメンのネットショップ顧客管理システム

## 1. 目的
本システムは、ラーメン店の顧客管理を行うためのWebアプリケーションです。店舗の商品情報の管理、顧客の注文履歴の管理、顧客情報の管理などの機能を提供し、ラーメン店の顧客サービスの向上と業務効率化を目的としています。

## 2. ファイル・フォルダ構成
```
ラーメンネットショップ顧客管理システム
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com
│   │   │       └── example
│   │   │           ├── controller
│   │   │           │   ├── CustomerController.java
│   │   │           │   ├── OrderController.java
│   │   │           │   └── ProductController.java
│   │   │           ├── model
│   │   │           │   ├── Customer.java
│   │   │           │   ├── Order.java
│   │   │           │   └── Product.java
│   │   │           └── service
│   │   │               ├── CustomerService.java
│   │   │               ├── OrderService.java
│   │   │               └── ProductService.java
│   │   └── resources
│   │       ├── application.properties
│   │       └── templates
│   │           ├── customer
│   │           │   ├── customerList.html
│   │           │   └── customerDetails.html
│   │           ├── order
│   │           │   ├── orderList.html
│   │           │   └── orderDetails.html
│   │           └── product
│   │               ├── productList.html
│   │               └── productDetails.html
│   └── test
│       └── java
│           └── com
│               └── example
│                   ├── controller
│                   │   ├── CustomerControllerTest.java
│                   │   ├── OrderControllerTest.java
│                   │   └── ProductControllerTest.java
│                   ├── model
│                   │   ├── CustomerTest.java
│                   │   ├── OrderTest.java
│                   │   └── ProductTest.java
│                   └── service
│                       ├── CustomerServiceTest.java
│                       ├── OrderServiceTest.java
│                       └── ProductServiceTest.java
└── pom.xml
```

## 3. クラス図
```
+---------------+         +---------------+
|    Customer   |         |    Product    |
+---------------+         +---------------+
| - id: Long    |         | - id: Long    |
| - name: String|         | - name: String|
| - email: String|         | - description: String|
| - address: String|      | - price: Double|
+---------------+         +---------------+
       ^                           ^
       |                           |
+---------------+         +---------------+
|     Order     |         |  OrderDetails |
+---------------+         +---------------+
| - id: Long    |         | - id: Long    |
| - customer: Customer |  | - order: Order|
| - orderDate: Date|      | - product: Product|
| - totalAmount: Double| | - quantity: Integer|
+---------------+         +---------------+
       ^                           ^
       |                           |
+---------------+         +---------------+
|  OrderService |         | CustomerService|
+---------------+         +---------------+
| - createOrder()|        | - createCustomer()|
| - getOrderList()|       | - getCustomerList()|
| - updateOrder()|        | - updateCustomer()|
+---------------+         +---------------+
       ^                           ^
       |                           |
+---------------+         +---------------+
| ProductService|         |  Controller   |
+---------------+         +---------------+
| - createProduct()|      | - handleCustomerRequest()|
| - getProductList()|     | - handleOrderRequest()|
| - updateProduct()|      | - handleProductRequest()|
+---------------+         +---------------+
```

## 4. クラスの詳細
### Customer
- 説明: 顧客情報を管理するクラス
- 属性:
  - id: Long - 顧客ID
  - name: String - 顧客名
  - email: String - 顧客メールアドレス
  - address: String - 顧客住所
- 操作:
  - getCustomerInfo(): 顧客情報を取得する
  - updateCustomerInfo(name, email, address): 顧客情報を更新する

### Order
- 説明: 注文情報を管理するクラス
- 属性:
  - id: Long - 注文ID
  - customer: Customer - 注文した顧客
  - orderDate: Date - 注文日
  - totalAmount: Double - 注文合計金額
- 操作:
  - placeOrder(customer, orderDetails): 注文を登録する
  - getOrderDetails(): 注文詳細を取得する
  - updateOrderDetails(orderDetails): 注文詳細を更新する

### OrderDetails
- 説明: 注文明細情報を管理するクラス
- 属性:
  - id: Long - 注文明細ID
  - order: Order - 注文情報
  - product: Product - 注文商品
  - quantity: Integer - 注文数量
- 操作:
  - addOrderDetails(product, quantity): 注文明細を追加する
  - updateOrderDetails(product, quantity): 注文明細を更更新する

### Product
- 説明: 商品情報を管理するクラス
- 属性:
  - id: Long - 商品ID
  - name: String - 商品名
  - description: String - 商品説明
  - price: Double - 商品価格
- 操作:
  - getProductInfo(): 商品情報を取得する
  - updateProductInfo(name, description, price): 商品情報を更新する

### CustomerService
- 説明: 顧客管理に関するサービスクラス
- 操作:
  - createCustomer(name, email, address): 新規顧客を登録する
  - getCustomerList(): 顧客一覧を取得する
  - updateCustomer(id, name, email, address): 顧客情報を更新する

### OrderService
- 説明: 注文管理に関するサービスクラス
- 操作:
  - createOrder(customer, orderDetails): 新規注文を登録する
  - getOrderList(): 注文一覧を取得する
  - updateOrder(id, orderDetails): 注文情報を更新する

### ProductService
- 説明: 商品管理に関するサービスクラス
- 操作:
  - createProduct(name, description, price): 新規商品を登録する
  - getProductList(): 商品一覧を取得する
  - updateProduct(id, name, description, price): 商品情報を更新する

### Controller
- 説明: ユーザーリクエストを処理するコントローラークラス
- 操作:
  - handleCustomerRequest(request): 顧客管理に関するリクエストを処理する
  - handleOrderRequest(request): 注文管理に関するリクエストを処理する
  - handleProductRequest(request): 商品管理に関するリクエストを処理する

## 5. ユースケース
1. 顧客管理
   - 顧客の新規登録
   - 顧客情報の表示
   - 顧客情報の更新

2. 注文管理
   - 新規注文の登録
   - 注文履歴の表示
   - 注文情報の更新

3. 商品管理
   - 新規商品の登録
   - 商品情報の表示
   - 商品情報の更新

## 6. シーケンス図
### 新規顧客登録
```
+----------------+    +----------------+    +----------------+
|  CustomerController|  |CustomerService|    |      Customer   |
+----------------+    +----------------+    +----------------+
       |                       |                     |
       | createCustomer(name,  |                     |
       |         email, address)|                    |
       |---------------------->|                     |
       |                       | new Customer(name,  |
       |                       |     email, address) |
       |                       |-------------------->|
       |                       |   saveCustomer()    |
       |                       |-------------------->|
       |           Customer ID |                     |
       |<----------------------|                     |
       |                       |                     |
```

### 注文登録
```
+----------------+    +----------------+    +----------------+    +----------------+
|   OrderController|  |   OrderService |    |     Order      |    | OrderDetails   |
+----------------+    +----------------+    +----------------+    +----------------+
       |                       |                     |                     |
       | placeOrder(customer,  |                     |                     |
       |        orderDetails)  |                     |                     |
       |---------------------->|                     |                     |
       |                       | new Order(customer, |                     |
       |                       |     orderDate)      |                     |
       |                       |-------------------->|                     |
       |                       |   saveOrder()       |                     |
       |                       |-------------------->|                     |
       |                       |                     | new OrderDetails(   |
       |                       |                     |   order, product,   |
       |                       |                     |     quantity)       |
       |                       |                     |-------------------->|
       |                       |                     |   saveOrderDetails()|
       |                       |                     |-------------------->|
       |           Order ID     |                     |                     |
       |<----------------------|                     |                     |
       |                       |                     |                     |
```