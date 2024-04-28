# 対応環境
Zoltraakは、MAC×Cursorで開発されています。
有志によってWindows版も開発されていますが、予期せぬエラーや想定外の動作をする可能性もあります。
ぜひ、issueへの登録/プルリクをお願いいたします。

# インストール方法
## STEP1：環境変数の設定
Zoltraakは、.env ファイルに環境変数を設定する必要があります。
.envファイルは、Zoltraakを動作させるディレクトリの配下に作成して下さい。

```
ANTHROPIC_API_KEY={Anthropicのキー}
```
※...{}は必要ありません。

## STEP2：インストール
ターミナルに以下のコマンドを入力することでZoltraakをインストールします。
```
pip install zoltraak
```

### バージョンアップしたい時
   ```sh
   pip install --upgrade zoltraak
   ```
