# きつねシステム 要件定義書

## 1. 目的
本システムは、きつねに関する情報を管理し、ユーザーに提供することを目的とします。ユーザーは、きつねの特徴、行動、生態などの情報を閲覧できます。また、ユーザーは自身の経験したきつねの出来事を投稿し、共有することができます。

## 2. ファイル・フォルダ構成
```
PetCareSystem/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           ├── model/
│   │   │           │   ├── FoxInfo.java
│   │   │           │   ├── FoxReport.java
│   │   │           │   └── FoxUser.java
│   │   │           ├── controller/
│   │   │           │   ├── FoxInfoController.java
│   │   │           │   └── FoxReportController.java
│   │   │           ├── service/
│   │   │           │   ├── FoxInfoService.java
│   │   │           │   └── FoxReportService.java
│   │   │           └── view/
│   │   └── resources/
│   │       ├── application.properties
│   │       └── templates/
│   │           ├── fox_info.html
│   │           └── fox_report.html
│   └── test/
│       └── java/
│           └── com/
│               └── example/
│                   ├── controller/
│                   │   ├── FoxInfoControllerTest.java
│                   │   └── FoxReportControllerTest.java
│                   └── service/
│                       ├── FoxInfoServiceTest.java
│                       └── FoxReportServiceTest.java
├── pom.xml
└── README.md
```

## 3. クラス図
```
+---------------+        +---------------+
|    FoxInfo    |        |   FoxReport   |
+---------------+        +---------------+
| - id: int     |        | - id: int     |
| - name: String|        | - title: String|
| - description:| <1..n> | - content: String|
|    String     |        | - userId: int |
| - habitat: String|     | - createdAt: Date|
| - behavior: String|    +---------------+
| + getFoxInfo()|        |   FoxUser     |
| + updateFoxInfo()|     +---------------+
+---------------+        | - id: int     |
                         | - name: String|
                         | - email: String|
                         | - password: String|
                         | + login()     |
                         | + register()  |
                         +---------------+
```

## 4. クラスの詳細

### FoxInfo
- **クラス名**: FoxInfo
- **説明**: きつねの基本情報を管理するクラス
- **属性**:
  - `id`: int - きつねの一意識別子
  - `name`: String - きつねの名称
  - `description`: String - きつねの詳細説明
  - `habitat`: String - きつねの生息地
  - `behavior`: String - きつねの行動特性
- **操作**:
  - `getFoxInfo()`: FoxInfo - きつねの情報を取得する
  - `updateFoxInfo()`: void - きつねの情報を更新する

### FoxReport
- **クラス名**: FoxReport
- **説明**: ユーザーが投稿したきつねに関する報告を管理するクラス
- **属性**:
  - `id`: int - 報告の一意識別子
  - `title`: String - 報告のタイトル
  - `content`: String - 報告の内容
  - `userId`: int - 報告者のユーザーID
  - `createdAt`: Date - 報告の作成日時
- **操作**:
  なし

### FoxUser
- **クラス名**: FoxUser
- **説明**: システムのユーザーを管理するクラス
- **属性**:
  - `id`: int - ユーザーの一意識別子
  - `name`: String - ユーザーの名称
  - `email`: String - ユーザーのメールアドレス
  - `password`: String - ユーザーのパスワード
- **操作**:
  - `login()`: boolean - ユーザーがログインする
  - `register()`: boolean - ユーザーが新規登録する

## 5. ユースケース

1. **きつね情報の閲覧**
   - 関連クラス: FoxInfo
   - 関連メソッド: `getFoxInfo()`

2. **きつね報告の投稿**
   - 関連クラス: FoxReport, FoxUser
   - 関連メソッド: `register()`

3. **ユーザー認証**
   - 関連クラス: FoxUser
   - 関連メソッド: `login()`

## 6. シーケンス図

### ユースケース1: きつね情報の閲覧
```
+----------+       +----------+
| FoxViewer|       | FoxInfo  |
+----------+       +----------+
     |                   |
     | getFoxInfo()      |
     |------------------>|
     |                   | return FoxInfo
     |<------------------|
     | displayFoxInfo()  |
     |                   |
```

### ユースケース2: きつね報告の投稿
```
+----------+       +----------+       +----------+
| FoxUser  |       | FoxReport|       | FoxReportService|
+----------+       +----------+       +----------+
     |                   |                    |
     | register()        |                    |
     |------------------>|                    |
     |                   | createFoxReport()  |
     |                   |------------------>|
     |                   |                    | saveFoxReport()
     |                   |                    |------------------>|
     |                   |<------------------|                    |
     |                   |                    |<------------------|
     |<------------------|                    |
     |                   |                    |
```

### ユースケース3: ユーザー認証
```
+----------+       +----------+
| FoxUser  |       | FoxAuth  |
+----------+       +----------+
     |                   |
     | login()           |
     |------------------>|
     |                   | authenticate()
     |                   |------------------>|
     |                   |<------------------|
     |<------------------|                    |
     |                   |                    |
```