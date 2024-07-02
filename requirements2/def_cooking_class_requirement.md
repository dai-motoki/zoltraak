# 塾構築の要件定義書
## ゴール: 2024年料理教室開講！v4

## 1. 目的
本システムの目的は、2024年に料理教室を開講することです。この塾は、定期的に開催される講義形式の授業で、参加者に料理の知識と実践的なスキルを提供することを目的としています。

## 2. ファイル・フォルダ構成
```
root/
├── lectures/
│   ├── lecture1.md
│   ├── lecture2.md
│   ├── lecture3.md
│   └── ...
├── resources/
│   ├── images/
│   │   ├── banner.jpg
│   │   └── ...
│   └── slides/
│       ├── slide1.pdf
│       ├── slide2.pdf
│       └── ...
├── tests/
│   ├── test1.md
│   ├── test2.md
│   └── ...
├── utils/
│   ├── email.py
│   └── notification.py
├── main.py
└── README.md
```

## 3. クラス図
```
+---------------+         +---------------+
|    Lecture    |         |    Student    |
+---------------+         +---------------+
| - title: str  |         | - name: str   |
| - content: str|         | - email: str  |
| - duration: int|        | - score: int  |
+---------------+         +---------------+
      ^                           ^
      |                           |
+---------------+         +---------------+
|   Classroom   |         |  TestManager  |
+---------------+         +---------------+
| - date: date  |         | - tests: list |
| - time: time  |         | - scores: dict|
| - capacity: int|        +---------------+
+---------------+
      ^
      |
+---------------+
|  Notification |
+---------------+
| - message: str|
| - recipients: list|
+---------------+
```

## 4. クラスの詳細
### Lecture
- **説明**: 講義の内容を表すクラス
- **属性**:
    - `title`: 講義のタイトル (str)
    - `content`: 講義の内容 (str)
    - `duration`: 講義の時間 (int, 単位: 分)
- **操作**:
    - `get_content()`: 講義の内容を返す
    - `get_duration()`: 講義の時間を返す

### Student
- **説明**: 受講生を表すクラス
- **属性**:
    - `name`: 受講生の名前 (str)
    - `email`: 受講生のメールアドレス (str)
    - `score`: 受講生の成績 (int)
- **操作**:
    - `get_name()`: 受講生の名前を返す
    - `get_email()`: 受講生のメールアドレスを返す
    - `set_score(score)`: 受講生の成績を設定する

### Classroom
- **説明**: 講義を行う教室を表すクラス
- **属性**:
    - `date`: 講義の日付 (date)
    - `time`: 講義の時間 (time)
    - `capacity`: 教室の収容人数 (int)
- **操作**:
    - `get_date()`: 講義の日付を返す
    - `get_time()`: 講義の時間を返す
    - `get_capacity()`: 教室の収容人数を返す

### TestManager
- **説明**: 小テストの管理を行うクラス
- **属性**:
    - `tests`: 小テストのリスト (list)
    - `scores`: 受講生の成績 (dict)
- **操作**:
    - `add_test(test)`: 小テストを追加する
    - `get_scores()`: 受講生の成績を返す
    - `update_score(student, score)`: 受講生の成績を更新する

### Notification
- **説明**: 通知を送信するクラス
- **属性**:
    - `message`: 通知メッセージ (str)
    - `recipients`: 通知の受信者リスト (list)
- **操作**:
    - `send()`: 通知を送信する

## 4. ユースケース
1. 講義の準備
    - 関連クラス: `Lecture`, `Classroom`
    - 関連メソッド: `Lecture.get_content()`, `Lecture.get_duration()`, `Classroom.get_date()`, `Classroom.get_time()`, `Classroom.get_capacity()`
2. 受講生の管理
    - 関連クラス: `Student`, `TestManager`
    - 関連メソッド: `Student.get_name()`, `Student.get_email()`, `Student.set_score()`, `TestManager.get_scores()`, `TestManager.update_score()`
3. 通知の送信
    - 関連クラス: `Notification`
    - 関連メソッド: `Notification.send()`

## 5. シーケンス図
### 講義の実施
```
+---------------+         +---------------+         +---------------+
|   Classroom   |         |    Lecture    |         |    Student    |
+---------------+         +---------------+         +---------------+
       |                         |                         |
       | start_lecture()         | get_content()           | attend_lecture()
       |----------------------->|------------------------>|
       |                         |                         |
       |                         | get_duration()          | take_test()
       |<----------------------|<-----------------------|
       |                         |                         |
       | end_lecture()           |                         |
       |----------------------->|                         |
       |                         |                         |
```

### 小テストの実施
```
+---------------+         +---------------+         +---------------+
|  TestManager  |         |    Student    |         |  Notification  |
+---------------+         +---------------+         +---------------+
       |                         |                         |
       | add_test(test)          | take_test()             |
       |----------------------->|------------------------>|
       |                         |                         |
       | update_score(student, score)|                    |
       |<-----------------------|                         |
       |                         |                         |
       |                         |                         | send()
       |                         |<-----------------------|
       |                         |                         |
```