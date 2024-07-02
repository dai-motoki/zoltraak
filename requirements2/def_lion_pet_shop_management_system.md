# ペットショップ管理システム

## ゴール: ライオンのペットショップのペットと顧客管理システムを作成する

## 1. 目的
このシステムの目的は、ペットショップの顧客管理と在庫管理を効率的に行うことです。顧客情報の管理、ペットの在庫管理、販売管理などの機能を提供することで、ペットショップの運営を支援します。

## 2. ファイル・フォルダ構成
```
ペットショップ管理システム/
├── src/
│   ├── main/
│   │   └── java/
│   │       └── com/
│   │           └── petshop/
│   │               ├── model/
│   │               │   ├── Customer.java
│   │               │   ├── Pet.java
│   │               │   ├── PetInventory.java
│   │               │   └── Sale.java
│   │               ├── repository/
│   │               │   ├── CustomerRepository.java
│   │               │   └── PetRepository.java
│   │               ├── service/
│   │               │   ├── CustomerService.java
│   │               │   └── PetService.java
│   │               └── PetShopApp.java
│   └── test/
│       └── java/
│           └── com/
│               └── petshop/
│                   ├── repository/
│                   │   ├── CustomerRepositoryTest.java
│                   │   └── PetRepositoryTest.java
│                   └── service/
│                       ├── CustomerServiceTest.java
│                       └── PetServiceTest.java
└── pom.xml
```

## 3. クラス図
```
+---------------+           +---------------+
|    Customer   |           |     Pet       |
+---------------+           +---------------+
| - id: int     |           | - id: int     |
| - name: String|           | - name: String|
| - email: String|          | - type: String|
| - phone: String|          | - price: double|
+---------------+           +---------------+
        |                           |
        |                           |
+---------------+           +---------------+
|  PetInventory |           |    Sale       |
+---------------+           +---------------+
| - id: int     |           | - id: int     |
| - pet: Pet    |           | - customer: Customer|
| - quantity: int|          | - pet: Pet    |
+---------------+           | - quantity: int|
        |                   | - date: Date  |
        |                   +---------------+
+---------------+
|PetShopService |
+---------------+
| + addCustomer()|
| + updateCustomer()|
| + getCustomers()|
| + addPet()     |
| + updatePet()  |
| + getPets()    |
| + makeSale()   |
| + getSales()   |
+---------------+
```

## 4. クラスの詳細

### Customer
- **説明**: 顧客情報を管理するクラス
- **属性**:
  - `id`: 顧客ID (int)
  - `name`: 顧客名 (String)
  - `email`: 顧客メールアドレス (String)
  - `phone`: 顧客電話番号 (String)
- **操作**:
  - `getId()`: 顧客IDを取得する
  - `getName()`: 顧客名を取得する
  - `getEmail()`: 顧客メールアドレスを取得する
  - `getPhone()`: 顧客電話番号を取得する
  - `setName(String name)`: 顧客名を設定する
  - `setEmail(String email)`: 顧客メールアドレスを設定する
  - `setPhone(String phone)`: 顧客電話番号を設定する

### Pet
- **説明**: ペットの情報を管理するクラス
- **属性**:
  - `id`: ペットID (int)
  - `name`: ペット名 (String)
  - `type`: ペットの種類 (String)
  - `price`: ペットの価格 (double)
- **操作**:
  - `getId()`: ペットIDを取得する
  - `getName()`: ペット名を取得する
  - `getType()`: ペットの種類を取得する
  - `getPrice()`: ペットの価格を取得する
  - `setName(String name)`: ペット名を設定する
  - `setType(String type)`: ペットの種類を設定する
  - `setPrice(double price)`: ペットの価格を設定する

### PetInventory
- **説明**: ペットの在庫情報を管理するクラス
- **属性**:
  - `id`: 在庫ID (int)
  - `pet`: 在庫のペット (Pet)
  - `quantity`: 在庫数 (int)
- **操作**:
  - `getId()`: 在庫IDを取得する
  - `getPet()`: 在庫のペットを取得する
  - `getQuantity()`: 在庫数を取得する
  - `setPet(Pet pet)`: 在庫のペットを設定する
  - `setQuantity(int quantity)`: 在庫数を設定する

### Sale
- **説明**: 販売情報を管理するクラス
- **属性**:
  - `id`: 販売ID (int)
  - `customer`: 購入した顧客 (Customer)
  - `pet`: 購入したペット (Pet)
  - `quantity`: 購入数 (int)
  - `date`: 購入日 (Date)
- **操作**:
  - `getId()`: 販売IDを取得する
  - `getCustomer()`: 購入した顧客を取得する
  - `getPet()`: 購入したペットを取得する
  - `getQuantity()`: 購入数を取得する
  - `getDate()`: 購入日を取得する
  - `setCustomer(Customer customer)`: 購入した顧客を設定する
  - `setPet(Pet pet)`: 購入したペットを設定する
  - `setQuantity(int quantity)`: 購入数を設定する
  - `setDate(Date date)`: 購入日を設定する

### PetShopService
- **説明**: ペットショップの各種サービスを提供するクラス
- **操作**:
  - `addCustomer(Customer customer)`: 新規顧客を登録する
  - `updateCustomer(int customerId, Customer updatedCustomer)`: 顧客情報を更新する
  - `getCustomers()`: 全顧客情報を取得する
  - `addPet(Pet pet)`: 新規ペットを登録する
  - `updatePet(int petId, Pet updatedPet)`: ペット情報を更新する
  - `getPets()`: 全ペット情報を取得する
  - `makeSale(Sale sale)`: 販売情報を登録する
  - `getSales()`: 全販売情報を取得する

## 4. ユースケース
1. 顧客管理
   - 顧客の登録
   - 顧客情報の更新
   - 顧客情報の表示
2. ペット管理
   - ペットの登録
   - ペット情報の更新
   - ペット情報の表示
3. 販売管理
   - 販売の登録
   - 販売情報の表示

## 5. シーケンス図

### 顧客の登録
```
+---------------+      +---------------+      +---------------+
|   PetShopApp  |      |CustomerService|      |CustomerRepository|
+---------------+      +---------------+      +---------------+
        |                      |                      |
        | addCustomer(customer)|                      |
        |----------------------|                      |
        |                      | saveCustomer(customer)|
        |                      |----------------------->|
        |                      |                      |
        |                      |<-----------------------|
        |                      |                      |
        |<--------------------|                      |
        |                      |                      |
```

### ペットの販売
```
+---------------+      +---------------+      +---------------+      +---------------+      +---------------+
|   PetShopApp  |      |   PetService  |      |PetRepository  |      |CustomerService|      |   SaleService  |
+---------------+      +---------------+      +---------------+      +---------------+      +---------------+
        |                      |                      |                      |                      |
        | makeSale(sale)       |                      |                      |                      |
        |----------------------|                      |                      |                      |
        |                      | getCustomer(customerId)|                      |                      |
        |                      |----------------------->|                      |                      |
        |                      |                      |<-----------------------|                      |
        |                      |                      |                      | getCustomer(customerId)|
        |                      |                      |                      |----------------------->|
        |                      |                      |                      |<-----------------------|
        |                      | getPet(petId)        |                      |                      |
        |                      |----------------------->|                      |                      |
        |                      |                      |<-----------------------|                      |
        |                      | saveSale(sale)       |                      |                      |
        |                      |----------------------->|                      |                      |
        |                      |                      |<-----------------------|                      |
        |<--------------------|                      |                      |                      |
        |                      |                      |                      |                      |
```