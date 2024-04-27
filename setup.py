from setuptools import setup, find_packages

setup(
    name="zoltraak",
    version="0.1.24",
    packages=find_packages(),
    # package_dir={'': '.'},  # ここでベースディレクトリを指定
    install_requires=[
        "openai",
        "anthropic",
        "groq",
        "python-dotenv",
        "pyperclip",
        "wheel"
    ],
    package_data={
        '': ['*.txt', '*.md', '*.json', '*.csv', '*.yaml', '*.yml'],
        'zoltraak': ['llms/*','utils/*', 'setting/**/*'],
    },
    entry_points={
        "console_scripts": [
            "zoltraak=zoltraak.cli:main",
        ],
    },
)
