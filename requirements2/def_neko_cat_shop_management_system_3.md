# 猫ショップ猫管理システム

## 1. 目的
本システムは、猫ショップの猫の管理を効率的に行うことを目的としています。システムを通して、猫の在庫管理、顧客管理、販売管理などを一元的に行うことで、猫ショップの業務を円滑化することが目的です。

## 2. ファイル・フォルダ構成
```
猫ショップ猫管理システム/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── catshop/
│   │   │           ├── entity/
│   │   │           │   ├── Cat.java
│   │   │           │   ├── Customer.java
│   │   │           │   └── Order.java
│   │   │           ├── repository/
│   │   │           │   ├── CatRepository.java
│   │   │           │   ├── CustomerRepository.java
│   │   │           │   └── OrderRepository.java
│   │   │           ├── service/
│   │   │           │   ├── CatService.java
│   │   │           │   ├── CustomerService.java
│   │   │           │   └── OrderService.java
│   │   │           └── CatShopApplication.java
│   │   └── resources/
│   └── test/
│       └── java/
│           └── com/
│               └── catshop/
│                   ├── repository/
│                   │   ├── CatRepositoryTest.java
│                   │   ├── CustomerRepositoryTest.java
│                   │   └── OrderRepositoryTest.java
│                   └── service/
│                       ├── CatServiceTest.java
│                       ├── CustomerServiceTest.java
│                       └── OrderServiceTest.java
└── pom.xml
```

## 3. クラス図
```
+---------------+           +---------------+
|     Cat       |           |   Customer    |
+---------------+           +---------------+
| - id: Long    |           | - id: Long    |
| - name: String|           | - name: String|
| - breed: String|          | - email: String|
| - age: int    |           | - phone: String|
| - price: int  |           +---------------+
+---------------+                   |
        |                           |
        |                           |
+---------------+           +---------------+
|     Order     |           |CatShopService |
+---------------+           +---------------+
| - id: Long    |           | + addCat()    |
| - customer: Customer |    | + updateCat() |
| - cat: Cat    |           | + deleteCat() |
| - orderDate: Date |       | + addCustomer()|
| - status: OrderStatus|    | + updateCustomer()|
+---------------+           | + deleteCustomer()|
        |                   | + placeOrder() |
        |                   | + updateOrder() |
        |                   | + cancelOrder() |
+---------------+           +---------------+
|OrderRepository|
+---------------+
| + save()      |
| + findById()  |
| + findAll()   |
+---------------+
```

## 4. クラスの詳細

### Cat
- **説明**: 猫の情報を表すクラス
- **属性**:
  - `id`: 猫のID (Long)
  - `name`: 猫の名前 (String)
  - `breed`: 猫の品種 (String)
  - `age`: 猫の年齢 (int)
  - `price`: 猫の価格 (int)
- **操作**:
  - `getId()`: 猫のIDを取得する
  - `getName()`: 猫の名前を取得する
  - `getBreed()`: 猫の品種を取得する
  - `getAge()`: 猫の年齢を取得する
  - `getPrice()`: 猫の価格を取得する
  - `setName(String name)`: 猫の名前を設定する
  - `setBreed(String breed)`: 猫の品種を設定する
  - `setAge(int age)`: 猫の年齢を設定する
  - `setPrice(int price)`: 猫の価格を設定する

### Customer
- **説明**: 顧客の情報を表すクラス
- **属性**:
  - `id`: 顧客のID (Long)
  - `name`: 顧客の名前 (String)
  - `email`: 顧客のメールアドレス (String)
  - `phone`: 顧客の電話番号 (String)
- **操作**:
  - `getId()`: 顧客のIDを取得する
  - `getName()`: 顧客の名前を取得する
  - `getEmail()`: 顧客のメールアドレスを取得する
  - `getPhone()`: 顧客の電話番号を取得する
  - `setName(String name)`: 顧客の名前を設定する
  - `setEmail(String email)`: 顧客のメールアドレスを設定する
  - `setPhone(String phone)`: 顧客の電話番号を設定する

### Order
- **説明**: 注文の情報を表すクラス
- **属性**:
  - `id`: 注文のID (Long)
  - `customer`: 注文した顧客 (Customer)
  - `cat`: 注文された猫 (Cat)
  - `orderDate`: 注文日 (Date)
  - `status`: 注文のステータス (OrderStatus)
