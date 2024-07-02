# カレーのネットショップ顧客管理システム

## 1. 目的
本システムは、カレーのオンラインショップの顧客管理を行うことを目的としています。顧客の情報管理、注文管理、商品管理などの機能を備え、カレーショップの運営を効率的に行うことができます。

## 2. ファイル・フォルダ構成
```
root/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── curryshoppe/
│   │   │           ├── model/
│   │   │           │   ├── Customer.java
│   │   │           │   ├── Order.java
│   │   │           │   ├── Product.java
│   │   │           │   └── ShoppingCart.java
│   │   │           ├── repository/
│   │   │           │   ├── CustomerRepository.java
│   │   │           │   ├── OrderRepository.java
│   │   │           │   └── ProductRepository.java
│   │   │           ├── service/
│   │   │           │   ├── CustomerService.java
│   │   │           │   ├── OrderService.java
│   │   │           │   └── ProductService.java
│   │   │           └── CurryShoppe.java
│   │   └── resources/
│   └── test/
│       └── java/
│           └── com/
│               └── curryshoppe/
│                   ├── model/
│                   ├── repository/
│                   ├── service/
│                   └── CurryShoppeTest.java
└── pom.xml
```

## 3. クラス図
```
+---------------+        +---------------+
|   Customer    |        |    Product    |
+---------------+        +---------------+
| - id: int     |        | - id: int     |
| - name: String|        | - name: String|
| - email: String|        | - description: String|
| - address: String|     | - price: double|
+---------------+        +---------------+
       ^                         ^
       |                         |
+---------------+        +---------------+
|    Order      |        | ShoppingCart  |
+---------------+        +---------------+
| - id: int     |        | - id: int     |
| - customer: Customer | | - customer: Customer|
| - products: List<Product>| - items: List<Product>|
| - totalAmount: double|        +---------------+
+---------------+                     ^
       ^                             |
+---------------+        +---------------+
|CustomerService|        |ProductService |
+---------------+        +---------------+
| + createCustomer()     | + createProduct()|
| + updateCustomer()     | + updateProduct()|
| + getCustomer()        | + getProduct()   |
+---------------+        +---------------+
       ^                         ^
       |                         |
+---------------+        +---------------+
|  OrderService |        |CustomerRepository|
+---------------+        +---------------+
| + createOrder()        | + saveCustomer()|
| + updateOrder()        | + getCustomer() |
| + getOrder()           +---------------+
+---------------+                ^
       ^                         |
+---------------+        +---------------+
|ProductRepository|        |OrderRepository|
+---------------+        +---------------+
| + saveProduct() |        | + saveOrder() |
| + getProduct()  |        | + getOrder()  |
+---------------+        +---------------+
```

## 4. クラスの詳細

### Customer
- **説明**: 顧客情報を表すクラス
- **属性**:
  - id: int - 顧客ID
  - name: String - 顧客名
  - email: String - 顧客のメールアドレス
  - address: String - 顧客の住所
- **操作**:
  - なし

### Product
- **説明**: 商品情報を表すクラス
- **属性**:
  - id: int - 商品ID
  - name: String - 商品名
  - description: String - 商品の説明
  - price: double - 商品価格
- **操作**:
  - なし

### Order
- **説明**: 注文情報を表すクラス
- **属性**:
  - id: int - 注文ID
  - customer: Customer - 注文した顧客
  - products: List<Product> - 注文された商品のリスト
  - totalAmount: double - 注文の合計金額
- **操作**:
  - なし

### ShoppingCart
- **説明**: ショッピングカートを表すクラス
- **属性**:
  - id: int - ショッピングカートID
  - customer: Customer - ショッピングカートの所有者
  - items: List<Product> - カートに入っている商品のリスト
- **操作**:
  - addItem(Product): void - 商品をカートに追加する
  - removeItem(Product): void - 商品をカートから削除する
  - getTotal(): double - カート内の商品の合計金額を取得する

### CustomerService
- **説明**: 顧客管理に関するサービスクラス
- **操作**:
  - createCustomer(Customer): void - 新しい顧客を作成する
  - updateCustomer(Customer): void - 顧客情報を更新する
  - getCustomer(int): Customer - 顧客IDから顧客情報を取得する

### ProductService
- **説明**: 商品管理に関するサービスクラス
- **操作**:
  - createProduct(Product): void - 新しい商品を作成する
  - updateProduct(Product): void - 商品情報を更新する
  - getProduct(int): Product - 商品IDから商品情報を取得する

