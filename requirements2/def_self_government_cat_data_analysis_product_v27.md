```
# システムの要件定義書
## ゴール: 自治体猫データ分析プロダクトv26

## 1. 目的
本システムは、自治体が管理する猫の情報を収集、分析し、自治体の効果的な猫対策を支援することを目的とする。猫の個体情報や位置情報、苦情・通報情報などを一元的に管理し、データに基づいた政策立案を可能にする。

## 2. ファイル・フォルダ構成
```
root/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── entity/
│   │   │           ├── repository/
│   │   │           ├── service/
│   │   │           └── controller/
│   │   └── resources/
│   │       ├── application.properties
│   │       └── log4j2.xml
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── example/
│       └── resources/
├── build.gradle
├── gradlew
├── gradlew.bat
└── settings.gradle
```

## 3. クラス図
```
+---------------+         +---------------+
|   CatEntity   |         |   LocationEntity   |
+---------------+         +---------------+
| - id: String  |         | - id: String  |
| - name: String|         | - latitude: double |
| - age: int    |         | - longitude: double|
| - gender: Gender |      | - address: String |
| - status: CatStatus |   +---------------+
+---------------+         
        |                         |
        |                         |
+---------------+         +---------------+
|   ReportEntity   |         |   ComplaintEntity   |
+---------------+         +---------------+
| - id: String  |         | - id: String  |
| - catId: String|         | - catId: String|
| - description: String |  | - description: String |
| - reportedAt: LocalDateTime |  | - reportedAt: LocalDateTime |
+---------------+         +---------------+
        |                         |
        |                         |
+---------------+         +---------------+
|   CatService   |         |   LocationService   |
+---------------+         +---------------+
| + getCatById(id: String): CatEntity |         | + getLocationByCatId(catId: String): LocationEntity |
| + createCat(cat: CatEntity): CatEntity |      | + createLocation(location: LocationEntity): LocationEntity |
| + updateCat(cat: CatEntity): CatEntity |      +---------------+
| + deleteCat(id: String): void |
+---------------+
        |                         |
        |                         |
+---------------+         +---------------+
|   ReportService   |         |   ComplaintService   |
+---------------+         +---------------+
| + getReportsByCatId(catId: String): List<ReportEntity> |         | + getComplaintsByCatId(catId: String): List<ComplaintEntity> |
| + createReport(report: ReportEntity): ReportEntity |      | + createComplaint(complaint: ComplaintEntity): ComplaintEntity |
+---------------+         +---------------+
        |                         |
        |                         |
+---------------+         +---------------+
|   CatController   |         |   LocationController   |
+---------------+         +---------------+
| + getCat(id: String): CatEntity |         | + getLocation(catId: String): LocationEntity |
| + createCat(@RequestBody cat: CatEntity): CatEntity |      | + createLocation(@RequestBody location: LocationEntity): LocationEntity |
| + updateCat(@RequestBody cat: CatEntity): CatEntity |      +---------------+
| + deleteCat(id: String): void |
+---------------+
        |                         |
        |                         |
