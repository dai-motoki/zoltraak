# 時計販売会社の顧客管理システム

## 1. 目的
本システムは、時計を販売する会社の顧客管理を支援するものである。顧客情報の管理、商品の管理、注文処理、顧客への通知など、時計販売会社の業務を効率的に行うことを目的とする。

## 2. ファイル・フォルダ構成
```
root/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── company/
│   │   │           ├── Customer.java
│   │   │           ├── Order.java
│   │   │           ├── Product.java
│   │   │           ├── ProductCatalog.java
│   │   │           ├── PurchaseHistory.java
│   │   │           └── SystemController.java
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── company/
│       │           ├── CustomerTest.java
│       │           ├── OrderTest.java
│       │           ├── ProductTest.java
│       │           ├── ProductCatalogTest.java
│       │           ├── PurchaseHistoryTest.java
│       │           └── SystemControllerTest.java
│       └── resources/
├── docs/
│   ├── class_diagram.md
│   ├── use_cases.md
│   └── sequence_diagrams/
│       ├── manage_customer.md
│       ├── place_order.md
│       └── view_purchase_history.md
├── build/
│   ├── classes/
│   │   ├── main/
│   │   │   └── com/
│   │   │       └── company/
│   │   │           ├── Customer.class                                       # 顧客クラスのコンパイル済みファイル
│   │   │           ├── Order.class                                          # 注文クラスのコンパイル済みファイル
│   │   │           ├── Product.class                                        # 商品クラスのコンパイル済みファイル
│   │   │           ├── ProductCatalog.class                                 # 商品カタログクラスのコンパイル済みファイル
│   │   │           ├── PurchaseHistory.class                                # 購入履歴クラスのコンパイル済みファイル
│   │   │           └── SystemController.class                               # システムコントローラークラスのコンパイル済みファイル
│   │   └── test/                                                            # テストコードのディレクトリ
│   │       └── com/                                                         # - comパッケージのディレクトリ
│   │           └── company/                                                 # -- companyパッケージのディレクトリ
│   │               ├── CustomerTest.class                                   # --- 顧客クラスのテストコードのコンパイル済みファイル
│   │               ├── OrderTest.class                                      # --- 注文クラスのテストコードのコンパイル済みファイル
│   │               ├── ProductTest.class                                    # --- 商品クラスのテストコードのコンパイル済みファイル
│   │               ├── ProductCatalogTest.class                             # --- 商品カタログクラスのテストコードのコンパイル済みファイル
│   │               ├── PurchaseHistoryTest.class                            # --- 購入履歴クラスのテストコードのコンパイル済みファイル
│   │               └── SystemControllerTest.class                           # --- システムコントローラークラスのテストコードのコンパイル済みファイル
│   └── libs/                                                                # ライブラリのディレクトリ
│       └── junit-4.13.2.jar
└── README.md
```

## 3. クラス図
```
+----------------+        +---------------+
|   Customer     |        |   Product     |
+----------------+        +---------------+
| - id: String   |        | - id: String  |
| - name: String |        | - name: String|
| - email: String|        | - price: int  |
| - phone: String|        | - stock: int  |
+----------------+        +---------------+
       ^                           ^
       |                           |
+----------------+        +---------------+
|   PurchaseHistory|        |ProductCatalog|
+----------------+        +---------------+
| - customerId: String|    | - products: Map<String, Product>|
| - orders: List<Order>|   +---------------+
+----------------+        
       ^
       |
+----------------+
|     Order      |
+----------------+
| - id: String   |
| - customerId: String|
| - productId: String|
| - quantity: int |
| - orderDate: Date|
+----------------+
       ^
       |
+----------------+
| SystemController|
+----------------+
| + addCustomer(Customer): void|
| + placeOrder(Order): void    |
| + viewPurchaseHistory(String): PurchaseHistory|
+----------------+
```

## 4. クラスの詳細
### Customer
- **説明**: 顧客を表すクラス
- **属性**:
  - `id: String` - 顧客ID
  - `name: String` - 顧客名
  - `email: String` - 顧客メールアドレス
  - `phone: String` - 顧客電話番号
