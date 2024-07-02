# きつねのペットショップのペットと顧客管理システム

## 1. 目的
このシステムは、きつねのペットショップの運営を支援するために開発されます。主な目的は、ペットの在庫管理、顧客情報の管理、注文処理などの機能を提供することで、ペットショップの業務を効率化し、顧客サービスの向上につなげることです。

## 2. ファイル・フォルダ構成
```
きつねのペットショップ管理システム/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── model/
│   │   │           │   ├── Customer.java
│   │   │           │   ├── Order.java
│   │   │           │   ├── OrderItem.java
│   │   │           │   └── Product.java
│   │   │           ├── repository/
│   │   │           │   ├── CustomerRepository.java
│   │   │           │   ├── OrderRepository.java
│   │   │           │   └── ProductRepository.java
│   │   │           ├── service/
│   │   │           │   ├── CustomerService.java
│   │   │           │   ├── OrderService.java
│   │   │           │   └── ProductService.java
│   │   │           ├── controller/
│   │   │           │   ├── CustomerController.java
│   │   │           │   ├── OrderController.java
│   │   │           │   └── ProductController.java
│   │   │           └── KitsunePetShopApplication.java
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── example/
│       │           ├── model/
│       │           ├── repository/
│       │           ├── service/
│       │           └── controller/
│       └── resources/
├── pom.xml
├── README.md
└── docs/
    ├── requirements.md
    └── design.md
```

## 3. クラス図
```
+----------------+          +----------------+
|    Customer    |          |     Product    |
+----------------+          +----------------+
| - id: int      |          | - id: int      |
| - name: String |          | - name: String |
| - email: String|          | - description: String|
| - phone: String|          | - price: double|
| - address: String|        | - quantity: int|
+----------------+          +----------------+
       |                             |
       |                             |
+----------------+          +----------------+
|    Order       |          |  OrderItem     |
+----------------+          +----------------+
| - id: int      |          | - id: int      |
| - customer: Customer|     | - order: Order |
| - date: Date   |          | - product: Product|
| - total: double|          | - quantity: int|
+----------------+          +----------------+
       |                             |
       |                             |
+----------------+
|  OrderService  |
+----------------+
| + placeOrder(Customer, List<Product>, double): Order|
| + getOrderHistory(Customer): List<Order>|
+----------------+
```

## 4. クラスの詳細

### Customer
- 説明: ペットショップの顧客を表すクラス
- 属性:
  - id: int - 顧客ID
  - name: String - 顧客名
  - email: String - 顧客メールアドレス
  - phone: String - 顧客電話番号
  - address: String - 顧客住所
- 操作:
  - getCustomerInfo(): 顧客情報を取得する
  - updateCustomerInfo(String, String, String, String): 顧客情報を更新する

### Product
- 説明: ペットショップで販売するペットを表すクラス
- 属性:
  - id: int - ペットID
  - name: String - ペットの名称
  - description: String - ペットの説明
  - price: double - ペットの価格
  - quantity: int - ペットの在庫数
- 操作:
  - getProductInfo(): ペットの情報を取得する
  - updateProductInfo(String, String, double, int): ペットの情報を更新する
  - decreaseQuantity(int): ペットの在庫数を減らす

### Order
- 説明: 顧客の注文を表すクラス
- 属性:
  - id: int - 注文ID
  - customer: Customer - 注文した顧客
  - date: Date - 注文日
  - total: double - 注文合計金額
- 操作:
  - getOrderDetails(): 注文の詳細を取得する

### OrderItem
- 説明: 注文に含まれる個別の商品を表すクラス
- 属性:
  - id: int - 注文明細ID
  - order: Order - 注文
  - product: Product - 注文された商品
  - quantity: int - 注文数量
- 操作:
  - getItemDetails(): 注文明細の情報を取得する

### OrderService
- 説明: 注文処理を行うサービスクラス
- 操作:
  - placeOrder(Customer, List<Product>, double): 注文を作成する
  - getOrderHistory(Customer): 顧客の注文履歴を取得する

## 5. ユースケース
1. **新規顧客登録**
   - 関連クラス: Customer
   - 関連メソッド: createCustomer(name, email, phone, address)

2. **顧客情報の表示・更新**
   - 関連クラス: Customer
   - 関連メソッド: getCustomerInfo(), updateCustomerInfo(name, email, phone, address)

3. **ペットの在庫管理**
   - 関連クラス: Product
   - 関連メソッド: getProductInfo(), updateProductInfo(name, description, price, quantity), decreaseQuantity(quantity)

4. **注文の作成**
   - 関連クラス: Order, OrderItem, OrderService
   - 関連メソッド: placeOrder(customer, products, total)

5. **注文履歴の表示**
   - 関連クラス: Order, OrderService
   - 関連メソッド: getOrderHistory(customer)

## 6. シーケンス図

### 新規注文の作成
```
+------------+  +------------+  +------------+  +------------+
|  Customer  |  |  OrderItem |  |   Product  |  | OrderService|
+------------+  +------------+  +------------+  +------------+
     |                |               |                 |
     | placeOrder()   |               |                 |
     |--------------->|               |                 |
     |                |getProductInfo()|                 |
     |                |-------------->|                 |
     |                |    product    |                 |
     |                |<--------------|                 |
     |                |decreaseQuantity()|              |
     |                |-------------->|                 |
     |                |               |createOrder()    |
     |                |               |--------------->|
     |                |               |    order       |
     |                |<--------------|                 |
     |                |createOrderItem()|               |
     |                |-------------->|                 |
     |                |               |                 |
     |                |<--------------|                 |
     |                |               |                 |
     |<---------------|               |                 |
```

### 顧客の注文履歴の表示
```
+------------+  +------------+  +------------+
|  Customer  |  |    Order   |  | OrderService|
+------------+  +------------+  +------------+
     |                |               |
     | getOrderHistory()|             |
     |--------------->|               |
     |                |getOrders()    |
     |                |-------------->|
     |                |   orders     |
     |                |<--------------|
     |                |               |
     |<---------------|               |
```