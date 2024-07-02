# ペットショップ管理システム

## ゴール
犬のペットショップのペットと顧客の管理を行うシステムを構築する。

## 1. 目的
このシステムは、ペットショップの運営を効率化し、ペットの販売管理と顧客管理を一元的に行うことを目的とする。主な機能は以下の通り。

- ペットの在庫管理
- 顧客情報の管理
- ペットの販売管理
- 顧客の注文管理

## 2. ファイル・フォルダ構造
```
ペットショップ管理システム/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── model/
│   │   │           ├── repository/
│   │   │           ├── service/
│   │   │           └── Main.java
│   │   └── resources/
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── example/
│       │           ├── model/
│       │           ├── repository/
│       │           └── service/
│       └── resources/
├── pom.xml
└── README.md
```

## 3. クラス図
```
+-------------+        +---------------+
|    Pet      |        |   Customer    |
+-------------+        +---------------+
| - id: int   |        | - id: int     |
| - name: str |        | - name: str   |
| - breed: str|        | - phone: str  |
| - age: int  |        | - email: str  |
| - price: int|        +---------------+
+-------------+        |   inherits from   |
      |                +---------------+
      |                |   Person      |
      |                +---------------+
      |                | - name: str   |
      |                | - phone: str  |
      |                | - email: str  |
      |                +---------------+
      |                        |
      |                        |
      |                +---------------+
      |                | PetRepository |
      |                +---------------+
      |                | - pets: Map<int, Pet> |
      |                | + addPet(pet: Pet)   |
      |                | + getPet(id: int): Pet |
      |                | + updatePet(pet: Pet) |
      |                | + deletePet(id: int) |
      |                +---------------+
      |                        |
      |                        |
      |                +---------------+
      |                | CustomerRepository |
      |                +---------------+
      |                | - customers: Map<int, Customer> |
      |                | + addCustomer(customer: Customer) |
      |                | + getCustomer(id: int): Customer |
      |                | + updateCustomer(customer: Customer) |
      |                | + deleteCustomer(id: int) |
      |                +---------------+
      |                        |
      |                        |
      |                +---------------+
      |                |   PetService  |
      |                +---------------+
      |                | - petRepository: PetRepository |
      |                | + addPet(pet: Pet)             |
      |                | + getPet(id: int): Pet         |
      |                | + updatePet(pet: Pet)         |
      |                | + deletePet(id: int)          |
      |                +---------------+
      |                        |
      |                        |
      |                +---------------+
      |                | CustomerService|
      |                +---------------+
      |                | - customerRepository: CustomerRepository |
      |                | + addCustomer(customer: Customer)       |
      |                | + getCustomer(id: int): Customer       |
      |                | + updateCustomer(customer: Customer)   |
      |                | + deleteCustomer(id: int)              |
      |                +---------------+
      |                        |
      |                        |
      |                +---------------+
      |                |    Main       |
      |                +---------------+
      |                | + main(args: String[]) |
      |                +---------------+
```

## 4. クラスの詳細

### Pet
- 説明: ペットを表すクラス
- 属性:
  - id: int - ペットのID
  - name: String - ペットの名前
  - breed: String - ペットの品種
  - age: int - ペットの年齢
  - price: int - ペットの価格
- 操作:
  - なし

### Customer
- 説明: 顧客を表すクラス
- 属性:
  - id: int - 顧客のID
  - name: String - 顧客の名前
  - phone: String - 顧客の電話番号
  - email: String - 顧客のメールアドレス
- 操作:
  - なし

### Person
- 説明: 顧客の一般的な情報を表すクラス
- 属性:
  - name: String - 名前
  - phone: String - 電話番号
  - email: String - メールアドレス
- 操作:
  - なし

### PetRepository
- 説明: ペットの情報を管理するリポジトリ
- 属性:
  - pets: Map<Integer, Pet> - ペットの情報を保持する
- 操作:
  - addPet(pet: Pet): void - ペットを追加する
  - getPet(id: int): Pet - ペットのIDから情報を取得する
  - updatePet(pet: Pet): void - ペットの情報を更新する
  - deletePet(id: int): void - ペットの情報を削除する

### CustomerRepository
- 説明: 顧客の情報を管理するリポジトリ
- 属性:
  - customers: Map<Integer, Customer> - 顧客の情報を保持する
- 操作:
  - addCustomer(customer: Customer): void - 顧客を追加する
  - getCustomer(id: int): Customer - 顧客のIDから情報を取得する
  - updateCustomer(customer: Customer): void - 顧客の情報を更新する
  - deleteCustomer(id: int): void - 顧客の情報を削除する

