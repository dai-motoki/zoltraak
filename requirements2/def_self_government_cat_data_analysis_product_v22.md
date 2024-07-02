# AWSアーキテクチャ設計書
## ゴール: 自治体猫データ分析プロダクトv22

## 1. 目的
本システムの目的は自治体の猫に関するデータを収集・分析し、自治体の猫対策に役立てることである。AWSを使用することで、スケーラビリティ、可用性、セキュリティ、運用効率の高いシステムを構築できる。

## 2. AWSアーキテクチャ概要図
![](./assets/images/aws_architecture.png)

## 3. AWSサービスの選択
- **Amazon S3**: データ保管用のストレージ。大容量のデータを格納し、分析に活用できる。
- **Amazon Athena**: S3に格納されたデータをSQL形式で分析できる。
- **AWS Glue**: ETLジョブを実行し、データの抽出・変換・ロードを自動化できる。
- **Amazon Redshift**: 大規模な分析向けのデータウェアハウス。高速な分析が可能。
- **Amazon QuickSight**: 分析結果の可視化を行う。ダッシュボードの作成が簡単。
- **AWS Lambda**: サーバレスでイベント駆動型の処理を実行できる。
- **Amazon API Gateway**: APIの管理・公開を行う。
- **Amazon Cognito**: ユーザー認証を提供する。
- **AWS CloudTrail**: 管理イベントのログ記録と分析を行う。
- **Amazon CloudWatch**: リソースの監視と警報通知を行う。

## 4. 各AWSサービスの設定
### Amazon S3
- バケット名: `cat-data-bucket`
- オブジェクトのバージョン管理を有効化
- 暗号化: AES-256

### Amazon Athena
- データカタログ: AWS Glueを使用
- クエリ結果の出力先: `s3://cat-data-bucket/athena-query-results/`
- クエリ実行ロール: `athena-execution-role`

### AWS Glue
- クロールジョブ: 定期的にS3バケットをクロールし、スキーマを自動生成
- ETLジョブ: 必要に応じてデータの抽出・変換・ロードを実行

### Amazon Redshift
- クラスター名: `cat-data-cluster`
- ノードタイプ: `dc2.large`
- ノード数: 2
- データベース名: `catdata`

### Amazon QuickSight
- データソース: Amazon Redshift
- ダッシュボード: 自治体別の猫データの可視化

### AWS Lambda
- 関数名: `process-cat-data`
- トリガー: Amazon S3のPUT イベント
- 処理内容: 新しいデータが S3 に追加された際に、AWS GlueのETLジョブを起動する

### Amazon API Gateway
- API名: `cat-data-api`
- リソース: `/cats`
- メソッド: GET
- 認証: Amazon Cognito

### Amazon Cognito
- ユーザープール名: `cat-data-users`
- 認証フロー: ユーザー名とパスワードによる認証

### AWS CloudTrail
- トレイル名: `cat-data-trail`
- 記録するイベント: 全てのマネージメントイベント

### Amazon CloudWatch
- ロググループ名: `/aws/lambda/process-cat-data`
- メトリクス: Lambdaの実行時間、エラー数など

## 5. ネットワーク構成
### VPC
- CIDR ブロック: `10.0.0.0/16`

### サブネット
- パブリックサブネット (2AZ): `10.0.0.0/24`, `10.0.1.0/24`
- プライベートサブネット (2AZ): `10.0.10.0/24`, `10.0.11.0/24`

### セキュリティグループ
- `allow-ssh`: SSHアクセスを許可 (踏み台サーバ用)
- `allow-https`: HTTPSアクセスを許可 (API Gateway用)
- `allow-redshift`: Redshiftクラスターへのアクセスを許可

### NACL
- パブリックサブネット: インバウンド - HTTP/HTTPS、アウトバウンド - すべて許可
- プライベートサブネット: インバウンド - Redshift、アウトバウンド - すべて許可

## 6. 可用性と耐障害性
- マルチAZでRedshiftクラスターを構築し、高可用性を確保する。
- Lambdaはサーバレスのため、自動でスケーリングされる。
- API GatewayとCloudFrontを組み合わせ、CDNによるレイテンシの低減と可用性の向上を図る。
- CloudWatchアラームを設定し、リソースの異常を検知する。

## 7. セキュリティ対策
- IAMユーザーとロールを使ってアクセス権限を細かく設定する。
- S3バケットとRedshiftクラスターのデータを暗号化する。
- WAFを導入し、不正アクセスからAPIを保護する。
- CloudTrailでマネージメントイベントを記録し、セキュリティ監視に活用する。

## 8. 運用・保守
- CloudWatchを使ってリソースの監視とアラート通知を行う。
- CloudTrailでAPIコールやマネージメントイベントのログを取得し、セキュリティ分析に活用する。
- AWS Configで設定変更を記録し、リソースの状態を確認する。
- Lambdaの実行ログはCloudWatchログに出力され、Dashboardで可視化する。

以上のようなAWSアーキテクチャを構築することで、自治体猫データ分析プロダクトv22の要件を満たすことができる。スケーラビリティ、可用性、セキュリティ、運用効率が高く、コスト最適化にも配慮したシステムを実現できる。