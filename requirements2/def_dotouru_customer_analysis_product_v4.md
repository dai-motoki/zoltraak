# [システム名]の要件定義書
## ゴール: ドトール顧客分析プロダクトv4

## 1. 目的
本システムは、ドトール店舗の顧客行動分析を行い、店舗運営の最適化と新規顧客の獲得を支援することを目的とする。顧客の購買履歴や店舗訪問データを分析し、顧客セグメンテーションや購買予測、最適な店舗運営施策の提案などを行う。

## 2. ファイル・フォルダ構成
```
- src/
  - main/
    - java/
      - com/
        - dottore/
          - customer/
            - CustomerProfile.java
            - CustomerSegmentation.java
            - PurchaseHistory.java
          - store/
            - StoreData.java
            - StoreAnalytics.java
          - DottoreAnalyzer.java
          - DottoreApplication.java
    - resources/
      - application.properties
  - test/
    - java/
      - com/
        - dottore/
          - customer/
            - CustomerProfileTest.java
            - CustomerSegmentationTest.java
            - PurchaseHistoryTest.java
          - store/
            - StoreDataTest.java
            - StoreAnalyticsTest.java
          - DottoreAnalyzerTest.java
- build.gradle
- README.md
```

## 3. クラス図
```
+---------------+        +---------------+
|  CustomerProfile|        |  PurchaseHistory|
+---------------+        +---------------+
| - customerId  |        | - customerId   |
| - name        |        | - purchaseDate |
| - email       |        | - productId    |
| - gender      |        | - quantity     |
| - age         |        | - amount       |
+---------------+        +---------------+
       ^                         ^
       |                         |
+---------------+        +---------------+
|CustomerSegmentation|    |   StoreData   |
+---------------+        +---------------+
| - segmentId   |        | - storeId     |
| - segmentName |        | - storeName   |
| - description |        | - location    |
| - criteria    |        | - openingHours|
+---------------+        +---------------+
       ^                         ^
       |                         |
+---------------+        +---------------+
|  StoreAnalytics|        |DottoreAnalyzer|
+---------------+        +---------------+
| - storeId     |        | - customerProfiles|
| - kpi         |        | - purchaseHistory |
| - insights    |        | - storeData       |
+---------------+        | - analyze()      |
                         +---------------+
```

## 4. クラスの詳細
### CustomerProfile
- **説明**: 顧客の基本プロファイル情報を保持するクラス
- **属性**:
  - customerId: 顧客ID (String)
  - name: 顧客名 (String)
  - email: 顧客メールアドレス (String)
  - gender: 性別 (String)
  - age: 年齢 (int)
- **操作**:
  - getCustomerId(): 顧客IDを取得する
  - getName(): 顧客名を取得する
  - getEmail(): 顧客メールアドレスを取得する
  - getGender(): 性別を取得する
  - getAge(): 年齢を取得する

### PurchaseHistory
- **説明**: 顧客の購買履歴を保持するクラス
- **属性**:
  - customerId: 顧客ID (String)
  - purchaseDate: 購買日時 (Date)
  - productId: 購入商品ID (String)
  - quantity: 購入数量 (int)
  - amount: 購入金額 (double)
- **操作**:
  - getCustomerId(): 顧客IDを取得する
  - getPurchaseDate(): 購買日時を取得する
  - getProductId(): 購入商品IDを取得する
  - getQuantity(): 購入数量を取得する
  - getAmount(): 購入金額を取得する

### CustomerSegmentation
- **説明**: 顧客をセグメント化するためのクラス
- **属性**:
  - segmentId: セグメントID (String)
  - segmentName: セグメント名 (String)
  - description: セグメントの説明 (String)
  - criteria: セグメント化の基準 (String)
- **操作**:
  - getSegmentId(): セグメントIDを取得する
  - getSegmentName(): セグメント名を取得する
  - getDescription(): セグメントの説明を取得する
  - getCriteria(): セグメント化の基準を取得する
  - segmentCustomers(customerProfiles: List<CustomerProfile>): 顧客をセグメント化する

### StoreData
- **説明**: 店舗の基本情報を保持するクラス
- **属性**:
  - storeId: 店舗ID (String)
  - storeName: 店舗名 (String)
  - location: 店舗所在地 (String)
  - openingHours: 営業時間 (String)
