# さるペットショップのペットと顧客管理システム

## 1. 目的
このシステムは、さるペットショップの運営を支援するために開発されます。ペットの在庫管理、顧客情報の管理、販売管理などの機能を提供し、ペットショップの業務の効率化と生産性の向上を目的としています。

## 2. ファイル・フォルダ構成
```
- src/
  - main/
    - java/
      - com/
        - sarushop/
          - model/
            - Pet.java
            - Customer.java
            - Order.java
          - repository/
            - PetRepository.java
            - CustomerRepository.java
            - OrderRepository.java
          - service/
            - PetService.java
            - CustomerService.java
            - OrderService.java
          - controller/
            - PetController.java
            - CustomerController.java
            - OrderController.java
          - SaruShopApplication.java
    - resources/
      - application.properties
  - test/
    - java/
      - com/
        - sarushop/
          - SaruShopApplicationTests.java
          - service/
            - PetServiceTest.java
            - CustomerServiceTest.java
            - OrderServiceTest.java
- pom.xml
```

## 3. クラス図
```
+---------------+        1..n        +---------------+
|    Customer   |----------------------|    Order     |
+---------------+                     +---------------+
| - id: Long    |                     | - id: Long    |
| - name: String|                     | - customer: Customer|
| - email: String|                     | - pet: Pet    |
| - phone: String|                     | - orderDate: Date|
| - address: String|                  | - quantity: int|
+---------------+                     | - totalPrice: double|
                                      +---------------+
                                      
+---------------+        1..n        +---------------+
|      Pet      |----------------------|    Order     |
+---------------+                     +---------------+
| - id: Long    |                     | - id: Long    |
| - name: String|                     | - customer: Customer|
| - species: String|                  | - pet: Pet    |
| - age: int    |                     | - orderDate: Date|
| - price: double|                    | - quantity: int|
| - inStock: boolean|                 | - totalPrice: double|
+---------------+                     +---------------+

+---------------+        1..1        +---------------+
|  PetService   |----------------------| PetRepository|
+---------------+                     +---------------+
| + savePet()   |                     | + save()      |
| + updatePet() |                     | + findById()  |
| + deletePet() |                     | + findAll()   |
| + findPetById()|                    +---------------+
| + findAllPets()|
+---------------+

+---------------+        1..1        +---------------+
|CustomerService|----------------------|CustomerRepository|
+---------------+                     +---------------+
| + saveCustomer()|                   | + save()      |
| + updateCustomer()|                 | + findById()  |
| + deleteCustomer()|                 | + findAll()   |
| + findCustomerById()|               +---------------+
| + findAllCustomers()|
+---------------+

+---------------+        1..1        +---------------+
|  OrderService |----------------------|  OrderRepository|
+---------------+                     +---------------+
| + placeOrder()|                     | + save()      |
| + updateOrder()|                    | + findById()  |
| + cancelOrder()|                    | + findAll()   |
| + findOrderById()|                  +---------------+
| + findAllOrders()|
+---------------+
```

## 4. クラスの詳細

### Pet
- **説明**: ペットの情報を管理するクラス
- **属性**:
  - `id: Long` - ペットのID
  - `name: String` - ペットの名前
  - `species: String` - ペットの種類
  - `age: int` - ペットの年齢
  - `price: double` - ペットの価格
  - `inStock: boolean` - ペットの在庫状況
- **操作**:
  - `getId()`: ペットのIDを取得する
  - `getName()`: ペットの名前を取得する
  - `getSpecies()`: ペットの種類を取得する
  - `getAge()`: ペットの年齢を取得する
  - `getPrice()`: ペットの価格を取得する
  - `isInStock()`: ペットの在庫状況を取得する
  - `setName(String name)`: ペットの名前を設定する
  - `setSpecies(String species)`: ペットの種類を設定する
  - `setAge(int age)`: ペットの年齢を設定する
  - `setPrice(double price)`: ペットの価格を設定する
  - `setInStock(boolean inStock)`: ペットの在庫状況を設定する

### Customer
- **説明**: 顧客の情報を管理するクラス
- **属性**:
  - `id: Long` - 顧客のID
  - `name: String` - 顧客の名前
  - `email: String` - 顧客のメールアドレス
  - `phone: String` - 顧客の電話番号
  - `address: String` - 顧客の住所