### OrderService
- **説明**: 注文管理に関するサービスクラス
- **操作**:
  - createOrder(Order): void - 新しい注文を作成する
  - updateOrder(Order): void - 注文情報を更新する
  - getOrder(int): Order - 注文IDから注文情報を取得する

### CustomerRepository
- **説明**: 顧客情報の永続化を担当するリポジトリクラス
- **操作**:
  - saveCustomer(Customer): void - 顧客情報を保存する
  - getCustomer(int): Customer - 顧客IDから顧客情報を取得する

### ProductRepository
- **説明**: 商品情報の永続化を担当するリポジトリクラス
- **操作**:
  - saveProduct(Product): void - 商品情報を保存する
  - getProduct(int): Product - 商品IDから商品情報を取得する

### OrderRepository
- **説明**: 注文情報の永続化を担当するリポジトリクラス
- **操作**:
  - saveOrder(Order): void - 注文情報を保存する
  - getOrder(int): Order - 注文IDから注文情報を取得する

## 5. ユースケース

1. 顧客の登録
   - 関連クラス: Customer, CustomerService, CustomerRepository
   - 関連メソッド: CustomerService.createCustomer(), CustomerRepository.saveCustomer()

2. 商品の登録
   - 関連クラス: Product, ProductService, ProductRepository
   - 関連メソッド: ProductService.createProduct(), ProductRepository.saveProduct()

3. 注文の作成
   - 関連クラス: Order, ShoppingCart, OrderService, OrderRepository, CustomerRepository, ProductRepository
   - 関連メソッド: ShoppingCart.addItem(), ShoppingCart.getTotal(), OrderService.createOrder(), OrderRepository.saveOrder()

4. 注文の更新
   - 関連クラス: Order, OrderService, OrderRepository
   - 関連メソッド: OrderService.updateOrder(), OrderRepository.saveOrder()

5. 顧客情報の更新
   - 関連クラス: Customer, CustomerService, CustomerRepository
   - 関連メソッド: CustomerService.updateCustomer(), CustomerRepository.saveCustomer()

6. 商品情報の更新
   - 関連クラス: Product, ProductService, ProductRepository
   - 関連メソッド: ProductService.updateProduct(), ProductRepository.saveProduct()

7. 顧客情報の参照
   - 関連クラス: Customer, CustomerService, CustomerRepository
   - 関連メソッド: CustomerService.getCustomer(), CustomerRepository.getCustomer()

8. 商品情報の参照
   - 関連クラス: Product, ProductService, ProductRepository
   - 関連メソッド: ProductService.getProduct(), ProductRepository.getProduct()

9. 注文情報の参照
   - 関連クラス: Order, OrderService, OrderRepository
   - 関連メソッド: OrderService.getOrder(), OrderRepository.getOrder()

## 6. シーケンス図

### 1. 顧客の登録
```
+---------------+    +----------------+    +------------------+
|   CurryShoppe  |    |CustomerService|    |CustomerRepository|
+---------------+    +----------------+    +------------------+
     createCustomer()      createCustomer()        saveCustomer()
           |                     |                       |
           |-------------------->|                       |
           |                     |---------------------->|
           |<-------------------|                       |
           |                     |                       |
```

### 2. 注文の作成
```
+---------------+    +---------------+    +---------------+    +---------------+    +---------------+
|   CurryShoppe  |    |ShoppingCart   |    |ProductRepository|    |CustomerRepository|    |OrderRepository|
+---------------+    +---------------+    +---------------+    +---------------+    +---------------+
     createOrder()         addItem()             getProduct()          getCustomer()        saveOrder()
           |                     |                       |                       |                |
           |-------------------->|                       |                       |                |
           |                     |---------------------->|                       |                |
           |                     |<----------------------|                       |                |
           |                     |                       |                       |                |
           |                     |                       |                       |---------------------->
           |<-------------------|                       |                       |                |
           |                     |                       |                       |                |
```

### 3. 注文の更新
```
+---------------+    +---------------+    +---------------+
|   CurryShoppe  |    |OrderService   |    |OrderRepository|
+---------------+    +---------------+    +---------------+
     updateOrder()      updateOrder()        saveOrder()
           |                     |                  |
           |-------------------->|                  |
           |                     |----------------->|
           |<-------------------|                  |
           |                     |                  |
```

システムの詳細な仕様については、[追加の情報]を参照してください。