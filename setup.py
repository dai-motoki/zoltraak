from setuptools import setup, find_packages

setup(
    name="zoltraak",
    version="0.1.33",
    packages=find_packages(),
    # package_dir={'': '.'},  # ここでベースディレクトリを指定
    install_requires=[
        "openai",
        "anthropic",
        "groq",
        "python-dotenv",
        "pyperclip",
        "wheel",
        "diagrams"
        "google-api-python-client",  # Google APIクライアントライブラリを追加
        "google-generativeai",  # Google の生成 AI ライブラリを追加
    ],
    package_data={
        '': ['*.txt', '*.md', '*.json', '*.csv', '*.yaml', '*.yml'],
        'zoltraak': ['llms/*','utils/*', 'grimoires/**/*'],
    },
    entry_points={
        "console_scripts": [
            "zoltraak=zoltraak.cli:main",
        ],
    },
)
