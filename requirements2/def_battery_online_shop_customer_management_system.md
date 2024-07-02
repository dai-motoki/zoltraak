# 電池のネットショップ顧客管理システムの要件定義書

## 1. 目的
本システムは、電池のネットショップにおける顧客管理を効率化することを目的とする。顧客の登録、注文履歴の管理、在庫管理などの機能を提供することで、ショップの運営を支援する。

## 2. ファイル・フォルダ構成
```
- src/
  - main/
    - java/
      - com/
        - example/
          - batteryshop/
            - controller/
              - CustomerController.java
              - OrderController.java
              - InventoryController.java
            - model/
              - Customer.java
              - Order.java
              - Product.java
              - Inventory.java
            - repository/
              - CustomerRepository.java
              - OrderRepository.java
              - InventoryRepository.java
            - service/
              - CustomerService.java
              - OrderService.java
              - InventoryService.java
            - BatteryShopApplication.java
    - resources/
      - application.properties
  - test/
    - java/
      - com/
        - example/
          - batteryshop/
            - controller/
              - CustomerControllerTest.java
              - OrderControllerTest.java
              - InventoryControllerTest.java
            - service/
              - CustomerServiceTest.java
              - OrderServiceTest.java
              - InventoryServiceTest.java
```

## 3. クラス図
```
+---------------+          +---------------+
|   Customer    |          |    Product    |
+---------------+          +---------------+
| - id: Long    |          | - id: Long    |
| - name: String|          | - name: String|
| - email: String|          | - price: Double|
| - address: String|       | - description: String|
+---------------+          +---------------+
       |                           |
       |                           |
+---------------+          +---------------+
|    Order      |          |   Inventory   |
+---------------+          +---------------+
| - id: Long    |          | - id: Long    |
| - customerId: Long|      | - productId: Long|
| - productId: Long|       | - quantity: Integer|
| - orderDate: Date|       +---------------+
| - status: OrderStatus|
+---------------+
       |
       |
+---------------+
|OrderRepository|
+---------------+
| - save(Order) |
| - findById(id)|
| - findAll()   |
+---------------+
       |
       |
+---------------+
|OrderService   |
+---------------+
| - placeOrder(Customer, Product)|
| - getOrderHistory(Customer)   |
| - updateOrderStatus(Order)    |
+---------------+
```

## 4. クラスの詳細
### Customer
- **説明**: 顧客を表すクラス
- **属性**:
  - `id: Long` - 顧客ID
  - `name: String` - 顧客名
  - `email: String` - 顧客メールアドレス
  - `address: String` - 顧客住所
- **操作**:
  - `getOrders(): List<Order>` - 顧客の注文履歴を取得する
  - `updateProfile(String name, String email, String address)` - 顧客情報を更新する

### Product
- **説明**: 電池製品を表すクラス
- **属性**:
  - `id: Long` - 製品ID
  - `name: String` - 製品名
  - `price: Double` - 製品価格
  - `description: String` - 製品説明
- **操作**:
  - `getInventory(): Inventory` - 製品の在庫情報を取得する

### Order
- **説明**: 注文を表すクラス
- **属性**:
  - `id: Long` - 注文ID
  - `customerId: Long` - 注文者のCustomerID
  - `productId: Long` - 注文された製品のProductID
  - `orderDate: Date` - 注文日
  - `status: OrderStatus` - 注文ステータス
- **操作**:
  - `getCustomer(): Customer` - 注文者の顧客情報を取得する
  - `getProduct(): Product` - 注文された製品情報を取得する
  - `updateStatus(OrderStatus status)` - 注文ステータスを更新する

### Inventory
- **説明**: 在庫を表すクラス
- **属性**:
  - `id: Long` - 在庫ID
  - `productId: Long` - 在庫製品のProductID
  - `quantity: Integer` - 在庫数
- **操作**:
  - `updateQuantity(int quantity)` - 在庫数を更新する
  - `getProduct(): Product` - 在庫製品の情報を取得する

## 5. ユースケース
1. **顧客管理**
   - 顧客の登録/更新/削除
   - 顧客の注文履歴の確認
2. **注文管理**
   - 新規注文の作成
   - 注文ステータスの更新
   - 注文履歴の確認
3. **在庫管理**
   - 在庫数の確認
   - 在庫数の更新

## 6. シーケンス図
### 新規注文作成
```
+---------------+  +---------------+  +---------------+  +---------------+
| CustomerController| OrderController| OrderService   | OrderRepository|
+---------------+  +---------------+  +---------------+  +---------------+
       |                   |                 |                   |
       | placeOrder(customer, product)       |                   |
       |----------------------------->       |                   |
       |                   |                 | createOrder(customer, product)|
       |                   |                 |-------------------->|
       |                   |                 |                   | save(order)
       |                   |                 |<--------------------|
       |                   |                 |                   |
       |                   | 返却値          |                   |
       |<-----------------------------|       |                   |
       |                   |                 |                   |
```

### 注文ステータス更新
```
+---------------+  +---------------+  +---------------+  +---------------+
| OrderController| OrderService   | Order          | OrderRepository|
+---------------+  +---------------+  +---------------+  +---------------+
       |                   |                 |                   |
       | updateOrderStatus(order, status)    |                   |
       |----------------------------->       |                   |
       |                   | updateStatus(status)|               |
       |                   |---------------->|                   |
       |                   |                 |                   | save(order)
       |                   |<----------------|                   |
       |                   |                 |                   |
       |                   | 返却値          |                   |
       |<-----------------------------|       |                   |
       |                   |                 |                   |
```