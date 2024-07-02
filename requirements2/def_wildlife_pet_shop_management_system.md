# 野生動物ペットショップ管理システム

## ゴール
野生動物のペットショップのペットと顧客の管理を行うシステムを作成する。

## 1. 目的
このシステムの目的は、野生動物のペットショップの運営を支援し、ペットと顧客の情報を効率的に管理することです。
主な機能は以下の通りです。
- ペットの情報管理
- 顧客の情報管理
- ペットの販売管理
- 顧客の購買履歴管理

## 2. ファイル・フォルダ構成
```
- src/
  - main/
    - java/
      - com/
        - petshop/
          - model/
            - Animal.java
            - Customer.java
            - Order.java
          - repository/
            - AnimalRepository.java
            - CustomerRepository.java
            - OrderRepository.java
          - service/
            - AnimalService.java
            - CustomerService.java
            - OrderService.java
          - PetShopApplication.java
    - resources/
  - test/
    - java/
      - com/
        - petshop/
          - service/
            - AnimalServiceTest.java
            - CustomerServiceTest.java
            - OrderServiceTest.java
```

## 3. クラス図
```
+-----------------+        +-----------------+
|     Animal      |        |    Customer    |
+-----------------+        +-----------------+
| - id: int       |        | - id: int       |
| - name: String  |        | - name: String  |
| - species: String|        | - email: String |
| - age: int      |        | - phone: String |
| - price: double |        +-----------------+
+-----------------+                |
        |                          |
        |                          |
        v                          v
+-----------------+        +-----------------+
|     Order       |        |   OrderItem    |
+-----------------+        +-----------------+
| - id: int       |        | - id: int       |
| - customer: Customer |   | - order: Order  |
| - orderDate: Date|        | - animal: Animal|
| - total: double |        | - quantity: int |
+-----------------+        +-----------------+
```

## 4. クラスの詳細
### Animal
- **説明**: ペットショップで販売されている野生動物の情報を表すクラス
- **属性**:
  - `id`: 動物のID (int)
  - `name`: 動物の名前 (String)
  - `species`: 動物の種類 (String)
  - `age`: 動物の年齢 (int)
  - `price`: 動物の価格 (double)
- **操作**:
  - `getId()`: 動物のIDを取得する
  - `getName()`: 動物の名前を取得する
  - `getSpecies()`: 動物の種類を取得する
  - `getAge()`: 動物の年齢を取得する
  - `getPrice()`: 動物の価格を取得する

### Customer
- **説明**: ペットショップの顧客情報を表すクラス
- **属性**:
  - `id`: 顧客のID (int)
  - `name`: 顧客の名前 (String)
  - `email`: 顧客のメールアドレス (String)
  - `phone`: 顧客の電話番号 (String)
- **操作**:
  - `getId()`: 顧客のIDを取得する
  - `getName()`: 顧客の名前を取得する
  - `getEmail()`: 顧客のメールアドレスを取得する
  - `getPhone()`: 顧客の電話番号を取得する

### Order
- **説明**: ペットの注文情報を表すクラス
- **属性**:
  - `id`: 注文のID (int)
  - `customer`: 注文した顧客 (Customer)
  - `orderDate`: 注文日 (Date)
  - `total`: 注文の合計金額 (double)
- **操作**:
  - `getId()`: 注文のIDを取得する
  - `getCustomer()`: 注文した顧客を取得する
  - `getOrderDate()`: 注文日を取得する
  - `getTotal()`: 注文の合計金額を取得する

### OrderItem
- **説明**: 注文に含まれるペットの情報を表すクラス
- **属性**:
  - `id`: 注文アイテムのID (int)
  - `order`: 注文情報 (Order)
  - `animal`: 注文されたペット (Animal)
  - `quantity`: 注文数 (int)
- **操作**:
  - `getId()`: 注文アイテムのIDを取得する
  - `getOrder()`: 注文情報を取得する
  - `getAnimal()`: 注文されたペットを取得する
  - `getQuantity()`: 注文数を取得する

## 4. ユースケース
1. **ペットの管理**
   - 関連クラス: `Animal`, `AnimalRepository`, `AnimalService`
   - 主要メソッド: `createAnimal()`, `updateAnimal()`, `deleteAnimal()`, `getAnimalById()`, `getAllAnimals()`

2. **顧客の管理**
   - 関連クラス: `Customer`, `CustomerRepository`, `CustomerService`
   - 主要メソッド: `createCustomer()`, `updateCustomer()`, `deleteCustomer()`, `getCustomerById()`, `getAllCustomers()`

3. **注文の管理**
   - 関連クラス: `Order`, `OrderItem`, `OrderRepository`, `OrderService`
   - 主要メソッド: `createOrder()`, `updateOrder()`, `deleteOrder()`, `getOrderById()`, `getAllOrders()`, `createOrderItem()`, `updateOrderItem()`, `deleteOrderItem()`, `getOrderItemById()`, `getAllOrderItems()`

4. **ペットの販売**
   - 関連クラス: `Order`, `OrderItem`, `Animal`, `Customer`
   - 主要メソッド: `createOrder()`, `createOrderItem()`, `updateAnimal()`

## 5. シーケンス図
### ペットの購入
```
+---------------+    +---------------+    +---------------+    +---------------+
|   Customer    |    |    Order     |    |  OrderItem    |    |    Animal     |
+---------------+    +---------------+    +---------------+    +---------------+
       |                     |                     |                     |
       | createOrder()       |                     |                     |
       |------------------>  |                     |                     |
       |                     | createOrder()       |                     |
       |                     |------------------>  |                     |
       |                     |                     | createOrderItem()   |
       |                     |                     |------------------>  |
       |                     |                     |                     | updateAnimal()
       |                     |                     |<-------------------|
       |                     |<-------------------|                     |
       |<-------------------|                     |                     |
       |                     |                     |                     |
```

### 新しい顧客の登録
```
+---------------+    +---------------+
|   Customer    |    | CustomerService|
+---------------+    +---------------+
       |                     |
       | createCustomer()    |
       |------------------>  |
       |                     | createCustomer()
       |                     |------------------>
       |<-------------------|                     |
       |                     |<-------------------|
       |                     |                     |
```

### 注文履歴の参照
```
+---------------+    +---------------+    +---------------+    +---------------+
|   Customer    |    |    Order     |    |  OrderItem    |    |    Animal     |
+---------------+    +---------------+    +---------------+    +---------------+
       |                     |                     |                     |
       | getOrders()         |                     |                     |
       |------------------>  |                     |                     |
       |                     | getAllOrders()      |                     |
       |                     |------------------>  |                     |
       |                     |                     | getAllOrderItems()  |
       |                     |                     |------------------>  |
       |                     |                     |                     | getAllAnimals()
       |                     |                     |<-------------------|
       |                     |<-------------------|                     |
       |<-------------------|                     |                     |
       |                     |                     |                     |
```