+---------------+         +---------------+
|   ReportController   |         |   ComplaintController   |
+---------------+         +---------------+
| + getReports(catId: String): List<ReportEntity> |         | + getComplaints(catId: String): List<ComplaintEntity> |
| + createReport(@RequestBody report: ReportEntity): ReportEntity |      | + createComplaint(@RequestBody complaint: ComplaintEntity): ComplaintEntity |
+---------------+         +---------------+
```

## 4. クラスの詳細
### CatEntity
- 説明: 猫の基本情報を表すエンティティ
- 属性:
    - id: String - 猫の一意識別子
    - name: String - 猫の名前
    - age: int - 猫の年齢
    - gender: Gender - 猫の性別
    - status: CatStatus - 猫の現在の状態
- 操作:
    - なし

### LocationEntity
- 説明: 猫の位置情報を表すエンティティ
- 属性:
    - id: String - 位置情報の一意識別子
    - latitude: double - 緯度
    - longitude: double - 経度
    - address: String - 住所
- 操作:
    - なし

### ReportEntity
- 説明: 猫に関する通報情報を表すエンティティ
- 属性:
    - id: String - 通報の一意識別子
    - catId: String - 通報された猫の識別子
    - description: String - 通報の内容
    - reportedAt: LocalDateTime - 通報された日時
- 操作:
    - なし

### ComplaintEntity
- 説明: 猫に関する苦情情報を表すエンティティ
- 属性:
    - id: String - 苦情の一意識別子
    - catId: String - 苦情の対象となった猫の識別子
    - description: String - 苦情の内容
    - reportedAt: LocalDateTime - 苦情が報告された日時
- 操作:
    - なし

### CatService
- 説明: 猫の情報を管理するサービスクラス
- 属性:
    - なし
- 操作:
    - getCatById(id: String): CatEntity - 指定されたIDの猫の情報を取得する
    - createCat(cat: CatEntity): CatEntity - 新しい猫の情報を作成する
    - updateCat(cat: CatEntity): CatEntity - 既存の猫の情報を更新する
    - deleteCat(id: String): void - 指定されたIDの猫の情報を削除する

### LocationService
- 説明: 猫の位置情報を管理するサービスクラス
- 属性:
    - なし
- 操作:
    - getLocationByCatId(catId: String): LocationEntity - 指定された猫の位置情報を取得する
    - createLocation(location: LocationEntity): LocationEntity - 新しい位置情報を作成する

### ReportService
- 説明: 猫に関する通報情報を管理するサービスクラス
- 属性:
    - なし
- 操作:
    - getReportsByCatId(catId: String): List<ReportEntity> - 指定された猫に関する通報情報の一覧を取得する
    - createReport(report: ReportEntity): ReportEntity - 新しい通報情報を作成する

### ComplaintService
- 説明: 猫に関する苦情情報を管理するサービスクラス
- 属性:
    - なし
- 操作:
    - getComplaintsByCatId(catId: String): List<ComplaintEntity> - 指定された猫に関する苦情情報の一覧を取得する
    - createComplaint(complaint: ComplaintEntity): ComplaintEntity - 新しい苦情情報を作成する

### CatController
- 説明: 猫の情報に関する操作を提供するコントローラークラス
- 属性:
    - なし
- 操作:
    - getCat(id: String): CatEntity - 指定されたIDの猫の情報を取得する
    - createCat(@RequestBody cat: CatEntity): CatEntity - 新しい猫の情報を作成する
    - updateCat(@RequestBody cat: CatEntity): CatEntity - 既存の猫の情報を更新する
    - deleteCat(id: String): void - 指定されたIDの猫の情報を削除する

### LocationController
- 説明: 猫の位置情報に関する操作を提供するコントローラークラス
- 属性:
    - なし
- 操作:
    - getLocation(catId: String): LocationEntity - 指定された猫の位置情報を取得する
    - createLocation(@RequestBody location: LocationEntity): LocationEntity - 新しい位置情報を作成する

### ReportController
- 説明: 猫に関する通報情報に関する操作を提供するコントローラークラス
- 属性:
    - なし
- 操作:
    - getReports(catId: String): List<ReportEntity> - 指定された猫に関する通報情報の一覧を取得する
    - createReport(@RequestBody report: ReportEntity): ReportEntity - 新しい通報情報を作成する

### ComplaintController
- 説明: 猫に関する苦情情報に関する操作を提供するコントローラークラス
- 属性:
    - なし
- 操作:
    - getComplaints(catId: String): List<ComplaintEntity> - 指定された猫に関する苦情情報の一覧を取得する
    - createComplaint(@RequestBody complaint: ComplaintEntity): ComplaintEntity - 新しい苦情情報を作成する

## 4. ユースケース
1. 猫の情報の管理
    - 猫の基本情報の登録、更新、削除
    - 猫の位置情報の登録、更新
2. 猫に関する通報情報の管理
    - 猫に関する通報情報の登録
    - 特定の猫に関する通報情報の一覧表示
3. 猫に関する苦情情報の管理
    - 猫に関する苦情情報の登録
    - 特定の猫に関する苦情情報の一覧表示

## 5. シーケンス図
### ユースケース1: 猫の情報の管理
```
+---------------+         +---------------+         +---------------+
|   CatController   |         |   CatService   |         |   CatEntity   |
+---------------+         +---------------+         +---------------+
     createCat                   createCat                     new
         |                         |                           |
         |-------------------->    |                           |
         |                         |-------------------->      |
         |                         |       save               |
         |                         |<----------------          |
         |                         |                           |
         |<----------------        |                           |
         |       CatEntity         |                           |
         +---------------+         +---------------+         +---------------+
```

### ユースケース2: 猫に関する通報情報の管理
```
+---------------+         +---------------+         +---------------+
|   ReportController   |         |   ReportService   |         |   ReportEntity   |
+---------------+         +---------------+         +---------------+
     createReport                   createReport                     new
         |                         |                           |
         |-------------------->    |                           |
         |                         |-------------------->      |
         |                         |       save               |
         |                         |<----------------          |
         |                         |                           |
         |<----------------        |                           |
         |       ReportEntity      |                           |
         +---------------+         +---------------+         +---------------+
```

[追加の情報]
- 本システムは、自治体の猫対策を支援するための分析ツールとして開発されています。
- 猫の個体情報、位置情報、苦情・通報情報を一元的に管理し、データに基づいた政策立案を行うことを目的としています。
- 本システムは、Spring Bootフレームワークを使用して開発されています。
- 猫の個体情報、位置情報、苦情・通報情報は、関係性を持つエンティティとして設計されています。
- サービスクラスとコントローラークラスを通じて、エンティティの CRUD 操作を行うことができます。
- ユースケースに沿って、シーケンス図を作成しました。
- 今後、さらなる機能拡張や、データ分析機能の追加などを検討していきます。
```