- **操作**:
  - getStoreId(): 店舗IDを取得する
  - getStoreName(): 店舗名を取得する
  - getLocation(): 店舗所在地を取得する
  - getOpeningHours(): 営業時間を取得する

### StoreAnalytics
- **説明**: 店舗の分析結果を保持するクラス
- **属性**:
  - storeId: 店舗ID (String)
  - kpi: 店舗KPI (Map<String, Double>)
  - insights: 店舗インサイト (Map<String, String>)
- **操作**:
  - getStoreId(): 店舗IDを取得する
  - getKpi(): 店舗KPIを取得する
  - getInsights(): 店舗インサイトを取得する
  - analyzeStore(storeData: StoreData, customerProfiles: List<CustomerProfile>, purchaseHistory: List<PurchaseHistory>): 店舗の分析を行う

### DottoreAnalyzer
- **説明**: 顧客分析と店舗分析を統合的に行うクラス
- **属性**:
  - customerProfiles: 顧客プロファイル一覧 (List<CustomerProfile>)
  - purchaseHistory: 購買履歴一覧 (List<PurchaseHistory>)
  - storeData: 店舗データ一覧 (List<StoreData>)
- **操作**:
  - analyze(): 顧客分析と店舗分析を実行する
  - getCustomerSegments(): 顧客セグメントを取得する
  - getStoreAnalytics(): 店舗分析結果を取得する

## 4. ユースケース
1. 顧客セグメンテーション
   - 関連するクラス: CustomerProfile, CustomerSegmentation
   - 関連するメソッド: CustomerSegmentation.segmentCustomers()

2. 購買予測
   - 関連するクラス: PurchaseHistory, CustomerProfile, StoreData
   - 関連するメソッド: DottoreAnalyzer.analyze()

3. 店舗運営施策の提案
   - 関連するクラス: StoreData, StoreAnalytics
   - 関連するメソッド: StoreAnalytics.analyzeStore()

## 5. シーケンス図
### ユースケース1: 顧客セグメンテーション
```
+---------------+    +---------------+    +---------------+
|DottoreAnalyzer|    |CustomerProfile|    |CustomerSegmentation|
+---------------+    +---------------+    +---------------+
       |                     |                     |
       |-- getCustomerProfiles()-->                |
       |                     |                     |
       |<-customerProfiles---|                     |
       |                     |                     |
       |--segmentCustomers(customerProfiles)-->    |
       |                     |                     |
       |<-segments-----------|                     |
       |                     |                     |
       |--getCustomerSegments()-->                 |
       |                     |                     |
       |<-customerSegments---|                     |
       |                     |                     |
```

### ユースケース2: 購買予測
```
+---------------+    +---------------+    +---------------+    +---------------+
|DottoreAnalyzer|    |PurchaseHistory|    |CustomerProfile|    |    StoreData   |
+---------------+    +---------------+    +---------------+    +---------------+
       |                     |                     |                     |
       |-- analyze()-->       |                     |                     |
       |                     |                     |                     |
       |<-purchaseHistory----|                     |                     |
       |                     |                     |                     |
       |<-customerProfiles---|                     |                     |
       |                     |                     |                     |
       |<-storeData----------|                     |                     |
       |                     |                     |                     |
       |--predictPurchases()-->                    |                     |
       |                     |                     |                     |
       |<-purchasePredictions|                     |                     |
       |                     |                     |                     |
```

### ユースケース3: 店舗運営施策の提案
```
+---------------+    +---------------+    +---------------+
|DottoreAnalyzer|    |    StoreData   |    |StoreAnalytics |
+---------------+    +---------------+    +---------------+
       |                     |                     |
       |-- analyze()-->       |                     |
       |                     |                     |
       |<-storeData----------|                     |
       |                     |                     |
       |--getStoreAnalytics()-->                   |
       |                     |                     |
       |<-storeAnalytics-----|                     |
       |                     |                     |
       |--getInsights()----->                      |
       |                     |                     |
       |<-insights-----------|                     |
       |                     |                     |
       |--recommendStrategies()-->                 |
       |                     |                     |
       |<-strategies---------|                     |
       |                     |                     |
```