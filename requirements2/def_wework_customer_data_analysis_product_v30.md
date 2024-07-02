## 1. 目的
本システムは、WeWorkの顧客データを分析し、顧客の傾向を把握することが目的です。顧客の属性や利用状況、満足度などのデータを収集・分析し、WeWorkの事業戦略の立案や改善に活用することを目指します。

## 2. ファイル・フォルダ構成
```
wework-data-analysis/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── customers.py
│   │   │   │   └── reports.py
│   │   │   └── __init__.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── __init__.py
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   ├── models.py
│   │   │   └── session.py
│   │   ├── main.py
│   │   └── __init__.py
│   ├── Dockerfile
│   └── docker-compose.yml
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── CustomerTable.js
│   │   │   ├── ReportChart.js
│   │   │   └── Sidebar.js
│   │   ├── pages/
│   │   │   ├── CustomerAnalysis.js
│   │   │   └── ReportDashboard.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.js
│   │   └── index.js
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── package.json
│   └── yarn.lock
├── diagrams/
│   ├── app_architecture.png
│   └── sequence.png
└── README.md
```

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 4. APIエンドポイント
- GET /api/v1/customers: 顧客一覧を取得
- GET /api/v1/customers/{customer_id}: 特定の顧客の詳細情報を取得
- POST /api/v1/customers: 新規顧客を登録
- PUT /api/v1/customers/{customer_id}: 顧客情報を更新
- DELETE /api/v1/customers/{customer_id}: 顧客情報を削除
- GET /api/v1/reports/customer_summary: 顧客の利用状況や満足度などのサマリーレポートを取得
- GET /api/v1/reports/revenue_trends: 収益の推移レポートを取得

## 5. データモデル
### Customer
- id: int
- name: str
- email: str
- company: str
- job_title: str
- signup_date: datetime
- last_visit_date: datetime
- satisfaction_score: int

### Report
- id: int
- report_type: str
- data: JSON

## 6. Reactコンポーネント
### Sidebar
- 画面遷移を行うサイドバーコンポーネント
- props: 
  - currentPage: string
  - onNavigate: function

### CustomerTable
- 顧客一覧を表示するテーブルコンポーネント
- props:
  - customers: array of Customer
  - onCustomerSelect: function

### ReportChart
- 各種レポートをグラフ表示するコンポーネント
- props:
  - reportType: string
  - data: JSON

### CustomerAnalysis
- 顧客分析の画面を表示するページコンポーネント
- state:
  - selectedCustomer: Customer

### ReportDashboard 
- レポート表示の画面を表示するページコンポーネント
- state:
  - activeReportType: string

## 6. ユーザーインターフェース
![ユーザー画面遷移図](diagrams/app_architecture.png)