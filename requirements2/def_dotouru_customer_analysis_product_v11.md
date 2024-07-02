# ドトール顧客分析プロダクトv11

## ゴール: ドトール顧客分析プロダクトv11
上記を満たす要件定義書を作成する。

## 1. 目的
本システムは、ドトールの顧客データを分析し、効果的な販促施策を提案することを目的とする。顧客の購買傾向や嗜好を分析し、最適なマーケティング戦略を立案することで、ドトールの売上と顧客満足度の向上を目指す。

## 2. ファイル・フォルダ構成
```
ドトール顧客分析プロダクトv11/
├── src/
│   ├── main.py
│   ├── customer/
│   │   ├── CustomerData.py
│   │   ├── CustomerProfile.py
│   │   └── CustomerSegmentation.py
│   ├── analysis/
│   │   ├── PurchaseAnalyzer.py
│   │   ├── PreferenceAnalyzer.py
│   │   └── MarketingStrategyGenerator.py
│   └── utils/
│       ├── DataLoader.py
│       └── Visualizer.py
├── tests/
│   ├── test_customer.py
│   ├── test_analysis.py
│   └── test_utils.py
└── README.md
```

## 3. クラス図
```
+---------------+          +---------------+
|   Customer    |          | PurchaseData  |
+---------------+          +---------------+
| - id: int     |          | - customer_id |
| - name: str   |          | - product_id  |
| - email: str  |          | - purchase_date|
| - phone: str  |          | - quantity    |
+---------------+          +---------------+
       |                           |
       |                           |
+---------------+          +---------------+
| CustomerProfile|          | PreferenceData|
+---------------+          +---------------+
| - interests   |          | - customer_id |
| - purchase_history|       | - product_id |
| - visit_frequency|        | - rating     |
+---------------+          +---------------+
       |                           |
       |                           |
+---------------+          +---------------+
| CustomerSegmentation|     | MarketingStrategy|
+---------------+          +---------------+
| - segment     |          | - target_segment|
| - criteria    |          | - promotion_type|
| - strategies  |          | - discount_rate |
+---------------+          +---------------+
       |                           |
       |                           |
+---------------+          +---------------+
|   DataLoader  |          |   Visualizer  |
+---------------+          +---------------+
| + loadCustomerData()|     | + generateChart()|
| + loadPurchaseData()|     | + generateReport()|
| + loadPreferenceData()|   +---------------+
+---------------+
```

## 4. クラスの詳細
### Customer
- **説明**: 顧客情報を表すクラス
- **属性**:
    - id: int - 顧客ID
    - name: str - 顧客名
    - email: str - 顧客メールアドレス
    - phone: str - 顧客電話番号
- **操作**:
    - getProfile(): CustomerProfile - 顧客プロファイルを取得する
    - updateProfile(profile: CustomerProfile): void - 顧客プロファイルを更新する

### CustomerProfile
- **説明**: 顧客のプロファイル情報を表すクラス
- **属性**:
    - interests: list[str] - 顧客の関心事
    - purchase_history: list[PurchaseData] - 顧客の購買履歴
    - visit_frequency: int - 顧客の来店頻度
- **操作**:
    - updateInterests(interests: list[str]): void - 顧客の関心事を更新する
    - addPurchaseHistory(purchase: PurchaseData): void - 購買履歴を追加する
    - updateVisitFrequency(frequency: int): void - 来店頻度を更新する

### PurchaseData
- **説明**: 顧客の購買データを表すクラス
- **属性**:
    - customer_id: int - 顧客ID
    - product_id: int - 商品ID
    - purchase_date: datetime - 購買日時
    - quantity: int - 購買数量

### PreferenceData
- **説明**: 顧客の嗜好データを表すクラス
- **属性**:
    - customer_id: int - 顧客ID
    - product_id: int - 商品ID
    - rating: float - 商品に対する評価

### CustomerSegmentation
- **説明**: 顧客をセグメント化するクラス
- **属性**:
    - segment: str - セグメントの名称
    - criteria: dict[str, Any] - セグメント化の基準
    - strategies: list[MarketingStrategy] - セグメントに対する販促戦略
- **操作**:
    - segmentCustomers(customers: list[Customer]): dict[str, list[Customer]] - 顧客をセグメント化する
    - generateStrategies(): list[MarketingStrategy] - セグメントに応じた販促戦略を生成する

### MarketingStrategy
- **説明**: 販促戦略を表すクラス
- **属性**:
    - target_segment: str - 対象セグメント
    - promotion_type: str - 販促の種類
    - discount_rate: float - 割引率

