# 要件定義書
## ゴール: wework顧客データ分析プロダクトv3

上記のゴールを満たすReact + FastAPIアプリケーションの要件を記述する。
オブジェクト指向の原則に従って、以下の要件を含めて要件定義書を作成する。

## 1. 目的
本システムは、weworkの顧客データを分析し、各種レポートを生成することを目的とする。
顧客の利用状況の可視化や、需要予測などの機能を持つ。

## 2. ファイル・フォルダ構成
```
├── diagrams/
│   ├── app_architecture.png
│   ├── sequence.png
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── crud.py
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── docker-compose.yml
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── utils/
│   │   └── App.js
│   ├── package.json
│   ├── Dockerfile
│   └── docker-compose.yml
└── README.md
```

フロントエンド(React)とバックエンド(FastAPI)のディレクトリ構造を分けて管理する。
各ディレクトリにはDockerとdocker-compose.ymlを作成する。

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 4. APIエンドポイント
FastAPIで実装するAPIエンドポイントは以下の通り。

| HTTPメソッド | パス | 説明 |
| --- | --- | --- |
| GET | /customers | 顧客一覧を取得 |
| GET | /customers/{customer_id} | 特定の顧客の詳細を取得 |
| POST | /customers | 新規顧客を登録 |
| PUT | /customers/{customer_id} | 顧客情報を更新 |
| DELETE | /customers/{customer_id} | 顧客を削除 |
| GET | /reports/usage | 顧客の利用状況レポートを生成 |
| GET | /reports/forecast | 需要予測レポートを生成 |

## 5. データモデル
FastAPIで使用するデータモデル(SQLAlchemyモデル)は以下の通り。

### Customer
- id: int
- name: str
- email: str
- company: str
- plan: str
- created_at: datetime
- updated_at: datetime

### Usage
- id: int
- customer_id: int
- workspace_count: int
- member_count: int
- activity_count: int
- created_at: datetime

### Forecast
- id: int
- customer_id: int
- predicted_workspace_count: int
- predicted_member_count: int
- predicted_activity_count: int
- created_at: datetime

## 6. Reactコンポーネント
アプリケーションを構成する主要なReactコンポーネントは以下の通り。

### Layout
- ヘッダー、サイドバー、フッターなどのレイアウトコンポーネント

### CustomerList
- 顧客一覧を表示するコンポーネント
- 顧客の基本情報を一覧で表示
- 検索、ソート、ページネーションなどの機能を持つ

### CustomerDetail
- 特定の顧客の詳細情報を表示するコンポーネント
- 顧客情報、利用状況、需要予測などのデータを表示

### ReportUsage
- 顧客の利用状況レポートを表示するコンポーネント
- 利用状況の推移グラフ、顧客別の利用状況などを表示

### ReportForecast
- 需要予測レポートを表示するコンポーネント
- 顧客別の需要予測グラフ、全体の需要予測などを表示

## 6. ユーザーインターフェース
![画面遷移図](diagrams/screen_transition.png)

各画面のワイヤーフレームは以下の通り。
[ワイヤーフレーム1.png]
[ワイヤーフレーム2.png]
[ワイヤーフレーム3.png]