# React + FastAPI アプリケーションの要件定義書
## ゴール: かぞく情報データ分析v5

## 1. 目的
本システムは、家族情報の管理と分析を目的としています。
ユーザーは家族構成や家族の属性情報を登録・管理し、データ分析機能を使って
家族の傾向を把握することができます。

## 2. ファイル・フォルダ構成

### フロントエンド (React)
```
/frontend
  /src
    /components
      App.js
      Header.js
      FamilyList.js
      FamilyDetail.js
      FamilyForm.js
      DataAnalysis.js
    /utils
      api.js
    index.js
  package.json
  webpack.config.js
```

### バックエンド (FastAPI)
```
/backend
  /app
    /models
      family.py
    /schemas
      family.py
    /api
      family.py
    main.py
  requirements.txt
  alembic
  docker
```

## 3. APIエンドポイント

| HTTPメソッド | パス | 説明 |
| --- | --- | --- |
| GET | /api/families | 家族情報の一覧を取得 |
| POST | /api/families | 新しい家族情報を登録 |
| GET | /api/families/{family_id} | 指定した家族情報を取得 |
| PUT | /api/families/{family_id} | 指定した家族情報を更新 |
| DELETE | /api/families/{family_id} | 指定した家族情報を削除 |
| GET | /api/analysis/demographics | 家族構成に関する統計情報を取得 |
| GET | /api/analysis/trends | 家族属性の推移を取得 |

## 4. データモデル

### Family
- id: int
- name: str
- members: List[FamilyMember]
- created_at: datetime
- updated_at: datetime

### FamilyMember
- id: int
- family_id: int
- name: str
- age: int
- gender: str
- relationship: str
- created_at: datetime
- updated_at: datetime

## 5. Reactコンポーネント

### App
- 全体のレイアウトを管理
- Headerとメインコンテンツを表示

### Header
- アプリケーションのヘッダーを表示
- ナビゲーションリンクを提供

### FamilyList
- 登録された家族情報の一覧を表示
- 各家族の詳細ページへのリンクを提供

### FamilyDetail
- 選択された家族の詳細情報を表示
- 家族メンバーの一覧を表示
- 家族情報の編集機能を提供

### FamilyForm
- 新規の家族情報を登録するためのフォームを表示
- 家族情報の更新機能を提供

### DataAnalysis
- 家族構成や属性の統計情報を表示
- 家族の傾向を分析するためのグラフを表示

## 6. ユーザーインターフェース

### 画面遷移図
![画面遷移図](transition_diagram.png)

### ワイヤーフレーム
- [FamilyList画面のワイヤーフレーム](family_list_wireframe.png)
- [FamilyDetail画面のワイヤーフレーム](family_detail_wireframe.png)
- [DataAnalysis画面のワイヤーフレーム](data_analysis_wireframe.png)