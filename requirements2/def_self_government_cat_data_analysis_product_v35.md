## 1. 目的
本アプリケーションは、自治体が管理する猫の情報を収集・分析し、地域の猫の現状を把握することを目的とする。行政担当者や地域住民は、このアプリケーションを通して、地域の猫の生息状況や健康状態、飼養状況などの情報を確認することができる。これにより、地域の猫の適切な管理と福祉の向上につなげることが期待される。

## 2. ファイル・フォルダ構成
```
react-app/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── CatList.js
│   │   ├── CatDetail.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── CatListPage.js
│   │   ├── CatDetailPage.js
│   │   └── ...
│   ├── services/
│   │   ├── api.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── utils/
│   │   ├── helpers.js
│   │   └── ...
│   ├── App.js
│   └── index.js
├── Dockerfile
└── docker-compose.yml

api/
├── app/
│   ├── models/
│   │   ├── cat.py
│   │   ├── user.py
│   │   └── ...
│   ├── routers/
│   │   ├── cats.py
│   │   ├── users.py
│   │   └── ...
│   ├── schemas/
│   │   ├── cat.py
│   │   ├── user.py
│   │   └── ...
│   ├── db.py
│   ├── main.py
│   └── ...
├── Dockerfile
└── docker-compose.yml
```

![シーケンス図](diagrams/sequence.png)

## 3. アーキテクチャ図
![アーキテクチャ](diagrams/app_architecture.png)

## 4. APIエンドポイント
- `GET /cats`: 登録されている全ての猫の情報を取得
- `GET /cats/{cat_id}`: 指定されたIDの猫の詳細情報を取得
- `POST /cats`: 新しい猫の情報を登録
- `PUT /cats/{cat_id}`: 指定されたIDの猫の情報を更新
- `DELETE /cats/{cat_id}`: 指定されたIDの猫の情報を削除
- `GET /users`: 登録されている全てのユーザーの情報を取得
- `GET /users/{user_id}`: 指定されたIDのユーザーの詳細情報を取得
- `POST /users`: 新しいユーザーを登録

## 5. データモデル
```python
# app/models/cat.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .base import Base

class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    breed = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    location = Column(String, nullable=False)
    health_status = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    owner = relationship("User", back_populates="cats")

# app/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, nullable=False)

    cats = relationship("Cat", back_populates="owner")
```

## 6. Reactコンポーネント
- `Header`: アプリケーションのヘッダーを表示するコンポーネント
- `CatList`: 登録されている猫の一覧を表示するコンポーネント
- `CatDetail`: 指定された猫の詳細情報を表示するコンポーネント
- `CatForm`: 猫の情報を登録/編集するためのフォームを提供するコンポーネント
- `UserList`: 登録されているユーザーの一覧を表示するコンポーネント
- `UserDetail`: 指定されたユーザーの詳細情報を表示するコンポーネント

## 7. ユーザーインターフェース
![ユーザー画面遷移図](diagrams/user_flow.png)

- **ホーム画面**: 猫の総数、新規登録数、健康状態別の内訳などの基本情報を表示
- **猫一覧画面**: 登録されている猫の一覧を表示し、詳細情報の確認や新規登録、編集が可能
- **猫詳細画面**: 選択した猫の詳細情報を表示
- **ユーザー一覧画面**: 登録されているユーザーの一覧を表示
- **ユーザー詳細画面**: 選択したユーザーの詳細情報を表示