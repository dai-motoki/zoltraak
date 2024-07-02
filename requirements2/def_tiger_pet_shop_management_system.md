# トラのペットショップ ペットと顧客管理システム

## 1. 目的
このシステムは、トラのペットショップの運営を支援することを目的としています。主な機能は、ペットの在庫管理、顧客情報の管理、注文管理などです。これにより、ペットショップの業務の効率化と、顧客サービスの向上を図ります。

## 2. ファイル・フォルダ構成
```
   ├── model/
   │   ├── Customer.java
   │   ├── Order.java
   │   ├── OrderItem.java
   │   └── Product.java
   ├── controller/
   │   ├── CustomerController.java
   │   ├── OrderController.java
   │   └── ProductController.java
   └── view/
       ├── CustomerView.java
       ├── OrderView.java
       └── ProductView.java
```

## 3. クラス図
```
                        +------------+
                        |  Customer  |
                        +------------+
                        | - id: int   |
                        | - name: String |
                        | - email: String |
                        | - phone: String |
                        | + getCustomerInfo() |
                        | + updateCustomerInfo() |
                        +------------+
                                |
                                | 1..* 
                                |
                        +------------+
                        |   Order    |
                        +------------+
                        | - id: int   |
                        | - customerId: int |
                        | - orderDate: Date |
                        | - totalAmount: double |
                        | + placeOrder() |
                        | + viewOrderDetails() |
                        +------------+
                                |
                                | 1..*
                                |
                        +------------+
                        | OrderItem  |
                        +------------+
                        | - id: int   |
                        | - orderId: int |
                        | - productId: int |
                        | - quantity: int |
                        | - price: double |
                        | + addOrderItem() |
                        | + updateOrderItem() |
                        +------------+
                                |
                                | 1..*
                                |
                        +------------+
                        |  Product   |
                        +------------+
                        | - id: int   |
                        | - name: String |
                        | - description: String |
                        | - price: double |
                        | - quantity: int |
                        | + addProduct() |
                        | + updateProduct() |
                        | + getProductDetails() |
                        +------------+
```

## 4. クラスの詳細

### Customer
- **説明**: 顧客の情報を表すクラス
- **属性**:
  - `id`: 顧客ID (int)
  - `name`: 顧客名 (String)
  - `email`: 顧客メールアドレス (String)
  - `phone`: 顧客電話番号 (String)
- **操作**:
  - `getCustomerInfo()`: 顧客情報を取得する
  - `updateCustomerInfo()`: 顧客情報を更新する

### Order
- **説明**: 注文情報を表すクラス
- **属性**:
  - `id`: 注文ID (int)
  - `customerId`: 注文した顧客ID (int)
  - `orderDate`: 注文日 (Date)
  - `totalAmount`: 注文合計金額 (double)
- **操作**:
  - `placeOrder()`: 注文を行う
  - `viewOrderDetails()`: 注文詳細を表示する

### OrderItem
- **説明**: 注文明細を表すクラス
- **属性**:
  - `id`: 注文明細ID (int)
  - `orderId`: 注文ID (int)
  - `productId`: 商品ID (int)
  - `quantity`: 注文数量 (int)
  - `price`: 単価 (double)
- **操作**:
  - `addOrderItem()`: 注文明細を追加する
  - `updateOrderItem()`: 注文明細を更新する

### Product
- **説明**: 商品情報を表すクラス
- **属性**:
  - `id`: 商品ID (int)
  - `name`: 商品名 (String)
  - `description`: 商品説明 (String)
  - `price`: 価格 (double)
  - `quantity`: 在庫数 (int)
- **操作**:
  - `addProduct()`: 新商品を追加する
  - `updateProduct()`: 商品情報を更新する
  - `getProductDetails()`: 商品詳細を取得する

## 5. ユースケース
主要なユースケースは以下の通りです:

1. 顧客管理
   - 顧客情報の登録/更新/参照
2. 商品管理
   - 商品情報の登録/更新/参照
   - 在庫管理
3. 注文管理
   - 注文の受付
   - 注文明細の管理
   - 注文履歴の参照

## 6. シーケンス図

### 顧客登録
```
+------------+         +------------+
|  Customer  |         |CustomerView|
+------------+         +------------+
     |                       |
     | createCustomer()      |
     |-------------------->  |
     |                       | getCustomerInfo()
     |                       |-------------------->
     |                       |
     |                  +------------+
     |                  |CustomerCtrl|
     |                  +------------+
     |                       |
     |                       | saveCustomer()
     |<--------------------  |
     |                       |
     | getCustomerId()       |
     |-------------------->  |
     |                       |
     | CustomerCreated       |
     |<--------------------  |
     |                       |
```

### 注文登録
```
+------------+         +------------+         +------------+         +------------+
|   Order    |         |  OrderView  |         |OrderController|         |  Product   |
+------------+         +------------+         +------------+         +------------+
     |                       |                       |                       |
     | placeOrder()          |                       |                       |
     |-------------------->  |                       |                       |
     |                       | getCustomerId()        |                       |
     |                       |-------------------->   |                       |
     |                       |                       | getCustomer()         |
     |                       |                       |-------------------->   |
     |                       |                       |                       |
     |                       |                  +------------+              |
     |                       |                  |  OrderItem  |              |
     |                       |                  +------------+              |
     |                       |                       |                       |
     |                       |                       | createOrderItems()    |
     |                       |                       |-------------------->  |
     |                       |                       |                       |
     |                       |                       | saveOrder()          |
     |                       |<--------------------  |                       |
     |                       |                       |                       |
     |                       | OrderPlaced           |                       |
     |<--------------------  |                       |                       |
     |                       |                       |                       |
```

以上が、トラのペットショップのペットと顧客管理システムの要件定義書です。オブジェクト指向の原則に基づいて設計されており、カプセル化、継承、ポリモーフィズムなどの概念が適用されています。また、設計パターンの活用により、柔軟性と拡張性を高めています。