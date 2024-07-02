# 自治体猫データ分析プロダクトv18のAWSアーキテクチャ設計書

## ゴール: 自治体猫データ分析プロダクトv18

## 1. 目的
本システムは、自治体から収集した猫の情報を分析し、地域の猫の現状を把握し、適切な対策を立てることを目的としている。
AWSを使用することで、柔軟なスケーリング、高可用性、セキュリティの確保、運用の効率化が期待できる。

## 2. アーキテクチャ概要図
```
+------------+     +------------+     +------------+
|    S3      |     |   Lambda   |     |  DynamoDB  |
+------------+     +------------+     +------------+
     |                    |                   |
     |                    |                   |
+------------+     +------------+     +------------+
|   Kinesis  |     |   Kinesis  |     |  Athena/  |
|  Firehose  |     |  Analytics |     |  QuickSight|
+------------+     +------------+     +------------+
     |                    |                   |
     |                    |                   |
+------------+     +------------+     +------------+
|    API     |     |   EC2/ECS  |     |   Route53  |
|   Gateway  |     +------------+     +------------+
+------------+             |
     |                     |
+------------+     +------------+
|   CloudFront|     |   CloudWatch|
+------------+     +------------+
```

## 3. AWSサービスの選択
- **S3**: 猫の情報を格納するデータレイク
  - 選択理由: 大容量のデータを低コストで保管でき、データレイクとしての活用が期待できる
- **Lambda**: データ処理、分析ロジックの実行
  - 選択理由: サーバレスで手軽に実行でき、スケーリングにも優れている
- **DynamoDB**: 猫の情報を管理するデータベース
  - 選択理由: NoSQLデータベースとして、大量のデータを高速に処理できる
- **Kinesis Firehose**: 猫の情報をリアルタイムで取り込む
  - 選択理由: 大量のデータをS3やRedshiftに簡単に取り込めるため
- **Kinesis Analytics**: 猫の情報のリアルタイム分析
  - 選択理由: ストリーミングデータの分析に適しており、リアルタイムの洞察が得られる
- **Athena/QuickSight**: 猫の情報の分析と可視化
  - 選択理由: SQLクエリによる分析と、ダッシュボードによる可視化が可能
- **API Gateway**: RESTfulなAPIを提供
  - 選択理由: 外部からのアクセスを管理し、セキュリティを確保できる
- **EC2/ECS**: アプリケーションの実行基盤
  - 選択理由: 必要に応じてスケーリングできる
- **Route53**: DNSサービス
  - 選択理由: 高可用性のDNSサービスを提供する
- **CloudFront**: コンテンツ配信
  - 選択理由: ユーザーに近いエッジロケーションからコンテンツを配信できる
- **CloudWatch**: リソースの監視
  - 選択理由: AWSリソースの稼働状況を監視し、アラートを設定できる

## 4. 各AWSサービスの設定
### S3
- バケット名: `cats-data-lake`
- バージョニング: 有効
- サーバー側暗号化: AES-256

### Lambda
- 実行ロール: `cats-data-analysis-role`
- メモリサイズ: 1024MB
- タイムアウト: 3分

### DynamoDB
- テーブル名: `cats-info`
- パーティションキー: `id`
- ソートキー: `timestamp`
- 読み取り/書き込み容量: オンデマンド

### Kinesis Firehose
- デリバリーストリーム名: `cats-data-stream`
- 宛先: S3 (`cats-data-lake`)
- バッファサイズ: 5MB
- バッファ期間: 60秒

### Kinesis Analytics
- アプリケーション名: `cats-data-analysis`
- 入力ストリーム: Kinesis Firehose (`cats-data-stream`)
- SQL クエリ: 猫の情報に基づく集計処理

### Athena
- データカタログ: `cats_data_catalog`
- データベース: `cats_data`
- テーブル: `cats_info`

### QuickSight
- データソース: Athena (`cats_data`)
- ダッシュボード: 猫の情報の分析結果を可視化

### API Gateway
- API名: `cats-api`
- メソッド: GET, POST, PUT, DELETE
- 認証: IAM
- 統合先: Lambda, DynamoDB

### EC2/ECS
- インスタンスタイプ: t3.medium
- Auto Scaling: 最小2台/最大10台
- タスク定義: Docker コンテナ

### Route53
- ホストゾーン: `cats.example.com`
- レコードセット: `www.cats.example.com`

### CloudFront
- オリジン: S3 (`cats-data-lake`)
- デフォルトキャッシュ期間: 1日

### CloudWatch
- ロググループ: `/aws/lambda/cats-data-analysis`
- アラーム: CPU使用率, メモリ使用率, エラー率

## 5. ネットワーク構成
### VPC
- CIDR: `10.0.0.0/16`

### サブネット
- パブリックサブネット: `10.0.1.0/24`, `10.0.2.0/24`
- プライベートサブネット: `10.0.10.0/24`, `10.0.20.0/24`

### セキュリティグループ
- `cats-app-sg`:
  - インバウンド: HTTP(80), HTTPS(443)
  - アウトバウンド: ALL traffic
- `cats-db-sg`:
  - インバウンド: MySQL/Aurora(3306) - `cats-app-sg`
  - アウトバウンド: ALL traffic

### NACL
- パブリックサブネット: インバウンド/アウトバウンド - ALL traffic
- プライベートサブネット: インバウンド/アウトバウンド - MySQL/Aurora(3306)

## 6. 可用性と耐障害性
- マルチAZでDynamoDBとECS/EC2を構成
- Auto Scalingによる自動スケーリング
- Application Load Balancerによるロードバランシング
- CloudWatchによるモニタリングとアラート

## 7. セキュリティ対策
- IAMによるアクセス制御
- S3とDynamoDBの暗号化
- WAFによるWebアプリケーションの保護
- CloudTrailによるログ記録

## 8. 運用・保守
- CloudWatchによるリソースの監視とアラート
- CloudTrailによるAPIコールのログ記録
- AWS Configによる設定の記録と変更の追跡
- CloudWatchLogsによるログ管理