- **操作**:
  - `getId()`: 顧客のIDを取得する
  - `getName()`: 顧客の名前を取得する
  - `getEmail()`: 顧客のメールアドレスを取得する
  - `getPhone()`: 顧客の電話番号を取得する
  - `getAddress()`: 顧客の住所を取得する
  - `setName(String name)`: 顧客の名前を設定する
  - `setEmail(String email)`: 顧客のメールアドレスを設定する
  - `setPhone(String phone)`: 顧客の電話番号を設定する
  - `setAddress(String address)`: 顧客の住所を設定する

### Order
- **説明**: 注文情報を管理するクラス
- **属性**:
  - `id: Long` - 注文のID
  - `customer: Customer` - 注文した顧客
  - `pet: Pet` - 注文されたペット
  - `orderDate: Date` - 注文日
  - `quantity: int` - 注文数
  - `totalPrice: double` - 注文合計金額
- **操作**:
  - `getId()`: 注文のIDを取得する
  - `getCustomer()`: 注文した顧客を取得する
  - `getPet()`: 注文されたペットを取得する
  - `getOrderDate()`: 注文日を取得する
  - `getQuantity()`: 注文数を取得する
  - `getTotalPrice()`: 注文合計金額を取得する
  - `setCustomer(Customer customer)`: 注文した顧客を設定する
  - `setPet(Pet pet)`: 注文されたペットを設定する
  - `setOrderDate(Date orderDate)`: 注文日を設定する
  - `setQuantity(int quantity)`: 注文数を設定する
  - `setTotalPrice(double totalPrice)`: 注文合計金額を設定する

## 5. ユースケース

1. **ペットの管理**
   - クラス: `PetService`, `PetRepository`
   - メソッド:
     - `savePet(Pet pet)`: ペットを新規登録する
     - `updatePet(Pet pet)`: ペットの情報を更新する
     - `deletePet(Long petId)`: ペットを削除する
     - `findPetById(Long petId)`: ペットの詳細情報を取得する
     - `findAllPets()`: 全てのペットの情報を取得する

2. **顧客の管理**
   - クラス: `CustomerService`, `CustomerRepository`
   - メソッド:
     - `saveCustomer(Customer customer)`: 顧客を新規登録する
     - `updateCustomer(Customer customer)`: 顧客の情報を更新する
     - `deleteCustomer(Long customerId)`: 顧客を削除する
     - `findCustomerById(Long customerId)`: 顧客の詳細情報を取得する
     - `findAllCustomers()`: 全ての顧客の情報を取得する

3. **注文の管理**
   - クラス: `OrderService`, `OrderRepository`
   - メソッド:
     - `placeOrder(Order order)`: 新しい注文を登録する
     - `updateOrder(Order order)`: 注文の情報を更新する
     - `cancelOrder(Long orderId)`: 注文をキャンセルする
     - `findOrderById(Long orderId)`: 注文の詳細情報を取得する
     - `findAllOrders()`: 全ての注文の情報を取得する

## 6. シーケンス図

### ペットの新規登録
```
+---------------+    +---------------+    +---------------+
|  PetController|    |   PetService  |    |PetRepository  |
+---------------+    +---------------+    +---------------+
       |                     |                     |
       | savePet(newPet)     |                     |
       |-------------------->|                     |
       |                     | savePet(newPet)     |
       |                     |-------------------->|
       |                     |                     | save(newPet)
       |                     |                     |-------------------->
       |                     |<--------------------|
       |<--------------------|                     |
       |                     |                     |
```

### 顧客の新規登録
```
+---------------+    +---------------+    +---------------+
|CustomerController|  |CustomerService|    |CustomerRepository|
+---------------+    +---------------+    +---------------+
       |                     |                     |
       | saveCustomer(newCustomer)|               |
       |-------------------->|                     |
       |                     | saveCustomer(newCustomer)|
       |                     |-------------------->|
       |                     |                     | save(newCustomer)
       |                     |                     |-------------------->
       |                     |<--------------------|
       |<--------------------|                     |
       |                     |                     |
```

### 注文の新規登録
```
+---------------+    +---------------+    +---------------+    +---------------+
|  OrderController|  |   OrderService|    |OrderRepository|    |   PetService  |
+---------------+    +---------------+    +---------------+    +---------------+
       |                     |                     |                     |
       | placeOrder(newOrder)|                     |                     |
       |-------------------->|                     |                     |
       |                     | placeOrder(newOrder)|                     |
       |                     |-------------------->|                     |
       |                     |                     | save(newOrder)      |
       |                     |                     |-------------------->|
       |                     |                     |                     | findPetById(newOrder.petId)
       |                     |                     |                     |-------------------->
       |                     |                     |<--------------------|
       |                     |<--------------------|                     |
       |<--------------------|                     |                     |
```