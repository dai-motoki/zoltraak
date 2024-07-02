# 手帳のネットショップ顧客管理システム

## 1. 目的
このシステムは、手帳の販売ネットショップの顧客管理を目的としている。顧客情報の管理、注文履歴の管理、商品在庫管理などの機能を提供し、ショップの運営を効率化することが目的である。

## 2. ファイル・フォルダ構成
```
- src/
  - main/
    - java/
      - com/
        - example/
          - customer/
            - Customer.java
            - CustomerRepository.java
            - CustomerService.java
          - order/
            - Order.java
            - OrderRepository.java
            - OrderService.java
          - product/
            - Product.java
            - ProductRepository.java
            - ProductService.java
          - ShopApplication.java
    - resources/
      - application.properties
  - test/
    - java/
      - com/
        - example/
          - customer/
            - CustomerRepositoryTest.java
            - CustomerServiceTest.java
          - order/
            - OrderRepositoryTest.java
            - OrderServiceTest.java
          - product/
            - ProductRepositoryTest.java
            - ProductServiceTest.java
```

## 3. クラス図
```
+---------------+          +---------------+
|   Customer    |          |    Product    |
+---------------+          +---------------+
| - id: Long    |          | - id: Long    |
| - name: String|          | - name: String|
| - email: String|          | - description: String|
| - address: String|        | - price: Double|
| - phone: String|          | - stock: Integer|
+---------------+          +---------------+
       ^                           ^
       |                           |
+---------------+          +---------------+
|   Order       |          | OrderDetail   |
+---------------+          +---------------+
| - id: Long    |          | - id: Long    |
| - customer: Customer |   | - order: Order|
| - orderDate: LocalDate| | - product: Product|
| - totalAmount: Double|   | - quantity: Integer|
+---------------+          +---------------+
       ^
       |
+---------------+
|OrderRepository|
+---------------+
| + save()      |
| + findById()  |
| + findAll()   |
+---------------+
       ^
       |
+---------------+
|OrderService   |
+---------------+
| + placeOrder()|
| + getOrders() |
+---------------+
```

## 4. クラスの詳細

### Customer
- 説明: 顧客情報を管理するクラス
- 属性:
  - id: Long - 顧客ID
  - name: String - 顧客名
  - email: String - 顧客メールアドレス
  - address: String - 顧客住所
  - phone: String - 顧客電話番号
- 操作:
  - getId(): Long - 顧客IDを取得する
  - getName(): String - 顧客名を取得する
  - getEmail(): String - メールアドレスを取得する
  - getAddress(): String - 住所を取得する
  - getPhone(): String - 電話番号を取得する

### Product
- 説明: 商品情報を管理するクラス
- 属性:
  - id: Long - 商品ID
  - name: String - 商品名
  - description: String - 商品説明
  - price: Double - 商品価格
  - stock: Integer - 在庫数
- 操作:
  - getId(): Long - 商品IDを取得する
  - getName(): String - 商品名を取得する
  - getDescription(): String - 商品説明を取得する
  - getPrice(): Double - 商品価格を取得する
  - getStock(): Integer - 在庫数を取得する
  - updateStock(int amount): void - 在庫数を更新する

### Order
- 説明: 注文情報を管理するクラス
- 属性:
  - id: Long - 注文ID
  - customer: Customer - 注文した顧客
  - orderDate: LocalDate - 注文日
  - totalAmount: Double - 注文総額
- 操作:
  - getId(): Long - 注文IDを取得する
  - getCustomer(): Customer - 注文した顧客を取得する
  - getOrderDate(): LocalDate - 注文日を取得する
  - getTotalAmount(): Double - 注文総額を取得する

### OrderDetail
- 説明: 注文詳細を管理するクラス
- 属性:
  - id: Long - 注文詳細ID
  - order: Order - 注文情報
  - product: Product - 注文された商品
  - quantity: Integer - 注文数量
- 操作:
  - getId(): Long - 注文詳細IDを取得する
  - getOrder(): Order - 注文情報を取得する
  - getProduct(): Product - 注文された商品を取得する
  - getQuantity(): Integer - 注文数量を取得する

### OrderRepository
- 説明: 注文情報の永続化を担当するリポジトリクラス
- 操作:
  - save(Order order): Order - 注文情報を保存する
  - findById(Long id): Optional<Order> - 注文IDから注文情報を取得する
  - findAll(): List<Order> - 全ての注文情報を取得する

### OrderService
- 説明: 注文管理に関する業務ロジックを担当するサービスクラス
- 操作:
  - placeOrder(Customer customer, List<OrderDetail> orderDetails): Order - 注文を受け付ける
  - getOrders(): List<Order> - 全ての注文情報を取得する

## 5. ユースケース

1. 顧客情報の管理
   - 顧客の登録
   - 顧客情報の参照
   - 顧客情報の更新

2. 商品情報の管理
   - 商品の登録
   - 商品情報の参照
   - 商品在庫の管理

3. 注文の管理
   - 注文の受付
   - 注文履歴の参照
   - 注文詳細の参照

## 6. シーケンス図

### 注文の受付
```
+---------------+  +---------------+  +---------------+  +---------------+
|   Customer    |  |   OrderService|  |   OrderRepository|  |   ProductService|
+---------------+  +---------------+  +---------------+  +---------------+
       |                   |                   |                   |
       | placeOrder()      |                   |                   |
       |------------------>|                   |                   |
       |                   | save(order)       |                   |
       |                   |------------------>|                   |
       |                   |                   | updateStock()     |
       |                   |                   |------------------>|
       |                   | return order      |                   |
       |<------------------|                   |                   |
       | return order      |                   |                   |
       |<------------------|                   |                   |
       |                   |                   |                   |
```

### 注文履歴の参照
```
+---------------+  +---------------+  +---------------+
|   Customer    |  |   OrderService|  |OrderRepository|
+---------------+  +---------------+  +---------------+
       |                   |                   |
       | getOrders()       |                   |
       |------------------>|                   |
       |                   | findAll()         |
       |                   |------------------>|
       |                   | return orders     |
       |<------------------|                   |
       | return orders     |                   |
       |<------------------|                   |
       |                   |                   |
```