- **操作**:
  - `getId()`: 注文のIDを取得する
  - `getCustomer()`: 注文した顧客を取得する
  - `getCat()`: 注文された猫を取得する
  - `getOrderDate()`: 注文日を取得する
  - `getStatus()`: 注文のステータスを取得する
  - `setCustomer(Customer customer)`: 注文した顧客を設定する
  - `setCat(Cat cat)`: 注文された猫を設定する
  - `setOrderDate(Date orderDate)`: 注文日を設定する
  - `setStatus(OrderStatus status)`: 注文のステータスを設定する

### CatShopService
- **説明**: 猫ショップの業務を管理するサービスクラス
- **操作**:
  - `addCat(Cat cat)`: 新しい猫を追加する
  - `updateCat(Cat cat)`: 猫の情報を更新する
  - `deleteCat(Long catId)`: 猫を削除する
  - `addCustomer(Customer customer)`: 新しい顧客を追加する
  - `updateCustomer(Customer customer)`: 顧客の情報を更新する
  - `deleteCustomer(Long customerId)`: 顧客を削除する
  - `placeOrder(Order order)`: 新しい注文を作成する
  - `updateOrder(Order order)`: 注文の情報を更新する
  - `cancelOrder(Long orderId)`: 注文をキャンセルする

### OrderRepository
- **説明**: 注文情報を管理するリポジトリクラス
- **操作**:
  - `save(Order order)`: 注文情報を保存する
  - `findById(Long id)`: 注文IDから注文情報を取得する
  - `findAll()`: 全ての注文情報を取得する

## 5. ユースケース

1. 猫の管理
   - 猫の追加
   - 猫の情報更新
   - 猫の削除

2. 顧客の管理
   - 顧客の追加
   - 顧客の情報更新
   - 顧客の削除

3. 注文の管理
   - 新規注文の作成
   - 注文の情報更新
   - 注文のキャンセル

各ユースケースに関連するクラスとメソッドは以下の通りです:

1. 猫の管理
   - 関連クラス: `Cat`, `CatRepository`, `CatService`
   - 関連メソッド:
     - `CatService.addCat(Cat cat)`
     - `CatService.updateCat(Cat cat)`
     - `CatService.deleteCat(Long catId)`

2. 顧客の管理
   - 関連クラス: `Customer`, `CustomerRepository`, `CustomerService`
   - 関連メソッド:
     - `CustomerService.addCustomer(Customer customer)`
     - `CustomerService.updateCustomer(Customer customer)`
     - `CustomerService.deleteCustomer(Long customerId)`

3. 注文の管理
   - 関連クラス: `Order`, `OrderRepository`, `OrderService`, `CatShopService`
   - 関連メソッド:
     - `CatShopService.placeOrder(Order order)`
     - `CatShopService.updateOrder(Order order)`
     - `CatShopService.cancelOrder(Long orderId)`

## 6. シーケンス図

### 猫の追加
```
+---------------+    +---------------+    +---------------+
|   CatService  |    |CatRepository  |    |      Cat      |
+---------------+    +---------------+    +---------------+
       |                     |                     |
       | addCat(cat)         |                     |
       |-------------------->|                     |
       |                     | save(cat)           |
       |                     |-------------------->|
       |                     |                     | new Cat(...)
       |                     |<--------------------|
       |                     |                     |
       |<--------------------|                     |
       |                     |                     |
```

### 注文の作成
```
+---------------+    +---------------+    +---------------+    +---------------+
|CatShopService |    |OrderRepository|    |     Order     |    |   Customer    |
+---------------+    +---------------+    +---------------+    +---------------+
       |                     |                     |                     |
       | placeOrder(order)   |                     |                     |
       |-------------------->|                     |                     |
       |                     | save(order)         |                     |
       |                     |-------------------->|                     |
       |                     |                     | new Order(...)      |
       |                     |<--------------------|                     |
       |                     |                     |                     |
       |<--------------------|                     |                     |
       |                     |                     |                     |
```

### 注文のキャンセル
```
+---------------+    +---------------+    +---------------+
|CatShopService |    |OrderRepository|    |     Order     |
+---------------+    +---------------+    +---------------+
       |                     |                     |
       | cancelOrder(orderId)|                     |
       |-------------------->|                     |
       |                     | findById(orderId)   |
       |                     |-------------------->|
       |                     |                     |
       |                     |<--------------------|
       |                     |                     |
       |                     | setStatus(CANCELED) |
       |                     |-------------------->|
       |                     | save(order)         |
       |                     |-------------------->|
       |<--------------------|                     |
       |                     |                     |
```