# タクシー配車システム

## 1. 目的
このシステムは、ユーザーがタクシーを呼び出し、配車を行うことを目的としています。ユーザーはスマートフォンアプリを使ってタクシーを呼び出し、乗車位置と目的地を入力することで、最寄りのタクシー運転手に配車依頼を送信できます。タクシー運転手は依頼を受け付けて、ユーザーを迎えに行くことができます。

## 2. ファイル・フォルダ構成
```
タクシー配車システム/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── model/
│   │   │           ├── controller/
│   │   │           └── view/
│   │   └── resources/
│   └── test/
│       └── java/
│           └── com/
│               └── example/
├── pom.xml
└── README.md
```

## 3. クラス図
```
+---------------+        +---------------+
|    User       |        |  TaxiDriver   |
+---------------+        +---------------+
| - name: String |        | - name: String|
| - phone: String|        | - carInfo: String|
+---------------+        +---------------+
       |                         |
       |                         |
+---------------+        +---------------+
|   TaxiRequest |        |  TaxiDispatcher|
+---------------+        +---------------+
| - pickupLocation: String| - drivers: List<TaxiDriver>|
| - destination: String  | - requests: List<TaxiRequest>|
| - status: RequestStatus| + assignDriver(TaxiRequest): TaxiDriver|
+---------------+        +---------------+
       |                         |
       |                         |
+---------------+        +---------------+
|   RequestStatus|        |    TaxiApp    |
+---------------+        +---------------+
| - PENDING     |        | - users: List<User>|
| - ASSIGNED   |        | - dispatcher: TaxiDispatcher|
| - COMPLETED  |        | + requestTaxi(User, String, String): TaxiRequest|
+---------------+        +---------------+
```

## 4. クラスの詳細

### User
- 説明: タクシーを呼び出すユーザー
- 属性:
  - name: String - ユーザー名
  - phone: String - ユーザーの電話番号
- 操作:
  - requestTaxi(pickupLocation: String, destination: String): TaxiRequest - タクシーを呼び出す

### TaxiDriver
- 説明: タクシーの運転手
- 属性:
  - name: String - 運転手の名前
  - carInfo: String - 運転手の車の情報
- 操作:
  - acceptRequest(TaxiRequest): void - タクシー配車依頼を受け入れる
  - completeTrip(TaxiRequest): void - 配車を完了する

### TaxiRequest
- 説明: ユーザーからのタクシー配車依頼
- 属性:
  - pickupLocation: String - 乗車位置
  - destination: String - 目的地
  - status: RequestStatus - 依頼の状態
- 操作:
  - getStatus(): RequestStatus - 依頼の状態を取得する
  - setStatus(RequestStatus): void - 依頼の状態を設定する

### RequestStatus
- 説明: タクシー配車依頼の状態
- 属性:
  - PENDING - 未割当
  - ASSIGNED - 割当済み
  - COMPLETED - 完了

### TaxiDispatcher
- 説明: タクシー配車を管理するディスパッチャー
- 属性:
  - drivers: List<TaxiDriver> - 利用可能なタクシー運転手のリスト
  - requests: List<TaxiRequest> - 受け付けた配車依頼のリスト
- 操作:
  - assignDriver(TaxiRequest): TaxiDriver - 最寄りの利用可能なタクシー運転手を割り当てる

### TaxiApp
- 説明: タクシー配車アプリケーション
- 属性:
  - users: List<User> - 登録ユーザーのリスト
  - dispatcher: TaxiDispatcher - タクシー配車を管理するディスパッチャー
- 操作:
  - requestTaxi(user: User, pickupLocation: String, destination: String): TaxiRequest - ユーザーからの配車依頼を受け付ける

## 4. ユースケース

1. ユーザーがタクシーを呼び出す
   - 関連クラス: User, TaxiRequest, TaxiDispatcher, TaxiApp
   - 関連メソッド: User.requestTaxi(), TaxiApp.requestTaxi(), TaxiDispatcher.assignDriver()

2. タクシー運転手が配車依頼を受け入れる
   - 関連クラス: TaxiDriver, TaxiRequest
   - 関連メソッド: TaxiDriver.acceptRequest()

3. タクシー運転手が配車を完了する
   - 関連クラス: TaxiDriver, TaxiRequest
   - 関連メソッド: TaxiDriver.completeTrip()

## 5. シーケンス図

### ユーザーがタクシーを呼び出す
```
+----------+  +---------------+  +---------------+  +--------------+
|   User   |  | TaxiRequest   |  | TaxiDispatcher|  |  TaxiDriver   |
+----------+  +---------------+  +---------------+  +--------------+
     |              |                    |                   |
     | requestTaxi()|                    |                   |
     |------------->|                    |                   |
     |              | create()           |                   |
     |              |----------------->  |                   |
     |              |                    | assignDriver()    |
     |              |                    |------------------>|
     |              |                    |                   | acceptRequest()
     |              |                    |<------------------|
     |              |                    |                   |
     |              |                    |                   |
```

### タクシー運転手が配車依頼を受け入れる
```
+---------------+  +--------------+
| TaxiRequest   |  |  TaxiDriver   |
+---------------+  +--------------+
       |                  |
       |                  | acceptRequest()
       |<-----------------|
       |                  |
       |                  |
```

### タクシー運転手が配車を完了する
```
+---------------+  +--------------+
| TaxiRequest   |  |  TaxiDriver   |
+---------------+  +--------------+
       |                  |
       |                  | completeTrip()
       |<-----------------|
       |                  |
       |                  |
```