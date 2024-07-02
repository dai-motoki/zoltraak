# 紅茶のネットショップ顧客管理システム

## 1. 目的
このシステムの目的は、紅茶の販売店がオンラインショップ上で顧客管理を行い、効率的な販売活動を行うことです。顧客の情報管理、注文の管理、商品の在庫管理などの機能を提供することで、店舗の業務を支援します。

## 2. ファイル・フォルダ構成
```
紅茶のネットショップ顧客管理システム/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── entity/
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
│   │   │           └── web/
│   │   │               ├── controller/
│   │   │               │   ├── CustomerController.java
│   │   │               │   ├── OrderController.java
│   │   │               │   └── ProductController.java
│   │   │               └── dto/
│   │   │                   ├── CustomerDTO.java
│   │   │                   ├── OrderDTO.java
│   │   │                   └── ProductDTO.java
│   │   └── resources/
│   └── test/
│       └── java/
│           └── com/
│               └── example/
│                   ├── repository/
│                   │   ├── CustomerRepositoryTest.java
│                   │   ├── OrderRepositoryTest.java
│                   │   └── ProductRepositoryTest.java
│                   └── service/
│                       ├── CustomerServiceTest.java
│                       ├── OrderServiceTest.java
│                       └── ProductServiceTest.java
└── pom.xml
```

## 3. クラス図
```
+----------------+        +---------------+
|    Customer    |        |   ShoppingCart|
+----------------+        +---------------+
| - id: int      |        | - id: int     |
| - name: String |        | - customerId: int|
| - email: String|        | - products: List<Product>|
| - address: String|      | + addProduct(product: Product)|
| + getOrders(): List<Order>|+ removeProduct(product: Product)|
| + addOrder(order: Order)| + getTotalPrice(): double |
+----------------+        +---------------+
       ^                           ^
       |                           |
+----------------+        +---------------+
|     Order      |        |    Product    |
+----------------+        +---------------+
| - id: int      |        | - id: int     |
| - customerId: int|      | - name: String|
| - productIds: List<int>|| - description: String|
| - totalPrice: double|   | - price: double|
| - status: OrderStatus| + getDetails(): String|
| + calculateTotal()|     +---------------+
+----------------+
       ^
       |
+----------------+
| OrderRepository|
+----------------+
| + save(order: Order)|
| + findById(id: int): Order|
| + findByCustomerId(customerId: int): List<Order>|
+----------------+
```

## 4. クラスの詳細
### Customer
- 説明: 顧客を表すクラス
- 属性:
  - id: int - 顧客ID
  - name: String - 顧客名
  - email: String - メールアドレス
  - address: String - 住所
- 操作:
  - getOrders(): List<Order> - 顧客の注文履歴を取得する
  - addOrder(order: Order) - 新しい注文を追加する

### ShoppingCart
- 説明: 買い物カゴを表すクラス
- 属性:
  - id: int - 買い物カゴID
  - customerId: int - 顧客ID
  - products: List<Product> - 買い物カゴに入っている商品のリスト
- 操作:
  - addProduct(product: Product) - 商品を買い物カゴに追加する
  - removeProduct(product: Product) - 商品を買い物カゴから削除する
  - getTotalPrice(): double - 買い物カゴの合計金額を取得する

### Order
- 説明: 注文を表すクラス
- 属性:
  - id: int - 注文ID
  - customerId: int - 顧客ID
  - productIds: List<int> - 注文した商品のID
  - totalPrice: double - 注文の合計金額
  - status: OrderStatus - 注文の状況
- 操作:
  - calculateTotal() - 注文の合計金額を計算する

### Product
- 説明: 商品を表すクラス
- 属性:
  - id: int - 商品ID
  - name: String - 商品名
  - description: String - 商品説明
  - price: double - 価格
- 操作:
  - getDetails(): String - 商品の詳細情報を取得する

### OrderRepository
- 説明: 注文情報を管理するリポジトリ
- 操作:
  - save(order: Order) - 注文情報を保存する
  - findById(id: int): Order - 注文IDから注文情報を取得する
  - findByCustomerId(customerId: int): List<Order> - 顧客IDから注文履歴を取得する

## 5. ユースケース
1. 顧客の登録と管理
   - 関連クラス: Customer, CustomerRepository, CustomerService, CustomerController
   - 主要メソッド: createCustomer(), updateCustomer(), deleteCustomer(), getCustomerOrders()

2. 商品の管理
   - 関連クラス: Product, ProductRepository, ProductService, ProductController
   - 主要メソッド: createProduct(), updateProduct(), deleteProduct(), getProductDetails()

3. 注文の管理
   - 関連クラス: Order, ShoppingCart, OrderRepository, OrderService, OrderController
   - 主要メソッド: placeOrder(), cancelOrder(), getOrderHistory()

4. ショッピングカートの管理
   - 関連クラス: ShoppingCart, Customer, Product
   - 主要メソッド: addToCart(), removeFromCart(), calculateTotal()

## 6. シーケンス図
### 顧客の新規登録
```
+---------------+   +---------------+   +---------------+
| CustomerController|   | CustomerService|   | CustomerRepository|
+---------------+   +---------------+   +---------------+
       |                     |                     |
       | createCustomer(dto) |                     |
       |-------------------->|                     |
       |                     | saveCustomer(customer)|
       |                     |-------------------->|
       |                     |                     | save(customer)
       |                     |                     |-------------------->
       |                     |<--------------------|
       | return customer     |                     |
       |<-------------------|                     |
       |                     |                     |
```

### 注文の作成
```
+---------------+   +---------------+   +---------------+   +---------------+   +---------------+
| OrderController|   |   OrderService|   |   OrderRepository|   | ShoppingCartService|   |   ProductService|
+---------------+   +---------------+   +---------------+   +---------------+   +---------------+
       |                     |                     |                     |                     |
       | placeOrder(dto)     |                     |                     |                     |
       |-------------------->|                     |                     |                     |
       |                     | getShoppingCart(customerId)|              |                     |
       |                     |-------------------->|                     |                     |
       |                     |                     | findByCustomerId(customerId)|             |
       |                     |                     |-------------------->|                     |
       |                     |                     |<--------------------|                     |
       |                     | calculateTotal()    |                     |                     |
       |                     |-------------------->|                     |                     |
       |                     |                     |                     | getProductPrices(productIds)|
       |                     |                     |                     |-------------------->|
       |                     |                     |                     |<--------------------|
       |                     | createOrder(order)  |                     |                     |
       |                     |-------------------->|                     |                     |
       |                     |                     | save(order)         |                     |
       |                     |                     |-------------------->|                     |
       |                     |<--------------------|                     |                     |
       | return order        |                     |                     |                     |
       |<-------------------|                     |                     |                     |
```