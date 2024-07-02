# ペットと顧客管理システム

## 1. 目的
このシステムは、ある小さなペットショップの顧客管理と在庫管理を支援することを目的としています。店主は、このシステムを使ってペットの在庫状況を把握し、顧客情報を管理することができます。また、顧客は、このシステムを通じてペットの情報を閲覧し、注文することができます。

## 2. ファイル・フォルダ構造

```
ペットと顧客管理システム/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── petshop/
│   │   │           ├── model/
│   │   │           │   ├── Customer.java
│   │   │           │   ├── Pet.java
│   │   │           │   ├── PetCategory.java
│   │   │           │   └── PetOrder.java
│   │   │           ├── repository/
│   │   │           │   ├── CustomerRepository.java
│   │   │           │   └── PetRepository.java
│   │   │           ├── service/
│   │   │           │   ├── CustomerService.java
│   │   │           │   └── PetService.java
│   │   │           └── App.java
│   │   └── resources/
│   └── test/
│       └── java/
│           └── com/
│               └── petshop/
│                   ├── model/
│                   ├── repository/
│                   └── service/
└── pom.xml
```

## 3. クラス図

```
+---------------+        +---------------+
|    Customer   |        |     Pet       |
+---------------+        +---------------+
| - id: int     |        | - id: int     |
| - name: String|        | - name: String|
| - email: String|        | - category: PetCategory|
| - phone: String|        | - price: double|
+---------------+        +---------------+
      |                         |
      |                         |
+---------------+        +---------------+
|  PetOrder     |        |  PetCategory  |
+---------------+        +---------------+
| - id: int     |        | - id: int     |
| - customer: Customer| | - name: String|
| - pet: Pet    |        +---------------+
| - quantity: int|
| - orderDate: Date|
+---------------+
      |
      |
+---------------+
| CustomerRepository|
+---------------+
| - customers: Map<int, Customer>|
| + saveCustomer(Customer): void|
| + getCustomer(int): Customer |
+---------------+
      |
      |
+---------------+
|  PetRepository |
+---------------+
| - pets: Map<int, Pet>|
| + savePet(Pet): void|
| + getPet(int): Pet |
+---------------+
      |
      |
+---------------+
|CustomerService|
+---------------+
| - repository: CustomerRepository|
| + createCustomer(String, String, String): Customer|
| + getCustomer(int): Customer|
+---------------+
      |
      |
+---------------+
|   PetService   |
+---------------+
| - repository: PetRepository|
| + createPet(String, PetCategory, double): Pet|
| + getPet(int): Pet|
+---------------+
```

## 4. クラスの詳細

### Customer
- **説明**: 顧客を表すクラス
- **属性**:
  - `id`: 顧客ID (int)
  - `name`: 顧客名 (String)
  - `email`: 顧客のメールアドレス (String)
  - `phone`: 顧客の電話番号 (String)
- **操作**:
  - `getId()`: 顧客IDを取得する
  - `getName()`: 顧客名を取得する
  - `getEmail()`: 顧客のメールアドレスを取得する
  - `getPhone()`: 顧客の電話番号を取得する

### Pet
- **説明**: ペットを表すクラス
- **属性**:
  - `id`: ペットID (int)
  - `name`: ペットの名前 (String)
  - `category`: ペットのカテゴリ (PetCategory)
  - `price`: ペットの価格 (double)
- **操作**:
  - `getId()`: ペットIDを取得する
  - `getName()`: ペットの名前を取得する
  - `getCategory()`: ペットのカテゴリを取得する
  - `getPrice()`: ペットの価格を取得する

### PetCategory
- **説明**: ペットのカテゴリを表すクラス
- **属性**:
  - `id`: カテゴリID (int)
  - `name`: カテゴリ名 (String)
- **操作**:
  - `getId()`: カテゴリIDを取得する
  - `getName()`: カテゴリ名を取得する

### PetOrder
- **説明**: ペットの注文を表すクラス
- **属性**:
  - `id`: 注文ID (int)
  - `customer`: 注文した顧客 (Customer)
  - `pet`: 注文されたペット (Pet)
  - `quantity`: 注文数 (int)
  - `orderDate`: 注文日 (Date)
