# 鏡売り会社の顧客管理システム

## 1. 目的
本システムは、鏡を販売する会社の顧客管理を行うことを目的とする。顧客情報の登録、検索、受注管理、販売実績の集計などの機能を提供し、顧客サービスの向上と業務効率化を図る。

## 2. ファイル・フォルダ構成
```
- src/
  - main/
    - java/
      - com/
        - mirrorsales/
          - Main.java
          - controller/
            - CustomerController.java
            - OrderController.java
          - model/
            - Customer.java
            - Order.java
            - Product.java
          - repository/
            - CustomerRepository.java
            - OrderRepository.java
            - ProductRepository.java
          - service/
            - CustomerService.java
            - OrderService.java
            - ProductService.java
  - test/
    - java/
      - com/
        - mirrorsales/
          - CustomerControllerTest.java
          - OrderControllerTest.java
          - CustomerServiceTest.java
          - OrderServiceTest.java
```

## 3. クラス図
```
+---------------+          +---------------+
|   Customer    |          |    Product    |
+---------------+          +---------------+
| - id: String  |          | - id: String  |
| - name: String|          | - name: String|
| - email: String|          | - price: int  |
| - phone: String|          +---------------+
+---------------+                  ^
        ^                          |
        |                          |
+---------------+          +---------------+
|     Order     |          |  OrderDetail  |
+---------------+          +---------------+
| - id: String  |          | - id: String  |
| - customer: Customer |   | - order: Order|
| - date: Date  |          | - product: Product|
| - total: int  |          | - quantity: int|
+---------------+          +---------------+
        ^
        |
+---------------+
| CustomerController |
+---------------+
| - customerService: CustomerService|
| - orderService: OrderService|
| - productService: ProductService|
+---------------+
        ^
        |
+---------------+
|  CustomerService  |
+---------------+
| - customerRepository: CustomerRepository|
| - createCustomer(customer: Customer): void|
| - getCustomer(id: String): Customer|
| - updateCustomer(customer: Customer): void|
+---------------+
        ^
        |
+---------------+
|  OrderService   |
+---------------+
| - orderRepository: OrderRepository|
| - createOrder(order: Order): void|
| - getOrder(id: String): Order|
| - updateOrder(order: Order): void|
+---------------+
        ^
        |
+---------------+
| ProductService  |
+---------------+
| - productRepository: ProductRepository|
| - getProduct(id: String): Product|
+---------------+
```

## 4. クラスの詳細

### Customer
- 説明: 顧客情報を表すクラス
- 属性:
  - id: String - 顧客ID
  - name: String - 顧客名
  - email: String - メールアドレス
  - phone: String - 電話番号
- 操作:
  - なし

### Product
- 説明: 販売する製品を表すクラス
- 属性:
  - id: String - 製品ID
  - name: String - 製品名
  - price: int - 価格
- 操作:
  - なし

### Order
- 説明: 受注情報を表すクラス
- 属性:
  - id: String - 注文ID
  - customer: Customer - 注文した顧客
  - date: Date - 注文日
  - total: int - 注文合計金額
- 操作:
  - なし

### OrderDetail
- 説明: 注文明細を表すクラス
- 属性:
  - id: String - 明細ID
  - order: Order - 注文情報
  - product: Product - 注文された製品
  - quantity: int - 注文数量
- 操作:
  - なし

### CustomerController
- 説明: 顧客管理に関する操作を行うコントローラークラス
- 属性:
  - customerService: CustomerService - 顧客サービスクラス
  - orderService: OrderService - 注文サービスクラス
  - productService: ProductService - 製品サービスクラス
- 操作:
  - なし

### CustomerService
- 説明: 顧客情報の管理を行うサービスクラス
- 属性:
  - customerRepository: CustomerRepository - 顧客リポジトリ
- 操作:
  - createCustomer(customer: Customer): void - 顧客を新規作成する
  - getCustomer(id: String): Customer - 顧客IDから顧客情報を取得する
  - updateCustomer(customer: Customer): void - 顧客情報を更新する

### OrderService
- 説明: 注文情報の管理を行うサービスクラス
- 属性:
  - orderRepository: OrderRepository - 注文リポジトリ
- 操作:
  - createOrder(order: Order): void - 注文を新規作成する
  - getOrder(id: String): Order - 注文IDから注文情報を取得する
  - updateOrder(order: Order): void - 注文情報を更新する

### ProductService
- 説明: 製品情報の管理を行うサービスクラス
- 属性:
  - productRepository: ProductRepository - 製品リポジトリ
- 操作:
  - getProduct(id: String): Product - 製品IDから製品情報を取得する

## 5. ユースケース

1. 顧客情報の登録
   - 関連クラス: CustomerController, CustomerService, Customer
   - 関連メソッド: createCustomer(customer: Customer)

2. 顧客情報の検索
   - 関連クラス: CustomerController, CustomerService, Customer
   - 関連メソッド: getCustomer(id: String)

3. 注文の登録
   - 関連クラス: CustomerController, OrderService, Order, OrderDetail, Product
   - 関連メソッド: createOrder(order: Order)

4. 注文情報の検索
   - 関連クラス: CustomerController, OrderService, Order
   - 関連メソッド: getOrder(id: String)

5. 販売実績の集計
   - 関連クラス: CustomerController, OrderService, Order, OrderDetail, Product
   - 関連メソッド: getOrder(id: String), getProduct(id: String)

## 6. シーケンス図

### 顧客情報の登録
```
+----------------+    +----------------+    +---------------+
| CustomerController|  | CustomerService|    |    Customer    |
+----------------+    +----------------+    +---------------+
       |                       |                     |
       | createCustomer(customer)|                     |
       |----------------------->|                     |
       |                       | createCustomer(customer)|
       |                       |-------------------->|
       |                       |                     | 
       |                       |<--------------------|
       |                       |                     |
       |<----------------------|                     |
       |                        |                     |
```

### 注文の登録
```
+----------------+    +----------------+    +---------------+    +---------------+
| CustomerController|  |   OrderService |    |     Order     |    | OrderDetail  |
+----------------+    +----------------+    +---------------+    +---------------+
       |                       |                     |                     |
       | createOrder(order)    |                     |                     |
       |---------------------->|                     |                     |
       |                       | createOrder(order)  |                     |
       |                       |------------------>  |                     |
       |                       |                     | createOrderDetail() |
       |                       |                     |-------------------->|
       |                       |<-------------------|                     |
       |                       |                     |                     |
       |<----------------------|                     |                     |
       |                        |                     |                     |
```

### 販売実績の集計
```
+----------------+    +----------------+    +---------------+    +---------------+
| CustomerController|  |   OrderService |    |     Order     |    |    Product    |
+----------------+    +----------------+    +---------------+    +---------------+
       |                       |                     |                     |
       | getOrder(orderId)     |                     |                     |
       |---------------------->|                     |                     |
       |                       | getOrder(orderId)   |                     |
       |                       |------------------>  |                     |
       |                       |                     | getProduct(productId)|
       |                       |                     |-------------------->|
       |                       |<-------------------|                     |
       |                       |                     |                     |
       |<----------------------|                     |                     |
       |                        |                     |                     |
```