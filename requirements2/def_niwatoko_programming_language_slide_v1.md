# システム名: Niwatokoプレゼンテーションシステム

## ゴール: Reveal.jsを利用して新しいプログラミング言語、Niwatokoの解説を行いたい

## 1. 目的
このシステムの目的は、Reveal.jsを使用して新しいプログラミング言語Niwatokoの解説を行うことです。Niwatokoの特徴や使用方法、サンプルコードなどを分かりやすく説明し、ユーザーが Niwatokoの理解を深められるようにすることが目的です。

## 2. ファイル・フォルダ構成
```
- root/
  - index.html
  - css/
    - reveal.css
    - theme.css
  - js/
    - reveal.js
    - niwatoken.js
  - slides/
    - intro.md
    - features.md
    - examples.md
  - assets/
    - images/
      - logo.png
      - diagram.png
    - fonts/
      - custom-font.ttf
```

## 3. クラス図
```
+---------------+        +---------------+
|   Presenter   |        |   Slide Deck  |
+---------------+        +---------------+
| - title       |        | - slides      |
| - description |        | + addSlide()  |
| + start()     |        | + navigate()  |
| + next()      |        | + render()    |
| + prev()      |        +---------------+
+---------------+
        ^
        |
+---------------+
|   Niwatoken   |
+---------------+
| - code        |
| - description |
| + execute()   |
| + explain()   |
+---------------+
```

## 4. クラスの詳細

### Presenter
- **クラス名**: Presenter
- **説明**: プレゼンテーションの全体的な制御を担当するクラス
- **属性**:
  - `title: string`
  - `description: string`
- **操作**:
  - `start(): void`
    - プレゼンテーションを開始する
  - `next(): void`
    - 次のスライドに移動する
  - `prev(): void`
    - 前のスライドに移動する

### SlideDeck
- **クラス名**: SlideDeck
- **説明**: プレゼンテーションのスライドを管理するクラス
- **属性**:
  - `slides: Slide[]`
- **操作**:
  - `addSlide(slide: Slide): void`
    - スライドを追加する
  - `navigate(index: number): void`
    - 指定のインデックスのスライドに移動する
  - `render(): void`
    - スライドを表示する

### Niwatoken
- **クラス名**: Niwatoken
- **説明**: Niwatokoプログラミング言語の機能を提供するクラス
- **属性**:
  - `code: string`
  - `description: string`
- **操作**:
  - `execute(): string`
    - Niwatokoのコードを実行し、結果を返す
  - `explain(): string`
    - Niwatokoの機能を説明する

## 5. ユースケース

1. **Niwatokoの概要を説明する**
   - 関連クラス: Presenter, SlideDeck, Niwatoken
   - 関連メソッド: `start()`, `addSlide()`, `render()`, `explain()`

2. **Niwatokoの機能を紹介する**
   - 関連クラス: Presenter, SlideDeck, Niwatoken
   - 関連メソッド: `next()`, `addSlide()`, `render()`, `execute()`, `explain()`

3. **サンプルコードを実行して解説する**
   - 関連クラス: Presenter, SlideDeck, Niwatoken
   - 関連メソッド: `next()`, `execute()`, `explain()`

## 6. シーケンス図

1. **Niwatokoの概要を説明する**
```
+------------+ +---------------+ +-------------+
|  Presenter | |   SlideDeck   | |  Niwatoken  |
+------------+ +---------------+ +-------------+
     start()        addSlide()        explain()
         |               |                |
         |------------->|                |
         |               |--------------->|
         |               |<---------------|
         |<--------------|                |
         |               |                |
         |               |    render()    |
         |------------->|                |
         |<--------------|                |
```

2. **Niwatokoの機能を紹介する**
```
+------------+ +---------------+ +-------------+
|  Presenter | |   SlideDeck   | |  Niwatoken  |
+------------+ +---------------+ +-------------+
     next()          addSlide()        explain()
         |               |                |
         |------------->|                |
         |               |--------------->|
         |               |<---------------|
         |<--------------|                |
         |               |                |
         |               |    render()    |
         |------------->|                |
         |<--------------|                |
```

3. **サンプルコードを実行して解説する**
```
+------------+ +---------------+ +-------------+
|  Presenter | |   SlideDeck   | |  Niwatoken  |
+------------+ +---------------+ +-------------+
     next()                            execute()
         |                                  |
         |------------------------------------>
         |<------------------------------------
         |                                  |
         |                                explain()
         |                                  |
         |------------------------------------>
         |<------------------------------------
         |                                  |
         |                    render()      |
         |------------------------------------>
         |<------------------------------------|
```