# ドトール顧客分析プロダクトv6

## ゴール: ドトール顧客分析プロダクトv6
上記を満たす要件定義書を作成する。

## 1. 目的
このシステムは、ドトールの顧客行動分析を行い、マーケティング戦略立案を支援することを目的とする。顧客の購買履歴、来店頻度、商品嗜好などのデータを収集・分析し、効果的な施策立案に寄与することが目標である。

## 2. ファイル・フォルダ構成
```
ドトール顧客分析プロダクトv6/
├── src/
│   ├── main.py
│   ├── customer/
│   │   ├── CustomerData.py
│   │   ├── CustomerProfile.py
│   │   └── CustomerSegmentation.py
│   ├── analysis/
│   │   ├── PurchaseAnalysis.py
│   │   ├── VisitFrequencyAnalysis.py
│   │   └── ProductPreferenceAnalysis.py
│   └── report/
│       ├── ReportGenerator.py
│       └── ReportViewer.py
├── tests/
│   ├── test_CustomerData.py
│   ├── test_CustomerProfile.py
│   ├── test_CustomerSegmentation.py
│   ├── test_PurchaseAnalysis.py
│   ├── test_VisitFrequencyAnalysis.py
│   └── test_ProductPreferenceAnalysis.py
└── README.md
```

## 3. クラス図
```
+---------------+        +----------------+        +---------------+
|   Customer    |        |  CustomerData  |        |CustomerProfile|
+---------------+        +----------------+        +---------------+
| - customerID  |        | - customerID   |        | - customerID  |
| - name        |        | - purchaseData |        | - name        |
| - email       |        | - visitHistory |        | - email       |
| - phone       |        | - productPrefs |        | - phone       |
+---------------+        +----------------+        +---------------+
       ^                         ^                         ^
       |                         |                         |
       |                         |                         |
+---------------+        +----------------+        +---------------+
|CustomerSegment|        |PurchaseAnalysis|        |VisitFrequency |
+---------------+        +----------------+        +---------------+
| - segmentID   |        | - customerData |        | - customerData|
| - segmentName |        | - purchaseData |        | - visitHistory|
| - criteria    |        +----------------+        +---------------+
+---------------+                ^                         ^
       ^                         |                         |
       |                         |                         |
+---------------+        +----------------+        +---------------+
|ProductPreference|       |ReportGenerator|        |   ReportViewer|
+---------------+        +----------------+        +---------------+
| - customerData |        | - customerData |        | - reportData  |
| - productPrefs |        | - analysisData |        | - reportFormat|
+---------------+        +----------------+        +---------------+
```

## 4. クラスの詳細
### CustomerData
- 説明: 顧客の購買履歴、来店履歴、商品嗜好データを管理するクラス
- 属性:
  - customerID: 顧客ID (str)
  - purchaseData: 顧客の購買履歴 (list)
  - visitHistory: 顧客の来店履歴 (list)
  - productPrefs: 顧客の商品嗜好 (dict)
- 操作:
  - addPurchaseData(purchase: dict): 購買履歴を追加する
  - addVisitHistory(visit: dict): 来店履歴を追加する
  - updateProductPrefs(productID: str, preference: float): 商品嗜好を更新する

### CustomerProfile
- 説明: 顧客の基本情報を管理するクラス
- 属性:
  - customerID: 顧客ID (str)
  - name: 顧客名 (str)
  - email: 顧客メールアドレス (str)
  - phone: 顧客電話番号 (str)
- 操作:
  - updateName(name: str): 顧客名を更新する
  - updateEmail(email: str): メールアドレスを更新する
  - updatePhone(phone: str): 電話番号を更新する

### CustomerSegmentation
- 説明: 顧客をセグメント化するクラス
- 属性:
  - segmentID: セグメントID (str)
  - segmentName: セグメント名 (str)
  - criteria: セグメント化の基準 (dict)
- 操作:
  - assignCustomerToSegment(customer: CustomerData): 顧客をセグメントに割り当てる
  - updateSegmentCriteria(criteria: dict): セグメント化の基準を更新する

### PurchaseAnalysis
- 説明: 顧客の購買履歴を分析するクラス
- 属性:
  - customerData: 顧客データ (CustomerData)
  - purchaseData: 購買履歴データ (list)
- 操作:
  - analyzePurchaseFrequency(): 購買頻度を分析する
  - analyzePurchaseAmount(): 購買金額を分析する
  - analyzePurchaseItems(): 購買商品を分析する

### VisitFrequencyAnalysis
- 説明: 顧客の来店履歴を分析するクラス
- 属性:
  - customerData: 顧客データ (CustomerData)
  - visitHistory: 来店履歴データ (list)