### PetService
- 説明: ペットの管理を行うサービス
- 属性:
  - petRepository: PetRepository - ペットの情報を管理するリポジトリ
- 操作:
  - addPet(pet: Pet): void - ペットを追加する
  - getPet(id: int): Pet - ペットのIDから情報を取得する
  - updatePet(pet: Pet): void - ペットの情報を更新する
  - deletePet(id: int): void - ペットの情報を削除する

### CustomerService
- 説明: 顧客の管理を行うサービス
- 属性:
  - customerRepository: CustomerRepository - 顧客の情報を管理するリポジトリ
- 操作:
  - addCustomer(customer: Customer): void - 顧客を追加する
  - getCustomer(id: int): Customer - 顧客のIDから情報を取得する
  - updateCustomer(customer: Customer): void - 顧客の情報を更新する
  - deleteCustomer(id: int): void - 顧客の情報を削除する

### Main
- 説明: アプリケーションのエントリーポイント
- 操作:
  - main(args: String[]): void - アプリケーションを起動する

## 5. ユースケース

1. ペットの管理
   - 操作: addPet, getPet, updatePet, deletePet
   - 関連クラス: Pet, PetRepository, PetService

2. 顧客の管理
   - 操作: addCustomer, getCustomer, updateCustomer, deleteCustomer
   - 関連クラス: Customer, CustomerRepository, CustomerService

3. ペットの販売
   - 操作: addPet, getPet, updatePet, addCustomer, getCustomer
   - 関連クラス: Pet, PetRepository, PetService, Customer, CustomerRepository, CustomerService

4. 注文管理
   - 操作: addCustomer, getCustomer, updateCustomer
   - 関連クラス: Customer, CustomerRepository, CustomerService

## 6. シーケンス図

### ペットの追加
```
+----------+   +---------------+   +-------------+
|   Main   |   | PetService    |   | PetRepository|
+----------+   +---------------+   +-------------+
     |               |                    |
     | addPet(pet)   |                    |
     |-------------->|                    |
     |               | addPet(pet)        |
     |               |------------------>|
     |               |                    | pets.put(pet.id, pet)
     |               |                    |
     |<--------------|                    |
     |               |                    |
```

### 顧客の追加
```
+----------+   +---------------+   +---------------+
|   Main   |   | CustomerService|   | CustomerRepository|
+----------+   +---------------+   +---------------+
     |               |                    |
     | addCustomer(customer) |            |
     |------------------>|                |
     |               | addCustomer(customer)|
     |               |------------------>|
     |               |                    | customers.put(customer.id, customer)
     |               |                    |
     |<---------------^                    |
     |               |                    |
```

### ペットの販売
```
+----------+   +---------------+   +-------------+   +---------------+
|   Main   |   | PetService    |   | PetRepository|   | CustomerService|
+----------+   +---------------+   +-------------+   +---------------+
     |               |                    |                    |
     | addPet(pet)    |                    |                    |
     |------------------>|                |                    |
     |               | addPet(pet)        |                    |
     |               |------------------>|                    |
     |               |                    | pets.put(pet.id, pet)|
     |               |                    |                    |
     |<---------------^                    |                    |
     |               |                    |                    |
     | addCustomer(customer)|             |                    |
     |                    |------------------>|                |
     |                    | addCustomer(customer)|             |
     |                    |------------------>|                |
     |                    |                    | customers.put(customer.id, customer)|
     |                    |                    |                |
     |                    |<------------------^                |
     |                    |                    |                |
```

### 注文管理
```
+----------+   +---------------+   +---------------+
|   Main   |   | CustomerService|   | CustomerRepository|
+----------+   +---------------+   +---------------+
     |               |                    |
     | addCustomer(customer)|             |
     |------------------>|                |
     |               | addCustomer(customer)|
     |               |------------------>|
     |               |                    | customers.put(customer.id, customer)
     |               |                    |
     |<---------------^                    |
     |               |                    |
     | getCustomer(id)|                    |
     |------------------>|                |
     |               | getCustomer(id)    |
     |               |------------------>|
     |               |                    | return customers.get(id)
     |               |                    |
     |<---------------^                    |
     |               |                    |
     | updateCustomer(customer)|          |
     |------------------>|                |
     |               | updateCustomer(customer)|
     |               |------------------>|
     |               |                    | customers.put(customer.id, customer)
     |               |                    |
     |<---------------^                    |
     |               |                    |
```