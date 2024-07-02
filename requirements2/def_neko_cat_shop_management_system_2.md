# 猫ショップ猫管理システム

## 1. 目的
本システムは、猫ショップにおける猫の管理を効率化し、ショップの運営を支援することを目的としています。具体的には、猫の在庫管理、顧客情報の管理、販売記録の管理などの機能を提供することで、ショップ経営の改善に寄与することを目的としています。

## 2. ファイル・フォルダ構成
```
猫ショップ猫管理システム/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── Cat.java
│   │   │           ├── Customer.java
│   │   │           ├── Order.java
│   │   │           ├── Shop.java
│   │   │           └── ShopManager.java
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── example/
│       │           ├── CatTest.java
│       │           ├── CustomerTest.java
│       │           ├── OrderTest.java
│       │           ├── ShopTest.java
│       │           └── ShopManagerTest.java
│       └── resources/
└── docs/
    ├── requirements.md
    └── design.md
```

## 3. クラス図
```
+---------------+        +---------------+
|     Cat       |        |   Customer    |
+---------------+        +---------------+
| - id: int     |        | - id: int     |
| - name: String|        | - name: String|
| - breed: String|        | - phone: String|
| - age: int    |        | - email: String|
| - price: int  |        +---------------+
+---------------+        |    methods    |
|    methods    |        +---------------+
+---------------+        

+---------------+        +---------------+
|     Order     |        |    ShopManager|
+---------------+        +---------------+
| - id: int     |        | - shop: Shop  |
| - customer: Customer|  | - catList: List<Cat>|
| - cat: Cat    |        | - customerList: List<Customer>|
| - date: Date  |        | - orderList: List<Order>|
+---------------+        +---------------+
|    methods    |        |    methods    |
+---------------+        +---------------+

+---------------+
|      Shop     |
+---------------+
| - name: String|
| - address: String|
+---------------+
|    methods    |
+---------------+
```

## 4. クラスの詳細
### Cat
- 説明: 猫の情報を表すクラス
- 属性:
  - id: int - 猫の一意な識別子
  - name: String - 猫の名前
  - breed: String - 猫の品種
  - age: int - 猫の年齢
  - price: int - 猫の価格
- 操作:
  - 猫の情報を取得/設定する各種メソッド

### Customer
- 説明: 顧客の情報を表すクラス
- 属性:
  - id: int - 顧客の一意な識別子
  - name: String - 顧客の名前
  - phone: String - 顧客の電話番号
  - email: String - 顧客のメールアドレス
- 操作:
  - 顧客の情報を取得/設定する各種メソッド

### Order
- 説明: 注文情報を表すクラス
- 属性:
  - id: int - 注文の一意な識別子
  - customer: Customer - 注文した顧客
  - cat: Cat - 注文された猫
  - date: Date - 注文日
- 操作:
  - 注文情報を取得/設定する各種メソッド
  - 注文の状況を管理するメソッド

### Shop
- 説明: 猫ショップの情報を表すクラス
- 属性:
  - name: String - ショップの名称
  - address: String - ショップの住所
- 操作:
  - ショップの情報を取得/設定する各種メソッド

### ShopManager
- 説明: 猫ショップの管理を行うクラス
- 属性:
  - shop: Shop - 管理対象のショップ
  - catList: List<Cat> - 在庫の猫のリスト
  - customerList: List<Customer> - 登録された顧客のリスト
  - orderList: List<Order> - 注文履歴のリスト
- 操作:
  - 猫の在庫管理に関するメソッド
  - 顧客管理に関するメソッド
  - 注文管理に関するメソッド
  - レポート出力などの管理機能を提供するメソッド

## 5. ユースケース
1. 猫の在庫管理
   - 関連クラス: Cat, ShopManager
   - 関連メソッド: ShopManager.addCat(), ShopManager.removeCat(), ShopManager.updateCatInfo()
2. 顧客管理
   - 関連クラス: Customer, ShopManager
   - 関連メソッド: ShopManager.addCustomer(), ShopManager.removeCustomer(), ShopManager.updateCustomerInfo()
3. 注文管理
   - 関連クラス: Order, Customer, Cat, ShopManager
   - 関連メソッド: ShopManager.placeOrder(), ShopManager.cancelOrder(), ShopManager.getOrderHistory()

## 6. シーケンス図
### 猫の在庫管理
```
+---------------+   +---------------+   +---------------+
|   ShopManager |   |      Cat      |   |      Shop     |
+---------------+   +---------------+   +---------------+
        |                   |                   |
        | addCat(cat)        |                   |
        |------------------>|                   |
        |                   | save(cat)         |
        |                   |------------------>|
        |                   |                   |
        |   removeCat(cat)   |                   |
        |------------------>|                   |
        |                   | delete(cat)       |
        |                   |------------------>|
        |                   |                   |
        |  updateCatInfo()   |                   |
        |------------------>|                   |
        |                   | update(cat)       |
        |                   |------------------>|
        |                   |                   |
```

### 顧客管理
```
+---------------+   +---------------+   +---------------+
|   ShopManager |   |    Customer   |   |      Shop     |
+---------------+   +---------------+   +---------------+
        |                   |                   |
        | addCustomer(customer)|               |
        |------------------>|                   |
        |                   | save(customer)   |
        |                   |------------------>|
        |                   |                   |
        | removeCustomer(customer)|            |
        |------------------>|                   |
        |                   | delete(customer) |
        |                   |------------------>|
        |                   |                   |
        | updateCustomerInfo()|                |
        |------------------>|                   |
        |                   | update(customer) |
        |                   |------------------>|
        |                   |                   |
```

### 注文管理
```
+---------------+   +---------------+   +---------------+   +---------------+
|   ShopManager |   |    Customer   |   |      Cat      |   |     Order     |
+---------------+   +---------------+   +---------------+   +---------------+
        |                   |                   |                   |
        |   placeOrder(order)|                  |                   |
        |------------------>|                   |                   |
        |                   | createOrder(cat)  |                   |
        |                   |------------------>|                   |
        |                   |                   |                   | save(order)
        |                   |                   |                   |------------------>
        |                   |                   |                   |
        |   cancelOrder(order)|                 |                   |
        |------------------>|                   |                   |
        |                   |                   |                   | delete(order)
        |                   |                   |                   |------------------>
        |                   |                   |                   |
        |  getOrderHistory() |                  |                   |
        |------------------>|                   |                   |
        |                   |                   |                   | getOrders()
        |                   |                   |                   |------------------>
        |                   |                   |                   |
```