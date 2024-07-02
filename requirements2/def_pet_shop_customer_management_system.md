# ペットショップ顧客管理システム

## 1. 目的
本システムは、ペットショップの顧客情報を管理し、ペットの販売や予約、顧客の注文履歴の確認などを行うことを目的とする。顧客情報の一元管理と、ペットの在庫管理、注文管理など、ペットショップの業務を効率化することを目指す。

## 2. ファイル・フォルダ構成
```
ペットショップ顧客管理システム/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── model/
│   │   │           ├── repository/
│   │   │           ├── service/
│   │   │           └── ui/
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── example/
│       └── resources/
├── pom.xml
└── README.md
```

## 3. クラス図
```
+---------------+          +---------------+
|   Customer    |          |    Product    |
+---------------+          +---------------+
| - id: int     |          | - id: int     |
| - name: String|          | - name: String|
| - email: String|          | - price: int  |
| - phone: String|          | - stock: int  |
+---------------+          +---------------+
       |                           |
       |                           |
+---------------+          +---------------+
|   Order       |          |   OrderItem   |
+---------------+          +---------------+
| - id: int     |          | - id: int     |
| - customer: Customer |   | - order: Order|
| - items: List<OrderItem>| | - product: Product|
| - total: int  |          | - quantity: int|
+---------------+          +---------------+
       |                           |
       |                           |
+---------------+          +---------------+
|   PetShop     |          |   Reservation |
+---------------+          +---------------+
| - id: int     |          | - id: int     |
| - name: String|          | - customer: Customer|
| - address: String|       | - product: Product|
| - phone: String|          | - date: Date  |
+---------------+          +---------------+
```

## 4. クラスの詳細
### Customer
- 説明: 顧客情報を表すクラス
- 属性:
  - id: int - 顧客ID
  - name: String - 顧客名
  - email: String - 顧客メールアドレス
  - phone: String - 顧客電話番号
- 操作:
  - getCustomerInfo(): String - 顧客情報を文字列で返す
  - updateCustomerInfo(name: String, email: String, phone: String) - 顧客情報を更新する

### Product
- 説明: 商品情報を表すクラス
- 属性:
  - id: int - 商品ID
  - name: String - 商品名
  - price: int - 商品価格
  - stock: int - 在庫数
- 操作:
  - getProductInfo(): String - 商品情報を文字列で返す
  - updateStock(quantity: int) - 在庫数を更新する

### Order
- 説明: 注文情報を表すクラス
- 属性:
  - id: int - 注文ID
  - customer: Customer - 注文した顧客
  - items: List<OrderItem> - 注文商品のリスト
  - total: int - 注文合計金額
- 操作:
  - addOrderItem(product: Product, quantity: int) - 注文商品を追加する
  - removeOrderItem(item: OrderItem) - 注文商品を削除する
  - calculateTotal() - 注文合計金額を計算する
  - getOrderInfo(): String - 注文情報を文字列で返す

### OrderItem
- 説明: 注文商品情報を表すクラス
- 属性:
  - id: int - 注文商品ID
  - order: Order - 注文情報
  - product: Product - 注文商品
  - quantity: int - 注文数量
- 操作:
  - getOrderItemInfo(): String - 注文商品情報を文字列で返す

### PetShop
- 説明: ペットショップ情報を表すクラス
- 属性:
  - id: int - ショップID
  - name: String - ショップ名
  - address: String - ショップ住所
  - phone: String - ショップ電話番号
- 操作:
  - getShopInfo(): String - ショップ情報を文字列で返す

### Reservation
- 説明: 予約情報を表すクラス
- 属性:
  - id: int - 予約ID
  - customer: Customer - 予約した顧客
  - product: Product - 予約した商品
  - date: Date - 予約日時
- 操作:
  - getReservationInfo(): String - 予約情報を文字列で返す
  - confirmReservation() - 予約を確定する
  - cancelReservation() - 予約をキャンセルする

## 5. ユースケース
1. 顧客情報の管理
   - 顧客の登録
   - 顧客情報の閲覧
   - 顧客情報の更新
   - 顧客の削除

2. 商品の管理
   - 商品の登録
   - 商品情報の閲覧
   - 商品在庫の更新

3. 注文の管理
   - 注文の登録
   - 注文情報の閲覧
   - 注文の変更
   - 注文の削除

4. 予約の管理
   - 予約の登録
   - 予約情報の閲覧
   - 予約の確定
   - 予約のキャンセル

## 6. シーケンス図
### 顧客情報の登録
```
+-------------+   +----------+   +---------------+
| CustomerUI  |   | Customer |   | CustomerService|
+-------------+   +----------+   +---------------+
     |                |                 |
     | registerCustomer(name, email, phone)|
     |----------------------------->|
     |                |                 |
     |                | create(name, email, phone)|
     |                |---------------->|
     |                |                 |
     |                |   save(customer)|
     |                |---------------->|
     |                |                 |
     |<---------------------------|
     |                |                 |
     | returnCustomerInfo(customer) |
     |<---------------------------|
     |                |                 |
```

### 商品の注文
```
+-------------+   +----------+   +-------------+   +------------+
|    OrderUI  |   |  Order   |   |  OrderService|   |  ProductRepo|
+-------------+   +----------+   +-------------+   +------------+
     |                |                 |                  |
     | placeOrder(customer, products)  |                  |
     |----------------------------->|                  |
     |                |                 |                  |
     |                | create(customer)|                  |
     |                |---------------->|                  |
     |                |                 |                  |
     |                |   addOrderItem()|                  |
     |                |---------------->|                  |
     |                |                 |   getProduct(id) |
     |                |                 |----------------->|
     |                |                 |<-----------------|
     |                |                 |   updateStock()  |
     |                |                 |----------------->|
     |                |   calculateTotal()|                |
     |                |---------------->|                  |
     |                |                 |                  |
     |<---------------------------|                  |
     |                |                 |                  |
     | returnOrderInfo(order)     |                  |
     |<---------------------------|                  |
     |                |                 |                  |
```

### 予約の登録
```
+---------------+   +------------+   +---------------+   +----------+
|   ReservationUI|   | Reservation|   | ReservationService|   | ProductRepo|
+---------------+   +------------+   +---------------+   +----------+
        |                 |                   |                  |
        | makeReservation(customer, product, date)|               |
        |------------------------>|                   |                  |
        |                 | create(customer, product, date)|       |
        |                 |------------------------>|                  |
        |                 |                   |   getProduct(id)  |
        |                 |                   |------------------>|
        |                 |                   |<------------------|
        |                 |   confirmReservation()|                  |
        |                 |------------------------>|                  |
        |                 |                   |                  |
        |<------------------------|                   |                  |
        |                 |                   |                  |
        | returnReservationInfo(reservation)|                   |
        |<------------------------|                   |                  |
        |                 |                   |                  |
```