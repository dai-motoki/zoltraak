#!/bin/sh
echo "##active_line2##"

echo "##active_line3##"
echo "バージョンをアップデート中..."
echo "##active_line4##"
python update_version.py
echo "##active_line5##"

echo "##active_line6##"
echo "パッケージをビルド中..."
echo "##active_line7##"
python setup.py sdist bdist_wheel
echo "##active_line8##"

echo "##active_line9##"
echo "ビルドしたパッケージをPyPIにアップロード中..."
echo "##active_line10##"
twine upload dist/*
