## システムの要件定義書

## ゴール: 適切な要件定義書の作成

### 1. 目的
本システムは、ユーザーが簡単に操作できるWebアプリケーションを提供することを目的とする。ユーザーは、このシステムを通じてさまざまな機能を利用できるようにする。

### 2. ファイル・フォルダ構成
```
.
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com
│   │   │       └── example
│   │   │           ├── controller
│   │   │           ├── model
│   │   │           └── view
│   │   └── resources
│   └── test
│       ├── java
│       │   └── com
│       │       └── example
│       └── resources
├── build.gradle
└── settings.gradle
```

### 3. クラス図
```
+---------------+        +---------------+
|   User        |        |   Product     |
+---------------+        +---------------+
| - userId      |        | - productId   |
| - userName    |        | - productName |
| - email       |        | - description |
| - password    |        | - price       |
+---------------+        +---------------+
     |                          |
     |                          |
+---------------+        +---------------+
|   Cart        |        |   Order       |
+---------------+        +---------------+
| - cartId      |        | - orderId     |
| - userId      |        | - userId      |
| - products    |<>-------|   products   |
+---------------+        +---------------+
     |                          |
     |                          |
+---------------+        +---------------+
|   Payment     |        |   Shipping    |
+---------------+        +---------------+
| - paymentId   |        | - shippingId  |
| - userId      |        | - userId      |
| - amount      |        | - address     |
| - method      |        | - status      |
+---------------+        +---------------+
```

### 4. クラスの詳細

**User**
- 説明: ユーザー情報を管理するクラス
- 属性:
  - userId: ユーザーID (String)
  - userName: ユーザー名 (String)
  - email: メールアドレス (String)
  - password: パスワード (String)
- 操作:
  - registerUser(userName, email, password): ユーザー登録
  - updateUserInfo(userId, userName, email, password): ユーザー情報の更新
  - deleteUser(userId): ユーザー削除

**Product**
- 説明: 商品情報を管理するクラス
- 属性:
  - productId: 商品ID (String)
  - productName: 商品名 (String)
  - description: 商品説明 (String)
  - price: 価格 (double)
- 操作:
  - createProduct(productName, description, price): 商品の新規登録
  - updateProduct(productId, productName, description, price): 商品情報の更新
  - deleteProduct(productId): 商品の削除

**Cart**
- 説明: カート情報を管理するクラス
- 属性:
  - cartId: カートID (String)
  - userId: ユーザーID (String)
  - products: カート内の商品リスト (List<Product>)
- 操作:
  - addToCart(userId, product): 商品をカートに追加
  - removeFromCart(userId, product): カートから商品を削除
  - viewCart(userId): ユーザーのカート内容を表示

**Order**
- 説明: 注文情報を管理するクラス
- 属性:
  - orderId: 注文ID (String)
  - userId: ユーザーID (String)
  - products: 注文商品リスト (List<Product>)
- 操作:
  - placeOrder(userId, products): 注文の作成
  - cancelOrder(orderId): 注文のキャンセル
  - trackOrder(orderId): 注文状況の確認

**Payment**
- 説明: 支払い情報を管理するクラス
- 属性:
  - paymentId: 支払いID (String)
  - userId: ユーザーID (String)
  - amount: 支払い金額 (double)
  - method: 支払い方法 (String)
- 操作:
  - makePayment(userId, amount, method): 支払いの実行
  - viewPaymentHistory(userId): ユーザーの支払い履歴を表示

**Shipping**
- 説明: 配送情報を管理するクラス
- 属性:
  - shippingId: 配送ID (String)
  - userId: ユーザーID (String)
  - address: 配送先住所 (String)
  - status: 配送状況 (String)
- 操作:
  - addShippingAddress(userId, address): 配送先住所の登録
  - updateShippingAddress(shippingId, address): 配送先住所の更新
  - trackShipment(shippingId): 配送状況の確認

### 4. ユースケース
1. ユーザー登録/ログイン
   - 関連クラス: User
   - 関連メソッド: registerUser, updateUserInfo, deleteUser

2. 商品の閲覧/検索
   - 関連クラス: Product
   - 関連メソッド: createProduct, updateProduct, deleteProduct

3. カートへの商品追加/削除
   - 関連クラス: Cart
   - 関連メソッド: addToCart, removeFromCart, viewCart

4. 注文の作成/キャンセル
   - 関連クラス: Order, Payment, Shipping
   - 関連メソッド: placeOrder, cancelOrder, trackOrder, makePayment, addShippingAddress, updateShippingAddress, trackShipment

### 5. シーケンス図

**ユーザー登録**
```
+----------+       +----------+
|   User   |       |   System |
+----------+       +----------+
     |                  |
     | registerUser()   |
     |----------------->|
     |                  | createUser()
     |                  |----------------->
     |                  |<-----------------
     |                  |
     |<-----------------|
     |
```

**商品の追加**
```
+----------+       +----------+       +----------+
|  Admin   |       |  Product |       |   System |
+----------+       +----------+       +----------+
     |                  |                    |
     | createProduct()  |                    |
     |----------------->|                    |
     |                  | createProduct()    |
     |                  |------------------>|
     |                  |<------------------|
     |                  |                    |
     |<-----------------|                    |
     |                  |                    |
```

**カートへの商品追加**
```
+----------+       +----------+       +----------+
|   User   |       |   Cart   |       |  Product |
+----------+       +----------+       +----------+
     |                  |                    |
     | addToCart()      |                    |
     |----------------->|                    |
     |                  | getProduct()       |
     |                  |------------------>|
     |                  |<------------------|
     |                  | addToCart()        |
     |                  |------------------>|
     |                  |<------------------|
     |<-----------------|                    |
     |                  |                    |
```

**注文の作成**
```
+----------+       +----------+       +----------+       +----------+       +----------+
|   User   |       |   Cart   |       |   Order  |       |  Payment |       |Shipping  |
+----------+       +----------+       +----------+       +----------+       +----------+
     |                  |                    |                    |                    |
     | placeOrder()     |                    |                    |                    |
     |----------------->|                    |                    |                    |
     |                  | getCartContents()  |                    |                    |
     |                  |------------------>|                    |                    |
     |                  |<------------------|                    |                    |
     |                  |                    | createOrder()      |                    |
     |                  |                    |------------------>|                    |
     |                  |                    |<------------------|                    |
     |                  |                    |                    | makePayment()      |
     |                  |                    |                    |------------------>|
     |                  |                    |                    |<------------------|
     |                  |                    |                    | addShippingAddress()|
     |                  |                    |                    |------------------>|
     |                  |                    |                    |<------------------|
     |<-----------------|                    |                    |                    |
     |                  |                    |                    |                    |
```