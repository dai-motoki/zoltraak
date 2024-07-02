# 新プログラミング言語Niwatokoの解説システム

## ゴール: Reveal.jsを利用して新しいプログラミング言語、Niwatokoの解説を行いたい

## 1. 目的
本システムは、新しいプログラミング言語Niwatokoの解説をWebブラウザ上で行うことを目的としています。Reveal.jsを利用することで、スライド形式でわかりやすい解説を提供できるようにします。

## 2. ファイル・フォルダ構成
```
root/
├── index.html
├── css/
│   └── styles.css
├── js/
│   ├── reveal.js
│   └── app.js
├── slides/
│   ├── 01_introduction.md
│   ├── 02_syntax.md
│   ├── 03_data_types.md
│   └── 04_examples.md
└── README.md
```

## 3. クラス図
```
┌───────────────┐
│   Presenter   │
├───────────────┤
│ - slideIndex  │
│ - slides      │
├───────────────┤
│ + start()     │
│ + next()      │
│ + prev()      │
│ + goto(index) │
└───────────────┘
     ▲
     │
     │
┌───────────────┐
│    Slide     │
├───────────────┤
│ - content     │
│ - notes       │
├───────────────┤
│ + render()    │
└───────────────┘
     ▲
     │
     │
┌───────────────┐
│   Revealer   │
├───────────────┤
│ - container   │
│ - options     │
├───────────────┤
│ + initialize()│
│ + start()     │
│ + next()      │
│ + prev()      │
│ + goto(index) │
└───────────────┘
```

## 4. クラスの詳細

### Presenter
- **説明**: スライドの表示や遷移を管理するクラス
- **属性**:
  - `slideIndex`: 現在表示中のスライドのインデックス
  - `slides`: 全てのスライドオブジェクトの配列
- **操作**:
  - `start()`: 最初のスライドを表示する
  - `next()`: 次のスライドに進む
  - `prev()`: 前のスライドに戻る
  - `goto(index)`: 指定したインデックスのスライドに移動する

### Slide
- **説明**: 1つのスライドを表現するクラス
- **属性**:
  - `content`: スライドの内容
  - `notes`: スライドのノート
- **操作**:
  - `render()`: スライドの内容を表示する

### Revealer
- **説明**: Reveal.jsの機能を抽象化したクラス
- **属性**:
  - `container`: スライドを表示するコンテナ要素
  - `options`: Reveal.jsの設定オプション
- **操作**:
  - `initialize()`: Reveal.jsを初期化する
  - `start()`: スライドショーを開始する
  - `next()`: 次のスライドに進む
  - `prev()`: 前のスライドに戻る
  - `goto(index)`: 指定したインデックスのスライドに移動する

## 5. ユースケース

1. **スライドショーの開始**
   - **関連クラス**: `Presenter`, `Revealer`
   - **関連メソッド**: `Presenter.start()`, `Revealer.initialize()`, `Revealer.start()`

2. **スライドの表示**
   - **関連クラス**: `Presenter`, `Slide`, `Revealer`
   - **関連メソッド**: `Presenter.next()`, `Presenter.prev()`, `Presenter.goto()`, `Slide.render()`, `Revealer.next()`, `Revealer.prev()`, `Revealer.goto()`

3. **スライドのナビゲーション**
   - **関連クラス**: `Presenter`, `Revealer`
   - **関連メソッド**: `Presenter.next()`, `Presenter.prev()`, `Presenter.goto()`, `Revealer.next()`, `Revealer.prev()`, `Revealer.goto()`

## 6. シーケンス図

### ユースケース1: スライドショーの開始
```
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│    Presenter  │ │    Revealer   │ │     Slide     │
├───────────────┤ ├───────────────┤ ├───────────────┤
│ start()       │ │ initialize()  │ │ render()      │
│               │ │               │ │               │
│ new Slide()   │ │ new Slide()   │ │               │
│ addSlide()    │ │               │ │               │
│               │ │ start()       │ │               │
│               │ │               │ │               │
└───────────────┘ └───────────────┘ └───────────────┘
```

### ユースケース2: スライドの表示
```
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│    Presenter  │ │    Revealer   │ │     Slide     │
├───────────────┤ ├───────────────┤ ├───────────────┤
│ next()        │ │ next()        │ │ render()      │
│               │ │               │ │               │
│ getSlide()    │ │               │ │               │
│               │ │               │ │               │
│               │ │               │ │               │
└───────────────┘ └───────────────┘ └───────────────┘
```

### ユースケース3: スライドのナビゲーション
```
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│    Presenter  │ │    Revealer   │ │     Slide     │
├───────────────┤ ├───────────────┤ ├───────────────┤
│ goto(index)   │ │ goto(index)   │ │ render()      │
│               │ │               │ │               │
│ getSlide()    │ │               │ │               │
│               │ │               │ │               │
│               │ │               │ │               │
└───────────────┘ └───────────────┘ └───────────────┘
```