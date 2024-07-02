# ドトール顧客分析プロダクトv13

## 1. 目的
本システムは、ドトール店舗の顧客行動を分析し、効果的な顧客サービスや販促施策の立案を支援することを目的とする。

## 2. ファイル・フォルダ構成
```
ドトール顧客分析プロダクト/
├── src/
│   ├── main.py
│   ├── customer/
│   │   ├── CustomerProfile.py
│   │   ├── CustomerSegmentation.py
│   │   └── CustomerBehaviorAnalyzer.py
│   ├── store/
│   │   ├── StoreInfo.py
│   │   └── SalesData.py
│   └── report/
│       ├── ReportGenerator.py
│       └── ReportViewer.py
├── tests/
│   ├── customer/
│   │   ├── test_CustomerProfile.py
│   │   ├── test_CustomerSegmentation.py
│   │   └── test_CustomerBehaviorAnalyzer.py
│   └── store/
│       ├── test_StoreInfo.py
│       └── test_SalesData.py
└── requirements.txt
```

## 3. クラス図
```
+---------------+         +---------------+
|   StoreInfo   |         | SalesData     |
+---------------+         +---------------+
| - storeId     |         | - storeId     |
| - storeName   |         | - salesData   |
| - location    |         +---------------+
| + getStoreInfo()|         + getSalesData()|
+---------------+         +---------------+
        ^                         ^
        |                         |
+---------------+         +---------------+
| CustomerProfile|         | CustomerSegmentation|
+---------------+         +---------------+
| - customerId  |         | - customerId  |
| - name        |         | - segment     |
| - birthDate   |         | + getSegment()|
| - gender      |         +---------------+
| + getProfile()|                 ^
+---------------+                 |
        ^                         |
        |                +---------------+
+---------------+         | CustomerBehaviorAnalyzer|
| ReportGenerator|         +---------------+
+---------------+         | - customerProfiles|
| + generateReport()|     | - salesData     |
+---------------+         | + analyze()     |
                          +---------------+
```

## 4. クラスの詳細

### StoreInfo
- 説明: 店舗情報を管理するクラス
- 属性:
  - storeId: 店舗ID
  - storeName: 店舗名
  - location: 店舗所在地
- 操作:
  - getStoreInfo(): 店舗情報を取得する

### SalesData
- 説明: 売上データを管理するクラス
- 属性:
  - storeId: 店舗ID
  - salesData: 売上データ
- 操作:
  - getSalesData(): 売上データを取得する

### CustomerProfile
- 説明: 顧客プロファイルを管理するクラス
- 属性:
  - customerId: 顧客ID
  - name: 顧客名
  - birthDate: 生年月日
  - gender: 性別
- 操作:
  - getProfile(): 顧客プロファイルを取得する

### CustomerSegmentation
- 説明: 顧客セグメンテーションを行うクラス
- 属性:
  - customerId: 顧客ID
  - segment: 顧客セグメント
- 操作:
  - getSegment(): 顧客セグメントを取得する

### CustomerBehaviorAnalyzer
- 説明: 顧客行動を分析するクラス
- 属性:
  - customerProfiles: 顧客プロファイル
  - salesData: 売上データ
- 操作:
  - analyze(): 顧客行動を分析する

### ReportGenerator
- 説明: 分析レポートを生成するクラス
- 操作:
  - generateReport(): 分析レポートを生成する

## 4. ユースケース

1. 顧客プロファイルの取得
   - 関連クラス: CustomerProfile
   - 関連メソッド: getProfile()

2. 顧客セグメンテーション
   - 関連クラス: CustomerSegmentation
   - 関連メソッド: getSegment()

3. 顧客行動分析
   - 関連クラス: CustomerBehaviorAnalyzer
   - 関連メソッド: analyze()

4. 分析レポートの生成
   - 関連クラス: ReportGenerator
   - 関連メソッド: generateReport()

## 5. シーケンス図

### ユースケース1: 顧客プロファイルの取得
```
+---------------+         +---------------+
|   Application |         | CustomerProfile|
+---------------+         +---------------+
     | getCustomerProfile() |               
     |---------------------->|               
     |                       | getProfile()  
     |<----------------------|               
     |   customerProfile     |               
     |<----------------------|               
     |                       |               
```

### ユースケース2: 顧客セグメンテーション
```
+---------------+         +---------------+
|   Application |         | CustomerSegmentation|
+---------------+         +---------------+
     | getCustomerSegment()  |               
     |---------------------->|               
     |                       | getSegment()  
     |<----------------------|               
     |   customerSegment     |               
     |<----------------------|               
     |                       |               
```

### ユースケース3: 顧客行動分析
```
+---------------+         +---------------+         +---------------+
|   Application |         | CustomerBehaviorAnalyzer|         | SalesData     |
+---------------+         +---------------+         +---------------+
     | analyzeCustomerBehavior()|             |                       
     |---------------------->|             |                       
     |                       | analyze()    |                       
     |                       |------------>|                       
     |                       |             | getSalesData()        
     |                       |<------------|                       
     |                       |             |   salesData          
     |                       |<------------|                       
     |   customerAnalysis    |             |                       
     |<----------------------|             |                       
     |                       |             |                       
```

### ユースケース4: 分析レポートの生成
```
+---------------+         +---------------+
|   Application |         | ReportGenerator|
+---------------+         +---------------+
     | generateReport()     |               
     |---------------------->|               
     |                       | generateReport()
     |<----------------------|               
     |   analysisReport      |               
     |<----------------------|               
     |                       |               
```