### DataLoader
- **説明**: 顧客データを読み込むクラス
- **操作**:
    - loadCustomerData(): list[Customer] - 顧客データを読み込む
    - loadPurchaseData(): list[PurchaseData] - 購買データを読み込む
    - loadPreferenceData(): list[PreferenceData] - 嗜好データを読み込む

### Visualizer
- **説明**: 分析結果を可視化するクラス
- **操作**:
    - generateChart(data: Any, chart_type: str): str - グラフを生成する
    - generateReport(strategies: list[MarketingStrategy]): str - 分析レポートを生成する

## 4. ユースケース
1. 顧客データの読み込み
    - 関連クラス: DataLoader
    - 関連メソッド: loadCustomerData(), loadPurchaseData(), loadPreferenceData()

2. 顧客セグメンテーション
    - 関連クラス: CustomerSegmentation
    - 関連メソッド: segmentCustomers(), generateStrategies()

3. 顧客の購買傾向分析
    - 関連クラス: PurchaseAnalyzer
    - 関連メソッド: analyzeCustomerPurchases()

4. 顧客の嗜好分析
    - 関連クラス: PreferenceAnalyzer
    - 関連メソッド: analyzeCustomerPreferences()

5. 販促戦略の提案
    - 関連クラス: MarketingStrategyGenerator
    - 関連メソッド: generateMarketingStrategies()

6. 分析結果の可視化
    - 関連クラス: Visualizer
    - 関連メソッド: generateChart(), generateReport()

## 5. シーケンス図
### ユースケース1: 顧客データの読み込み
```
+---------------+    +---------------+    +---------------+
|   DataLoader  |    | CustomerData  |    | PurchaseData  |
+---------------+    +---------------+    +---------------+
       |                     |                     |
       |-- loadCustomerData()->                    |
       |                     |                     |
       |<----- Customer -----+                     |
       |                     |                     |
       |-- loadPurchaseData()->                   |
       |                     |                     |
       |<----- PurchaseData --+                    |
       |                     |                     |
       |-- loadPreferenceData()->                 |
       |                     |                     |
       |<----- PreferenceData-+                    |
       |                     |                     |
       +---------------+    +---------------+    +---------------+
```

### ユースケース2: 顧客セグメンテーション
```
+---------------+    +---------------+    +---------------+
| CustomerSegmentation|    |   Customer   |    |MarketingStrategy|
+---------------+    +---------------+    +---------------+
       |                     |                     |
       |-- segmentCustomers()->                    |
       |                     |                     |
       |<---- segments ------+                     |
       |                     |                     |
       |-- generateStrategies()->                 |
       |                     |                     |
       |<---- strategies ----+                     |
       |                     |                     |
       +---------------+    +---------------+    +---------------+
```

### ユースケース3: 顧客の購買傾向分析
```
+---------------+    +---------------+    +---------------+
|  PurchaseAnalyzer|    |   Customer   |    |  PurchaseData  |
+---------------+    +---------------+    +---------------+
       |                     |                     |
       |-- analyzeCustomerPurchases()->            |
       |                     |                     |
       |<---- analysis ------+                     |
       |                     |                     |
       +---------------+    +---------------+    +---------------+
```

### ユースケース4: 顧客の嗜好分析
```
+---------------+    +---------------+    +---------------+
| PreferenceAnalyzer|    |   Customer   |    | PreferenceData |
+---------------+    +---------------+    +---------------+
       |                     |                     |
       |-- analyzeCustomerPreferences()->          |
       |                     |                     |
       |<---- analysis ------+                     |
       |                     |                     |
       +---------------+    +---------------+    +---------------+
```

### ユースケース5: 販促戦略の提案
```
+---------------+    +---------------+    +---------------+
|MarketingStrategyGenerator|    |CustomerSegmentation|    |MarketingStrategy|
+---------------+    +---------------+    +---------------+
       |                     |                     |
       |-- generateMarketingStrategies()->         |
       |                     |                     |
       |<---- strategies ----+                     |
       |                     |                     |
       +---------------+    +---------------+    +---------------+
```

### ユースケース6: 分析結果の可視化
```
+---------------+    +---------------+    +---------------+
|    Visualizer  |    |MarketingStrategy|    |   DataAnalysis |
+---------------+    +---------------+    +---------------+
       |                     |                     |
       |-- generateChart()-->|                     |
       |                     |                     |
       |<-- chart_data ------+                     |
       |                     |                     |
       |-- generateReport()-->|                     |
       |                     |                     |
       |<-- report_data -----+                     |
       |                     |                     |
       +---------------+    +---------------+    +---------------+
```