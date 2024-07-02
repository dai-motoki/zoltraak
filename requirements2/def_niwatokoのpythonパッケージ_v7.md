None

# 要件定義書

## ゴール
niwatokoという自然言語でプログラムを行うことのできるプログラミング言語のpythonパッケージを作成する。

## 1. 目的
このシステムの目的は、自然言語である niwatokoを使ってプログラミングができるpythonパッケージを開発することです。これにより、プログラミングの初心者やプログラミングに不慣れな人でも、自然な言語で簡単にプログラムを記述できるようになります。

## 2. ファイル・フォルダ構成

```
niwatoken/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── parser.py
│   ├── interpreter.py
│   └── executor.py
├── stdlib/
│   ├── __init__.py
│   ├── data_types.py
│   └── built_ins.py
├── examples/
│   ├── __init__.py
│   └── sample_programs.py
└── tests/
    ├── __init__.py
    ├── test_parser.py
    ├── test_interpreter.py
    └── test_executor.py
```

## 3. クラス図

```
+---------------+      +---------------+
|    Parser     |      |  Interpreter  |
+---------------+      +---------------+
| - tokens      |      | - ast         |
| - ast         |      | - symbol_table|
| + parse()     |      | + interpret() |
+---------------+      +---------------+
       ^                       ^
       |                       |
+---------------+      +---------------+
|    Executor   |      |   ASTNode     |
+---------------+      +---------------+
| - interpreter |      | - type        |
| + execute()   |      | - value       |
+---------------+      +---------------+
       ^                       ^
       |                       |
+---------------+      +---------------+
|   StdLibrary  |      |   BuiltIns    |
+---------------+      +---------------+
| - data_types  |      | - functions   |
| - built_ins   |      | + execute()   |
+---------------+      +---------------+
```

## 4. クラスの詳細

### Parser
- **説明**: niwatokoの構文を解析し、抽象構文木(AST)を生成するクラス
- **属性**:
  - `tokens`: 字句解析によって得られたトークンのリスト
  - `ast`: 構文解析によって得られた抽象構文木
- **操作**:
  - `parse()`: 入力された niwatokoのソースコードを解析し、ASTを生成する

### Interpreter
- **説明**: ASTを解釈し、プログラムの実行結果を生成するクラス
- **属性**:
  - `ast`: 解釈対象の抽象構文木
  - `symbol_table`: 変数やオブジェクトの情報を保持するシンボルテーブル
- **操作**:
  - `interpret()`: ASTを解釈し、プログラムを実行する

### Executor
- **説明**: Interpreterによって生成された実行結果を実際に実行するクラス
- **属性**:
  - `interpreter`: Interpreterのインスタンス
- **操作**:
  - `execute()`: Interpreterによって生成された実行結果を実行する

### ASTNode
- **説明**: 抽象構文木を構成する各ノードを表すクラス
- **属性**:
  - `type`: ノードの型(式、文、宣言など)
  - `value`: ノードの値
- **操作**:
  なし

### StdLibrary
- **説明**: niwatokoの標準ライブラリを提供するクラス
- **属性**:
  - `data_types`: 標準データ型の定義
  - `built_ins`: 標準組み込み関数の定義
- **操作**:
  なし

### BuiltIns
- **説明**: 標準組み込み関数を定義するクラス
- **属性**:
  - `functions`: 組み込み関数の定義
- **操作**:
  - `execute()`: 組み込み関数を実行する

## 5. ユースケース

1. **niwatokoプログラムの実行**
   - **関連クラス**:
     - Parser
     - Interpreter
     - Executor
   - **関連メソッド**:
     - `Parser.parse()`
     - `Interpreter.interpret()`
     - `Executor.execute()`

2. **niwatokoの標準ライブラリの使用**
   - **関連クラス**:
     - StdLibrary
     - BuiltIns
   - **関連メソッド**:
     - `StdLibrary.data_types`
     - `StdLibrary.built_ins`
     - `BuiltIns.execute()`

3. **niwatokoプログラムのデバッグ**
   - **関連クラス**:
     - Parser
     - Interpreter
     - Executor
   - **関連メソッド**:
     - `Parser.parse()`
     - `Interpreter.interpret()`
     - `Executor.execute()`

## 6. シーケンス図

### ユースケース1: niwatokoプログラムの実行

```
+---------------+      +---------------+      +---------------+
|    Parser     |      |  Interpreter  |      |   Executor    |
+---------------+      +---------------+      +---------------+
       |                       |                       |
       | parse(source_code)    |                       |
       |-------------------->  |                       |
       |        ast            |                       |
       |<--------------------  |                       |
       |                       | interpret(ast)        |
       |                       |-------------------->  |
       |                       |        result         |
       |                       |<--------------------  |
       |                       |                       | execute(result)
       |                       |                       |-------------------->
       |                       |                       |        output
       |                       |                       |<--------------------
```

### ユースケース2: niwatokoの標準ライブラリの使用

```
+---------------+      +---------------+
|   StdLibrary  |      |   BuiltIns    |
+---------------+      +---------------+
       |                       |
       | data_types            |
       |-------------------->  |
       |        type_info      |
       |<--------------------  |
       |                       | execute(function_call)
       |                       |-------------------->
       |                       |        result
       |                       |<--------------------
```

### ユースケース3: niwatokoプログラムのデバッグ

```
+---------------+      +---------------+      +---------------+
|    Parser     |      |  Interpreter  |      |   Executor    |
+---------------+      +---------------+      +---------------+
       |                       |                       |
       | parse(source_code)    |                       |
       |-------------------->  |                       |
       |        ast            |                       |
       |<--------------------  |                       |
       |                       | interpret(ast)        |
       |                       |-------------------->  |
       |                       |        result         |
       |                       |<--------------------  |
       |                       |                       | execute(result)
       |                       |                       |-------------------->
       |                       |                       |        output
       |                       |                       |<--------------------
```