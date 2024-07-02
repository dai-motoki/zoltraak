# [自治体猫データ分析プロダクトv23]のAWSアーキテクチャ設計書

## ゴール: 自治体猫データ分析プロダクトv23

## 1. 目的
本システムは自治体の猫に関するデータを収集、分析、可視化することを目的としている。AWSを使用することで、スケーラビリティ、高可用性、セキュリティ、運用効率を確保しながら、コスト最適化を図ることができる。

## 2. ファイル・フォルダ構成
```
- frontend/
  - index.html
  - app.js
  - components/
    - Header.vue
    - Footer.vue
- backend/
  - app.py
  - models.py
  - routes.py
- infra/
  - main.tf
  - variables.tf
  - outputs.tf
- tests/
  - test_app.py
  - test_models.py
- assets/
  - images/
    - aws_architecture.png
```

## 3. AWSアーキテクチャ概要図
![](./assets/images/aws_architecture.png)

## 4. AWSサービスの選択
1. **Amazon S3**: データ保存
   - 用途: 猫データの永続化
   - 選択理由: 大容量データの格納、高可用性、低コスト

2. **Amazon RDS (PostgreSQL)**: データベース
   - 用途: 構造化データの管理
   - 選択理由: 高可用性、スケーラビリティ、管理機能

3. **AWS Lambda**: サーバーレスコンピューティング
   - 用途: バックエンドロジック
   - 選択理由: スケーラビリティ、運用効率、コスト最適化

4. **Amazon API Gateway**: API管理
   - 用途: バックエンドAPIの公開
   - 選択理由: セキュリティ、スケーラビリティ、管理機能

5. **Amazon Cognito**: ユーザー認証
   - 用途: ユーザー認証
   - 選択理由: セキュリティ、管理機能

6. **Amazon CloudWatch**: モニタリング
   - 用途: システムの監視、ログ管理
   - 選択理由: 運用効率、可視性

7. **Amazon CloudFront**: CDN
   - 用途: フロントエンドアセットの配信
   - 選択理由: パフォーマンス向上、セキュリティ

## 5. 各AWSサービスの設定
1. **Amazon S3**:
   - バケット名: `cat-data-v23`
   - バージョニング: 有効
   - アクセス制御: プライベート

2. **Amazon RDS (PostgreSQL)**:
   - エンジンバージョン: 13.7
   - インスタンスクラス: db.t3.medium
   - マルチAZデプロイ: 有効
   - バックアップ保持期間: 7日

3. **AWS Lambda**:
   - ランタイム: Python 3.9
   - メモリサイズ: 512 MB
   - タイムアウト: 10秒
   - 環境変数: DB接続情報、AWS SecretsManager認証情報

4. **Amazon API Gateway**:
   - エンドポイントタイプ: Regional
   - セキュリティ: Amazon Cognito

5. **Amazon Cognito**:
   - ユーザープール: 有効
   - 連携アプリクライアント: フロントエンド、バックエンド

6. **Amazon CloudWatch**:
   - ロググループ: `/aws/lambda/cat-data-v23-*`
   - アラーム: CPU使用率、メモリ使用率、エラー数

7. **Amazon CloudFront**:
   - オリジン: Amazon S3バケット
   - キャッシュ設定: 1時間

## 6. ネットワーク構成
- **VPCのCIDRブロック**: 10.0.0.0/16
- **サブネットの種類とCIDRブロック**:
  - パブリックサブネット: 10.0.1.0/24, 10.0.2.0/24
  - プライベートサブネット: 10.0.10.0/24, 10.0.11.0/24
- **セキュリティグループのインバウンド/アウトバウンドルール**:
  - インバウンド: HTTP(80), HTTPS(443)
  - アウトバウンド: すべて許可
- **NACLのインバウンド/アウトバウンドルール**:
  - インバウンド: HTTP(80), HTTPS(443)
  - アウトバウンド: すべて許可

## 7. 可用性と耐障害性
- **マルチAZ構成**: Amazon RDS、Amazon Cognito
- **オートスケーリング**: AWS Lambda、Amazon API Gateway
- **ロードバランシング**: Amazon API Gateway、Amazon CloudFront

## 8. セキュリティ対策
- **IAMによるアクセス制御**: サービスごとにロールを割り当て
- **暗号化**:
  - データ保存時: Amazon S3のサーバー側暗号化
  - 通信時: HTTPS
- **WAF**: Amazon API Gatewayに統合

## 9. 運用・保守
- **CloudWatch**:
  - ログ監視: AWS Lambdaのログ、Amazon RDSのスロークエリ
  - アラーム設定: CPU使用率、メモリ使用率、エラー数
- **CloudTrail**: APIコールの記録
- **AWS Config**: リソース設定の記録と変更管理

コスト最適化の観点から、以下の施策を検討する:
- 適切なインスタンスタイプの選択
- リザーブドインスタンスの活用
- 使用していないリソースの削除