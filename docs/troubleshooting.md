
### 課題 

| コマンド | zoltraak dev環境 | zoltraak env環境 |
|---------|------|------|
| Current directory: | /Users/motokidaisuke/motoki/zoltraak | /Users/motokidaisuke/aaaaa/zoltraak-env/lib/python3.11/site-packages/zoltraak |
| zoltraak.\_\_file\_\_ | /Users/motokidaisuke/motoki/zoltraak/\_\_init\_\_.py | /Users/motokidaisuke/aaaaa/zoltraak-env/lib/python3.11/site-packages/zoltraak/\_\_init\_\_.py |
| sys.prefix | /Users/motokidaisuke/motoki/zoltraak-dev | /Users/motokidaisuke/aaaaa/zoltraak-env |
| site.getsitepackages() | ['/Users/motokidaisuke/motoki/zoltraak-dev/lib/python3.11/site-packages'] | ['/Users/motokidaisuke/aaaaa/zoltraak-env/lib/python3.11/site-packages'] |
| install_paths = site.getsitepackages()<br>for path in install_paths:<br>&nbsp;&nbsp;&nbsp;&nbsp;print(path) | /Users/motokidaisuke/motoki/zoltraak-dev/lib/python3.11/site-packages | /Users/motokidaisuke/aaaaa/zoltraak-env/lib/python3.11/site-packages |



### 解決策

- zoltraak.\_\_file\_\_ を利用する