- **操作**:
  - `getCustomerId(): String` - 顧客IDを取得する
  - `getName(): String` - 顧客名を取得する
  - `getEmail(): String` - 顧客メールアドレスを取得する
  - `getPhone(): String` - 顧客電話番号を取得する

### Product
- **説明**: 商品を表すクラス
- **属性**:
  - `id: String` - 商品ID
  - `name: String` - 商品名
  - `price: int` - 商品価格
  - `stock: int` - 在庫数
- **操作**:
  - `getProductId(): String` - 商品IDを取得する
  - `getName(): String` - 商品名を取得する
  - `getPrice(): int` - 商品価格を取得する
  - `getStock(): int` - 在庫数を取得する
  - `updateStock(int): void` - 在庫数を更新する

### Order
- **説明**: 注文を表すクラス
- **属性**:
  - `id: String` - 注文ID
  - `customerId: String` - 注文者のCustomerID
  - `productId: String` - 注文された商品のProductID
  - `quantity: int` - 注文数
  - `orderDate: Date` - 注文日
- **操作**:
  - `getOrderId(): String` - 注文IDを取得する
  - `getCustomerId(): String` - 注文者のCustomerIDを取得する
  - `getProductId(): String` - 注文された商品のProductIDを取得する
  - `getQuantity(): int` - 注文数を取得する
  - `getOrderDate(): Date` - 注文日を取得する

### PurchaseHistory
- **説明**: 顧客の購買履歴を表すクラス
- **属性**:
  - `customerId: String` - 顧客ID
  - `orders: List<Order>` - 注文履歴
- **操作**:
  - `getCustomerId(): String` - 顧客IDを取得する
  - `getOrders(): List<Order>` - 注文履歴を取得する
  - `addOrder(Order): void` - 注文を履歴に追加する

### ProductCatalog
- **説明**: 商品カタログを表すクラス
- **属性**:
  - `products: Map<String, Product>` - 商品の辞書
- **操作**:
  - `getProduct(String): Product` - 商品IDから商品を取得する
  - `addProduct(Product): void` - 商品を追加する
  - `updateProduct(Product): void` - 商品を更新する

### SystemController
- **説明**: システムの処理を制御するクラス
- **操作**:
  - `addCustomer(Customer): void` - 顧客を追加する
  - `placeOrder(Order): void` - 注文を処理する
  - `viewPurchaseHistory(String): PurchaseHistory` - 顧客の購買履歴を表示する

## 5. ユースケース
1. 顧客の管理
   - 顧客の追加
   - 顧客情報の表示
2. 注文の処理
   - 注文の作成
   - 注文の履歴表示
3. 商品の管理
   - 商品の追加
   - 商品の在庫管理

## 6. シーケンス図
### 顧客の追加
```
+----------------+    +---------------+    +----------------+
|   Customer     |    |SystemController|    |PurchaseHistory |
+----------------+    +---------------+    +----------------+
| createCustomer() |   |   addCustomer()  |   |                |
|---------------->|   |----------------->|   |                |
|                 |   |                 |   |                |
|                 |   |                 |   |                |
|                 |   |                 |   |                |
+----------------+    +---------------+    +----------------+
```

### 注文の作成
```
+----------------+    +---------------+    +----------------+    +---------------+
|     Order      |    |SystemController|    |ProductCatalog  |    |PurchaseHistory|
+----------------+    +---------------+    +----------------+    +---------------+
| createOrder()  |   |   placeOrder()  |   |  getProduct()  |   |  addOrder()   |
|---------------->|   |---------------->|   |--------------->|   |--------------->|
|                 |   |                 |   |                |   |                |
|                 |   |                 |   |                |   |                |
|                 |   |                 |   |                |   |                |
+----------------+    +---------------+    +----------------+    +---------------+
```

### 購買履歴の表示
```
+----------------+    +---------------+    +----------------+
|PurchaseHistory |    |SystemController|    |     Customer   |
+----------------+    +---------------+    +----------------+
|viewHistory()   |   |viewPurchaseHistory()|   |               |
|---------------->|   |----------------->|   |               |
|                 |   |                 |   |               |
|                 |   |                 |   |               |
|                 |   |                 |   |               |
+----------------+    +---------------+    +----------------+
```