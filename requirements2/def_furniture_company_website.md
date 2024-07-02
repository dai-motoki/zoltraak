# Furniture.AI ホームページ フロントエンド要件定義書

## 1. コンセプト
### 1.1 全体的なデザインコンセプト
家具AIサービスの魅力を最大限に引き出すデザインコンセプト。シンプルで洗練された印象を与え、ユーザーの関心を引き付ける。

## 2. ファイル・フォルダ構成
```
Furniture.AI/
├── index.html
├── css/
│   ├── reset.css
│   ├── base.css
│   └── style.css
├── js/
│   ├── main.js
│   └── vendor/
├── img/
│   ├── hero-image.jpg
│   ├── feature-icon-1.svg
│   ├── feature-icon-2.svg
│   ├── feature-icon-3.svg
│   ├── testimonial-avatar-1.jpg
│   ├── testimonial-avatar-2.jpg
│   └── client-logos/
└── fonts/
    ├── roboto-regular.woff2
    └── roboto-bold.woff2
```

## 3. 利用技術

### 3.1 HTML
- HTML5

### 3.2 CSS
- CSS3
- Sass/SCSS

### 3.3 JavaScript
- ES6
- React.js

### 3.4 素材（画像、動画など）
- 画像: JPG、SVG
- アイコン: SVG
- フォント: WOFF2

## 4. UI構造

### 4.1 全体構成
```
┌───────────────┐
│   4.2 ヘッダー │
├───────────────┤
│   4.3 メインコンテンツ   │
│   ┌──────────────┐     │
│   │ 4.3.1 ヒーロー │     │
│   └──────────────┘     │
│   ┌──────────────┐     │
│   │ 4.3.2 機能説明 │     │
│   └──────────────┘     │
│   ┌──────────────┐     │
│   │ 4.3.3 製品検索 │     │
│   └──────────────┘     │
│   ┌──────────────┐     │
│   │ 4.3.4 テスティモニアル │
│   └──────────────┘     │
│   ┌──────────────┐     │
│   │ 4.3.5 ユーザー企業ロゴ │
│   └──────────────┘     │
│   ┌──────────────┐     │
│   │ 4.3.6 コール・トゥ・アクション │
│   └──────────────┘     │
├───────────────┤
│   4.4 フッター │
└───────────────┘
```

### 4.2 ヘッダー
- ロゴ
- メインナビゲーション
- 問い合わせボタン

### 4.3 メインコンテンツ
#### 4.3.1 ヒーロー セクション
- メインビジュアル
- キャッチコピー
- 製品説明

#### 4.3.2 機能説明セクション
- 3つの主要機能のアイコンと説明

#### 4.3.3 製品検索機能セクション
- 製品検索フォーム
- 製品カテゴリー一覧

#### 4.3.4 テスティモニアル セクション
- ユーザーのテスティモニアル
- ユーザー情報

#### 4.3.5 ユーザー企業ロゴ セクション
- 導入企業のロゴ

#### 4.3.6 コール・トゥ・アクション セクション
- 無料体験のCTAボタン

### 4.4 フッター
- 会社情報
- 製品情報
- ヘルプ
- 利用規約
- プライバシーポリシー