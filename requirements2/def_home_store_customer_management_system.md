# 家のネットショップ顧客管理システム 要件定義書

## 1. 目的
本システムは、家のネットショップの顧客管理を効率的に行うことを目的とする。顧客情報の管理、注文履歴の管理、商品在庫の管理などの機能を提供し、ネットショップの運営を支援する。

## 2. ファイル・フォルダ構成
```
/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── Customer.java
│   │   │           ├── Order.java
│   │   │           ├── Product.java
│   │   │           ├── Inventory.java
│   │   │           └── ShopManager.java
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── example/
│       │           ├── CustomerTest.java
│       │           ├── OrderTest.java
│       │           ├── ProductTest.java
│       │           ├── InventoryTest.java
│       │           └── ShopManagerTest.java
│       └── resources/
├── build.gradle
└── README.md
```

## 3. クラス図
```
+--------------+       +-------------+
|    Customer  |       |   Product   |
+--------------+       +-------------+
| - id: int    |       | - id: int   |
| - name: String|       | - name: String|
| - email: String|       | - description: String|
| - address: String|    | - price: double|
| - phone: String|       +-------------+
| + getOrders(): List<Order>|
| + updateProfile()|
| + placeOrder(Product)|
+--------------+       +-------------+
                       |  Inventory  |
                       +-------------+
                       | - id: int   |
                       | - product: Product|
                       | - quantity: int|
                       | + updateQuantity(int)|
                       | + checkAvailability(Product): boolean|
                       +-------------+

+---------------+
|   Order       |
+---------------+
| - id: int     |
| - customer: Customer|
| - product: Product|
| - quantity: int|
| - orderDate: LocalDate|
| - status: OrderStatus|
| + updateStatus(OrderStatus)|
+---------------+

+---------------+
|  ShopManager  |
+---------------+
| - customers: List<Customer>|
| - orders: List<Order>|
| - inventory: List<Inventory>|
| + addCustomer(Customer)|
| + removeCustomer(Customer)|
| + placeOrder(Order)|
| + updateInventory(Inventory)|
| + generateReports()|
+---------------+
```

## 4. クラスの詳細
### Customer
- **説明**: 顧客を表すクラス
- **属性**:
  - `id: int` - 顧客ID
  - `name: String` - 顧客名
  - `email: String` - 顧客メールアドレス
  - `address: String` - 顧客住所
  - `phone: String` - 顧客電話番号
- **操作**:
  - `getOrders(): List<Order>` - 顧客の注文履歴を取得する
  - `updateProfile()` - 顧客情報を更新する
  - `placeOrder(Product)` - 商品を注文する

### Product
- **説明**: 商品を表すクラス
- **属性**:
  - `id: int` - 商品ID
  - `name: String` - 商品名
  - `description: String` - 商品説明
  - `price: double` - 商品価格

### Inventory
- **説明**: 在庫を表すクラス
- **属性**:
  - `id: int` - 在庫ID
  - `product: Product` - 在庫の商品
  - `quantity: int` - 在庫数
- **操作**:
  - `updateQuantity(int)` - 在庫数を更新する
  - `checkAvailability(Product): boolean` - 商品の在庫が利用可能かを確認する

### Order
- **説明**: 注文を表すクラス
- **属性**:
  - `id: int` - 注文ID
  - `customer: Customer` - 注文した顧客
  - `product: Product` - 注文された商品
  - `quantity: int` - 注文数
  - `orderDate: LocalDate` - 注文日
  - `status: OrderStatus` - 注文ステータス
- **操作**:
  - `updateStatus(OrderStatus)` - 注文ステータスを更新する

### ShopManager
- **説明**: ネットショップ全体を管理するクラス
- **属性**:
  - `customers: List<Customer>` - 登録された顧客一覧
  - `orders: List<Order>` - 受けた注文一覧
  - `inventory: List<Inventory>` - 在庫一覧
- **操作**:
  - `addCustomer(Customer)` - 新規顧客を追加する
  - `removeCustomer(Customer)` - 顧客を削除する
  - `placeOrder(Order)` - 注文を受け付ける
  - `updateInventory(Inventory)` - 在庫情報を更新する
  - `generateReports()` - 各種レポートを生成する

## 5. ユースケース
1. 顧客管理
   - 顧客の新規登録
   - 顧客情報の更新
   - 顧客の削除
2. 注文管理
   - 注文の受付
   - 注文ステータスの更新
   - 注文履歴の参照
3. 在庫管理
   - 在庫数の更新
   - 商品の在庫状況の確認
4. レポート生成
   - 顧客レポートの生成
   - 注文レポートの生成
   - 在庫レポートの生成

## 6. シーケンス図
### 新規顧客登録
```
+---------------+     +---------------+
|   ShopManager |     |    Customer   |
+---------------+     +---------------+
        |                     |
        | createCustomer(name, email, address, phone)|
        |----------------------------->|
        |                     | new Customer(name, email, address, phone)|
        |                     |----------------------------->|
        |                     |         customer             |
        |<-----------------------------|
        | addCustomer(customer)|
        |----------------------------->|
        |                     |
        |                     |
```

### 注文の受付
```
+---------------+     +---------------+     +-------------+
|   ShopManager |     |    Customer   |     |   Product   |
+---------------+     +---------------+     +-------------+
        |                     |                     |
        | placeOrder(customer, product, quantity)  |
        |----------------------------->|             |
        |                     | new Order(customer, product, quantity)|
        |                     |----------------------------->|
        |                     |         order         |
        |<-----------------------------|             |
        | checkAvailability(product)   |             |
        |----------------------------->|             |
        |                     |                     | checkAvailability(): boolean|
        |                     |                     |----------------------------->|
        |                     |                     |         true/false          |
        |                     |                     |<-----------------------------|
        | updateInventory(order.product, order.quantity)|
        |----------------------------->|             |
        |                     |                     |
        |                     |                     |
```

### 在庫状況確認
```
+---------------+     +-------------+
|   ShopManager |     |  Inventory  |
+---------------+     +-------------+
        |                     |
        | checkAvailability(product)|
        |----------------------------->|
        |                     | checkAvailability(product): boolean|
        |                     |----------------------------->|
        |                     |         true/false          |
        |                     |<-----------------------------|
        |                     |                             |
        |                     |                             |
```