# 戦略コンサルタント納品ドキュメント定義書

## ゴール: 今月中にビジネスコンサルティングドキュメントを作成する

上記を満たす納品ドキュメントを作成します。

## 1. 目的

戦略コンサルタントが行う課題出し、施策出し、計画立案のプロセスを効率化し、複数のパターンやアイデアを生成することで、コンサルタントの意思決定を支援する。

## 2. ファイル・フォルダ構成

- Markdown形式で戦略コンサルタントが作成するドキュメントのファイル・フォルダ構成は以下のようになります。

```
- strategic-consulting-deliverables/
  - README.md
  - issue.md
  - measure.md
  - revenue-model.md
  - plan.md
  - fermi-estimation.md
```

## 3. クラス図

以下のようなASCII文字によるクラス図を作成しました。

```
+---------------+        +---------------+
|     Issue     |        |    Measure    |
+---------------+        +---------------+
| - description |        | - description |
| - impactLevel |        | - effectivenessScore |
+---------------+        +---------------+
| + generatePatterns() |  | + generatePatterns() |
| + defineAxes()       |  | + defineAxes()       |
+---------------+        +---------------+

+---------------+        +---------------+
|  RevenueModel  |        |     Plan      |
+---------------+        +---------------+
| - revenueSources |      | - goal        |
| - pricing        |      | - timeline    |
| - salesForecast   |      | - resources   |
+---------------+        +---------------+
| + generatePatterns() |  | + generatePatterns() |
| + defineAxes()       |  | + defineAxes()       |
| + estimateRevenue()  |  +---------------+

+---------------+
| FermiEstimation |
+---------------+
| - targetValue   |
| - assumptions   |
| - calculationSteps |
+---------------+
| + estimate()    |
+---------------+
```

## 4. クラスの詳細

### Issue
- 説明: 課題を表すクラス
- 記述方法: 表形式（課題5つ、軸3つ）
- 属性:
  - description (String): 課題の説明
  - impactLevel (int): 課題の影響度
- 操作:
  - generatePatterns() (public): 複数の課題パターンを生成する
  - defineAxes() (public): 課題を分析するための軸を定義する

### Measure
- 説明: 施策を表すクラス
- 記述方法: 表形式（施策5つ、軸3つ）
- 属性:
  - description (String): 施策の説明
  - effectivenessScore (int): 施策の有効性スコア
- 操作: 
  - generatePatterns() (public): 複数の施策パターンを生成する
  - defineAxes() (public): 施策を分析するための軸を定義する

### RevenueModel
- 説明: 収益モデルを表すクラス
- 記述方法: 図、表形式（収益源、価格設定、売上予測を記載）
- 属性:
  - revenueSources (List<String>): 収益源のリスト
  - pricing (Map<String, Double>): 価格設定
  - salesForecast (Map<String, Double>): 売上予測
- 操作:
  - generatePatterns() (public): 複数の収益モデルパターンを生成する
  - defineAxes() (public): 収益モデルを分析するための軸を定義する
  - estimateRevenue() (public): 売上を予測する

### Plan
- 説明: 計画を表すクラス  
- 記述方法: 表形式（ガントチャート形式、担当者を仮設定, Marmaid記法）
- 属性:
  - goal (String): 計画の目標
  - timeline (int): 計画の期間
  - resources (Map<String, Object>): 計画に必要なリソース
- 操作:
  - generatePatterns() (public): 複数の計画パターンを生成する
  - defineAxes() (public): 計画を分析するための軸を定義する

### FermiEstimation
- 説明: フェルミ推定を行うクラス
- 記述方法: Texを利用、大学レベル以上の高度な数理モデルを記述。計算はPythonプログラムを執筆。
- 属性: 
  - targetValue (double): 推定対象の値
  - assumptions (Map<String, Double>): 推定に使用する仮定 
  - calculationSteps (List<String>): 計算ステップ
- 操作:
  - estimate() (public): フェルミ推定を実行する

## 4. 想定パターン（3つ）

1. 課題出し
   - 関連クラス: Issue
   - 関連メソッド: generatePatterns(), defineAxes()

2. 施策出し  
   - 関連クラス: Measure
   - 関連メソッド: generatePatterns(), defineAxes()

3. 計画立案
   - 関連クラス: Plan 
   - 関連メソッド: generatePatterns(), defineAxes()

4. フェルミ推定
   - 関連クラス: FermiEstimation
   - 関連メソッド: estimate()

## 5. ドキュメント作成計画立案

上記の定義に基づき、以下のような作成計画を立てます。

- 本日: README.mdの作成
- 明日: issue.md, measure.md, revenue-model.md, plan.md, fermi-estimation.mdの作成
- 明後日: クラス図の修正、全体の確認・校正
- 今週末: 納品