- 操作:
  - analyzeVisitFrequency(): 来店頻度を分析する
  - analyzeVisitDuration(): 来店時間を分析する
  - analyzeVisitTime(): 来店時間帯を分析する

### ProductPreferenceAnalysis
- 説明: 顧客の商品嗜好を分析するクラス
- 属性:
  - customerData: 顧客データ (CustomerData)
  - productPrefs: 商品嗜好データ (dict)
- 操作:
  - analyzeProductPreference(): 商品嗜好を分析する
  - recommendProducts(customerID: str): 顧客に合った商品を推薦する

### ReportGenerator
- 説明: 分析結果のレポートを生成するクラス
- 属性:
  - customerData: 顧客データ (CustomerData)
  - analysisData: 分析結果データ (dict)
- 操作:
  - generateCustomerReport(customerID: str): 個別顧客レポートを生成する
  - generateSegmentReport(segmentID: str): セグメントレポートを生成する
  - generateOverallReport(): 全体レポートを生成する

### ReportViewer
- 説明: 生成されたレポートを表示するクラス
- 属性:
  - reportData: レポートデータ (dict)
  - reportFormat: レポート形式 (str)
- 操作:
  - viewReport(): レポートを表示する
  - exportReport(format: str): レポートを指定の形式でエクスポートする

## 4. ユースケース
1. 顧客情報の管理
   - 顧客の基本情報の登録・更新 (CustomerProfile)
   - 顧客の購買履歴、来店履歴、商品嗜好の管理 (CustomerData)
2. 顧客セグメンテーション
   - 顧客をセグメントに分類 (CustomerSegmentation)
   - セグメント化の基準の設定・更新 (CustomerSegmentation)
3. 顧客行動分析
   - 購買頻度、金額、商品の分析 (PurchaseAnalysis)
   - 来店頻度、時間、時間帯の分析 (VisitFrequencyAnalysis)
   - 商品嗜好の分析 (ProductPreferenceAnalysis)
4. レポート生成・表示
   - 個別顧客レポートの生成 (ReportGenerator)
   - セグメントレポートの生成 (ReportGenerator)
   - 全体レポートの生成 (ReportGenerator)
   - レポートの表示・エクスポート (ReportViewer)

## 5. シーケンス図
### 顧客情報の登録
```
+---------------+        +----------------+        +---------------+
|   Customer    |        |  CustomerData  |        |CustomerProfile|
+---------------+        +----------------+        +---------------+
        |                         |                         |
        | createCustomer()        |                         |
        |----------------------->|                         |
        |                         | createCustomerData()    |
        |                         |----------------------->|
        |                         |                         | createCustomerProfile()
        |                         |                         |----------------------->
        |                         |                         |
        |<----------------------|                         |
        |                         |                         |
        |                         |                         |
```

### 顧客セグメンテーション
```
+---------------+        +----------------+        +---------------+
|   Customer    |        |CustomerSegment |        |CustomerProfile|
+---------------+        +----------------+        +---------------+
        |                         |                         |
        | getCustomerData()        |                         |
        |----------------------->|                         |
        |                         | assignCustomerToSegment()|
        |                         |----------------------->|
        |                         |                         |
        |<----------------------|                         |
        |                         |                         |
        |                         |                         |
```

### 顧客行動分析
```
+---------------+        +----------------+        +---------------+
|   Customer    |        |PurchaseAnalysis|        |VisitFrequency |
+---------------+        +----------------+        +---------------+
        |                         |                         |
        | getCustomerData()        | analyzePurchaseFrequency()|
        |----------------------->|----------------------->|
        |                         |                         | analyzeVisitFrequency()
        |                         |<----------------------|----------------------->
        |                         |                         |
        |                         | analyzePurchaseAmount() |
        |                         |----------------------->|
        |                         |                         |
        |                         | analyzePurchaseItems() |
        |                         |----------------------->|
        |                         |                         |
        |<----------------------|                         |
        |                         |                         |
```

### レポート生成
```
+---------------+        +----------------+        +---------------+
|   Customer    |        |ReportGenerator |        |   ReportViewer|
+---------------+        +----------------+        +---------------+
        |                         |                         |
        | getCustomerData()        | generateCustomerReport()|
        |----------------------->|----------------------->|
        |                         |                         | viewReport()
        |                         |<----------------------|----------------------->
        |                         |                         |
        |                         | generateSegmentReport() |
        |                         |----------------------->|
        |                         |                         |
        |                         | generateOverallReport() |
        |                         |----------------------->|
        |                         |                         |
        |<----------------------|                         |
        |                         |                         |
```