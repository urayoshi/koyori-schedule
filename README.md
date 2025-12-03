✅ 博衣こより 配信スケジュール自動取得アプリ

🧪 概要
---
ホロライブ所属 博衣こより さんの YouTube 配信情報を
リアルタイムで自動取得し、わかりやすく分類して表示するWebアプリ です。

YouTube Data API v3 を利用し、

🔴 配信中（Live）

🕒 配信予定（Upcoming）

✅ 直近のライブラリー（ライブアーカイブ）

の3カテゴリに自動仕分けして一覧表示します。

🧰 使用技術
---
<img width="291" height="100" alt="image" src="https://github.com/user-attachments/assets/61ca478b-c264-4733-8905-731a9960432f" />

💡 工夫した点・こだわりポイント
1️⃣ YouTube API を使った実データ取得

API から配信情報（Live / Upcoming / Past）を取得

liveBroadcastContent と liveStreamingDetails を使い、
動画の状態を正確に分類 できるようにしています

2️⃣ JST（日本時間）に自動変換

APIで返される時間は UTC のため、

datetime を用いて 日本時間（UTC+9）に変換して表示

3️⃣ フロントデザインの工夫

博衣こよりさんのカラーに合わせたピンク系デザイン

LIVE / 配信予定 / アーカイブをタブ切り替えで表示

サムネイル（thumbnail）を表示し、視認性を強化

4️⃣ シンプルな構成なのでローカル実行しやすい

必要なファイルは app.py と index.html のみ

Python が使えれば、誰でもすぐ実行できるように設計しました

📁 ディレクトリ構造
---
<img width="218" height="115" alt="image" src="https://github.com/user-attachments/assets/1522bbd2-09bc-4f4b-8f12-dbfec89fc83c" />


🚀 実行方法
---
1. 必要ライブラリをインストール
pip install flask requests python-dotenv

2. YouTube APIキーを .env に保存（推奨）

.env を作成して以下を記述：

API_KEY=あなたのAPIキー


または、app.py に直接埋め込んでも動きます。

3. 起動
python app.py


ブラウザで：

http://127.0.0.1:5000


にアクセスするとアプリが開きます。

🖥 画面イメージ
---
<img width="1918" height="910" alt="image" src="https://github.com/user-attachments/assets/25067c72-950c-47ab-aee3-fb1317e29216" />
<img width="1918" height="907" alt="image" src="https://github.com/user-attachments/assets/2c1c45e4-00b3-4631-813e-c82f4fbe08b8" />
<img width="1919" height="908" alt="image" src="https://github.com/user-attachments/assets/fd0f6ebd-6756-4fe0-81df-7013b0a52041" />

⚠ 免責事項（必須）
---
本アプリは 非公式のファン制作 です。
カバー株式会社およびホロライブプロダクションとは一切関係ありません。
YouTube API 利用規約に基づき、個人利用の範囲で開発しています。
