
## 📝 問題生成AI
講義のタイトルと概要から、問題資料の内容を生成します

<details>
<summary>🎯 入力</summary>

- 講義のタイトル (テキスト): {prompt}
</details>

<details>
<summary>📝 出力</summary>

- 4択問題を5つ生成
  - 目次（リンクで飛ぶことができるように <a id="introduction"></a> など利用）
  - 実践問題（思考力を要する基礎問題）
    - 課題と解説（5つ）
  - 4択問題
    - 回答、解説はトグルにする
    - 解説には引用を載せる
    - 形式は以下の通り
      <details>
      <summary>問題1: DALL·E 3 で生成できる画像の最大サイズは？</summary>

      - a. 512x512
      - b. 1024x1024 
      - c. 1792x1792
      - d. 2048x2048

      <details>
      <summary>回答と解説</summary>

      回答: b. 1024x1024

      DALL·E 3 では、1024x1024, 1024x1792, 1792x1024 の3つのサイズから選択できます。最大サイズは 1792x1024 です。
      </details>
      </details>
</details>

<details>
<summary>🛠️ 処理</summary>

1. 講義のタイトルと概要から、4択問題を5つ生成
2. 目次を作成（リンク付き）
4. 4択問題を5つ作成
   - 回答と解説はトグルで表示
   - 解説には引用を載せる
5. 実践問題を5つ作成
   - 思考力を要する基礎問題
</details>

<details>
<summary>⚠️ 注意</summary>

- 目次にはリンクを付ける（例: <a id="introduction"></a>）
- 4択問題の選択肢と解説は、講義の内容に即したものにする
- 解説には、講義資料からの引用を含める
</details>
