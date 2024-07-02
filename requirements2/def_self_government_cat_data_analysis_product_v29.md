## 1. 目的
本システムは、自治体が保護する猫の情報を一元管理し、データ分析に基づいた効率的な猫の保護活動を支援することを目的とする。自治体職員は本システムを使って、保護猫の情報を登録・管理し、各種統計情報を確認することができる。また、一般ユーザーは本システムを通じて、地域の保護猫の情報を閲覧し、猫の里親募集に参加することができる。

## 2. ファイル・フォルダ構成

### フロントエンド (React)
```
frontend/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Footer.js
│   │   ├── CatList.js
│   │   ├── CatDetail.js
│   │   ├── AdoptionForm.js
│   │   └── ...
│   ├── pages/
│   │   ├── HomePage.js
│   │   ├── CatsPage.js
│   │   ├── AdoptionPage.js
│   │   └── ...
│   ├── styles/
│   │   ├── global.css
│   │   └── ...
│   ├── utils/
│   │   ├── api.js
│   │   └── ...
│   ├── App.js
│   └── index.js
├── package.json
└── README.md
```

### バックエンド (FastAPI)
```
backend/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── cats.py
│   │   ├── adoption.py
│   │   └── ...
│   ├── models/
│   │   ├── cat.py
│   │   ├── adoption.py
│   │   └── ...
│   ├── schemas/
│   │   ├── cat.py
│   │   ├── adoption.py
│   │   └── ...
│   ├── database.py
│   └── dependencies.py
├── tests/
│   ├── test_cats.py
│   ├── test_adoption.py
│   └── ...
├── alembic/
│   ├── versions/
│   └── env.py
├── requirements.txt
└── README.md
```

### diagrams/
- app_architecture.png
- sequence.png
- user_interface.png

## 3. APIエンドポイント

```
GET /cats
- 保護猫の一覧を取得

GET /cats/{cat_id}
- 指定したIDの保護猫の詳細情報を取得

POST /cats
- 新しい保護猫の情報を登録

PUT /cats/{cat_id}
- 指定したIDの保護猫の情報を更新

DELETE /cats/{cat_id}
- 指定したIDの保護猫の情報を削除

GET /adoption
- 里親募集の一覧を取得

POST /adoption
- 新しい里親募集情報を登録

PUT /adoption/{adoption_id}
- 指定したIDの里親募集情報を更新

DELETE /adoption/{adoption_id}
- 指定したIDの里親募集情報を削除
```

## 4. データモデル

```python
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Cat(Base):
    __tablename__ = "cats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    color = Column(String, nullable=False)
    description = Column(String)
    is_adopted = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    adoption = relationship("Adoption", back_populates="cat", uselist=False)

class Adoption(Base):
    __tablename__ = "adoptions"

    id = Column(Integer, primary_key=True, index=True)
    cat_id = Column(Integer, ForeignKey("cats.id"), nullable=False)
    applicant_name = Column(String, nullable=False)
    applicant_email = Column(String, nullable=False)
    applicant_phone = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    cat = relationship("Cat", back_populates="adoption")
```

## 5. Reactコンポーネント

```
App
├── Header
├── Footer
├── HomePage
│   ├── HeroSection
│   ├── StatsSection
│   └── CallToActionSection
├── CatsPage
│   ├── CatList
│   └── CatDetail
├── AdoptionPage
│   ├── AdoptionList
│   ├── AdoptionForm
│   └── AdoptionDetail
└── utils
    ├── api.js
    └── ...
```

- `App`: アプリケーションのルートコンポーネント
- `Header`: ヘッダーコンポーネント
- `Footer`: フッターコンポーネント
- `HomePage`: トップページのコンポーネント群
- `CatsPage`: 保護猫一覧ページのコンポーネント群
- `AdoptionPage`: 里親募集ページのコンポーネント群
- `utils/api.js`: APIリクエストを行うユーティリティ

## 6. ユーザーインターフェース

![user_interface.png](diagrams/user_interface.png)

- トップページ
  - ヒーローセクション: 本システムの概要を紹介
  - 統計セクション: 保護猫数や里親募集状況などの統計情報を表示
  - 呼びかけセクション: 里親募集への参加を呼びかける
- 保護猫一覧ページ
  - 保護猫の一覧を表示
  - 各保護猫の詳細情報を表示
  - 里親募集への申し込みができる
- 里親募集ページ
  - 里親募集の一覧を表示
  - 各里親募集の詳細情報を表示
  - 里親募集への申し込みフォームを表示