- **操作**:
  - `getId()`: 注文IDを取得する
  - `getCustomer()`: 注文した顧客を取得する
  - `getPet()`: 注文されたペットを取得する
  - `getQuantity()`: 注文数を取得する
  - `getOrderDate()`: 注文日を取得する

### CustomerRepository
- **説明**: 顧客情報を管理するリポジトリ
- **属性**:
  - `customers`: 顧客情報を保持するMap (Map<int, Customer>)
- **操作**:
  - `saveCustomer(Customer)`: 顧客情報を保存する
  - `getCustomer(int)`: 顧客IDから顧客情報を取得する

### PetRepository
- **説明**: ペット情報を管理するリポジトリ
- **属性**:
  - `pets`: ペット情報を保持するMap (Map<int, Pet>)
- **操作**:
  - `savePet(Pet)`: ペット情報を保存する
  - `getPet(int)`: ペットIDからペット情報を取得する

### CustomerService
- **説明**: 顧客管理に関するサービスクラス
- **属性**:
  - `repository`: 顧客リポジトリ (CustomerRepository)
- **操作**:
  - `createCustomer(String, String, String)`: 新しい顧客を作成する
  - `getCustomer(int)`: 顧客IDから顧客情報を取得する

### PetService
- **説明**: ペット管理に関するサービスクラス
- **属性**:
  - `repository`: ペットリポジトリ (PetRepository)
- **操作**:
  - `createPet(String, PetCategory, double)`: 新しいペットを作成する
  - `getPet(int)`: ペットIDからペット情報を取得する

## 5. ユースケース

1. 顧客の登録
   - 関連クラス: `Customer`, `CustomerService`, `CustomerRepository`
   - 関連メソッド: `createCustomer(String, String, String)`, `saveCustomer(Customer)`

2. ペットの登録
   - 関連クラス: `Pet`, `PetCategory`, `PetService`, `PetRepository`
   - 関連メソッド: `createPet(String, PetCategory, double)`, `savePet(Pet)`

3. 顧客情報の表示
   - 関連クラス: `Customer`, `CustomerService`, `CustomerRepository`
   - 関連メソッド: `getCustomer(int)`

4. ペット情報の表示
   - 関連クラス: `Pet`, `PetService`, `PetRepository`
   - 関連メソッド: `getPet(int)`

5. ペットの注文
   - 関連クラス: `PetOrder`, `Customer`, `Pet`
   - 関連メソッド: `new PetOrder(Customer, Pet, int, Date)`

## 6. シーケンス図

### 顧客の登録

```
+---------------+    +---------------+    +---------------+
|   App         |    | CustomerService|    | CustomerRepository|
+---------------+    +---------------+    +---------------+
     |                      |                     |
     | createCustomer()     |                     |
     |-------------------->|                     |
     |                      | saveCustomer()     |
     |                      |-------------------->|
     |                      |                     |
     |<--------------------|                     |
     | return Customer      |                     |
     |                      |                     |
     |                      |                     |
```

### ペットの登録

```
+---------------+    +---------------+    +---------------+
|   App         |    |   PetService  |    |  PetRepository|
+---------------+    +---------------+    +---------------+
     |                      |                     |
     | createPet()          |                     |
     |-------------------->|                     |
     |                      | savePet()          |
     |                      |-------------------->|
     |                      |                     |
     |<--------------------|                     |
     | return Pet           |                     |
     |                      |                     |
     |                      |                     |
```

### 顧客情報の表示

```
+---------------+    +---------------+    +---------------+
|   App         |    | CustomerService|    | CustomerRepository|
+---------------+    +---------------+    +---------------+
     |                      |                     |
     | getCustomer()        |                     |
     |-------------------->|                     |
     |                      | getCustomer()       |
     |                      |-------------------->|
     |                      |                     |
     |<--------------------|                     |
     | return Customer      |                     |
     |                      |                     |
     |                      |                     |
```

### ペット情報の表示

```
+---------------+    +---------------+    +---------------+
|   App         |    |   PetService  |    |  PetRepository|
+---------------+    +---------------+    +---------------+
     |                      |                     |
     | getPet()             |                     |
     |-------------------->|                     |
     |                      | getPet()           |
     |                      |-------------------->|
     |                      |                     |
     |<--------------------|                     |
     | return Pet           |                     |
     |                      |                     |
     |                      |                     |
```