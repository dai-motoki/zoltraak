# ボス缶コーヒーのネットショップ顧客管理システム

## 1. 目的
このシステムは、ボス缶コーヒーのオンラインショップの顧客管理を行うことを目的とする。顧客の登録、注文管理、注文履歴の確認などの機能を提供し、ボス缶コーヒーの販売促進と顧客サービスの向上を図る。

## 2. ファイル・フォルダ構成
```
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com
│   │   │       └── boss
│   │   │           └── coffee
│   │   │               ├── controller
│   │   │               │   ├── CustomerController.java
│   │   │               │   ├── OrderController.java
│   │   │               │   └── ProductController.java
│   │   │               ├── model
│   │   │               │   ├── Customer.java
│   │   │               │   ├── Order.java
│   │   │               │   └── Product.java
│   │   │               └── service
│   │   │                   ├── CustomerService.java
│   │   │                   ├── OrderService.java
│   │   │                   └── ProductService.java
│   │   └── resources
│   └── test
│       └── java
│           └── com
│               └── boss
│                   └── coffee
│                       ├── controller
│                       ├── model
│                       └── service
└── pom.xml
```

## 3. クラス図
```
+----------------+         +----------------+
|    Customer    |         |    Product     |
+----------------+         +----------------+
| - id: int      |         | - id: int      |
| - name: String |         | - name: String |
| - email: String|         | - price: double|
| - address: String|       | - stock: int   |
+----------------+         +----------------+
       |                           |
       |                           |
+----------------+         +----------------+
|     Order      |         |   OrderItem    |
+----------------+         +----------------+
| - id: int      |         | - id: int      |
| - customer: Customer |   | - order: Order |
| - orderDate: Date|       | - product: Product|
| - status: OrderStatus|   | - quantity: int|
+----------------+         +----------------+
       |                           |
       |                           |
+----------------+
|  OrderService  |
+----------------+
| + placeOrder() |
| + cancelOrder()|
| + viewOrders() |
+----------------+
       |
       |
+----------------+
| CustomerService|
+----------------+
| + registerCustomer()|
| + updateCustomer() |
| + getCustomerInfo()|
+----------------+
       |
       |
+----------------+
|ProductService  |
+----------------+
| + addProduct()  |
| + updateProduct()|
| + getProductInfo()|
+----------------+
```

## 4. クラスの詳細

### Customer
- **説明**: 顧客を表すクラス
- **属性**:
  - `id: int` - 顧客ID
  - `name: String` - 顧客名
  - `email: String` - 顧客メールアドレス
  - `address: String` - 顧客住所
- **操作**:
  - `registerCustomer(name, email, address): void` - 新規顧客の登録
  - `updateCustomer(id, name, email, address): void` - 顧客情報の更新
  - `getCustomerInfo(id): Customer` - 顧客情報の取得

### Product
- **説明**: 商品を表すクラス
- **属性**:
  - `id: int` - 商品ID
  - `name: String` - 商品名
  - `price: double` - 商品価格
  - `stock: int` - 在庫数
- **操作**:
  - `addProduct(name, price, stock): void` - 新規商品の追加
  - `updateProduct(id, name, price, stock): void` - 商品情報の更新
  - `getProductInfo(id): Product` - 商品情報の取得

### Order
- **説明**: 注文を表すクラス
- **属性**:
  - `id: int` - 注文ID
  - `customer: Customer` - 注文した顧客
  - `orderDate: Date` - 注文日
  - `status: OrderStatus` - 注文ステータス
- **操作**:
  - `placeOrder(customer, orderItems): Order` - 新規注文の作成
  - `cancelOrder(id): void` - 注文のキャンセル
  - `viewOrders(customer): List<Order>` - 顧客の注文履歴の表示

### OrderItem
- **説明**: 注文明細を表すクラス
- **属性**:
  - `id: int` - 注文明細ID
  - `order: Order` - 注文
  - `product: Product` - 注文された商品
  - `quantity: int` - 注文数量
- **操作**:
  - `addOrderItem(order, product, quantity): OrderItem` - 注文明細の作成

### CustomerService
- **説明**: 顧客管理に関するサービスクラス
- **操作**:
  - `registerCustomer(name, email, address): Customer` - 新規顧客の登録
  - `updateCustomer(id, name, email, address): void` - 顧客情報の更新
  - `getCustomerInfo(id): Customer` - 顧客情報の取得

### OrderService
- **説明**: 注文管理に関するサービスクラス
- **操作**:
  - `placeOrder(customer, orderItems): Order` - 新規注文の作成
  - `cancelOrder(id): void` - 注文のキャンセル
  - `viewOrders(customer): List<Order>` - 顧客の注文履歴の表示

### ProductService
- **説明**: 商品管理に関するサービスクラス
- **操作**:
  - `addProduct(name, price, stock): Product` - 新規商品の追加
  - `updateProduct(id, name, price, stock): void` - 商品情報の更新
  - `getProductInfo(id): Product` - 商品情報の取得

## 5. ユースケース
1. 新規顧客の登録
   - **関連するクラスとメソッド**:
     - `CustomerService.registerCustomer(name, email, address)`

2. 顧客情報の更新
   - **関連するクラスとメソッド**:
     - `CustomerService.updateCustomer(id, name, email, address)`

3. 商品の追加
   - **関連するクラスとメソッド**:
     - `ProductService.addProduct(name, price, stock)`

4. 商品情報の更新
   - **関連するクラスとメソッド**:
     - `ProductService.updateProduct(id, name, price, stock)`

5. 注文の作成
   - **関連するクラスとメソッド**:
     - `OrderService.placeOrder(customer, orderItems)`

6. 注文のキャンセル
   - **関連するクラスとメソッド**:
     - `OrderService.cancelOrder(id)`

7. 顧客の注文履歴の表示
   - **関連するクラスとメソッド**:
     - `OrderService.viewOrders(customer)`

## 6. シーケンス図

### 新規注文の作成
```
+---------------+   +---------------+   +---------------+   +---------------+
|  CustomerController|  CustomerService |     Order      |   OrderService  |
+---------------+   +---------------+   +---------------+   +---------------+
       |                   |                    |                    |
       | placeOrder(customer, orderItems)       |                    |
       |------------------------------>         |                    |
       |                   |                    |                    |
       |                   | registerCustomer(name, email, address) |
       |                   |--------------------->                    |
       |                   |                    |                    |
       |                   |<---------------------|                    |
       |                   |                    |                    |
       |                   | createOrder(customer, orderItems)       |
       |                   |--------------------->                    |
       |                   |                    |                    |
       |                   |<---------------------|                    |
       |<-----------------------------|         |                    |
       |                   |                    |                    |
```

### 注文の履歴表示
```
+---------------+   +---------------+   +---------------+
|  CustomerController|   OrderService  |     Order      |
+---------------+   +---------------+   +---------------+
       |                   |                    |
       | viewOrders(customer)                  |
       |------------------------------>         |
       |                   | getOrdersByCustomer(customer)|
       |                   |--------------------->         |
       |                   |<---------------------|         |
       |<-----------------------------|         |
       |                   |                    |
```

上記のシーケンス図では、オブジェクト間のメッセージの流れを示しています。カプセル化の原則に基づき、各クラスの責務が明確に分離されています。また、サービスクラスを介して、コントローラーとモデルクラスの依存関係を低減しています。