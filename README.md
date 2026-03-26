# こより配信スケジュール

YouTube Data API v3 を使って、博衣こよりさんの配信情報を一覧表示する Flask アプリです。

このアプリでは、以下の 3 カテゴリを表示します。

- `LIVE`
- `Upcoming`
- `Archive`

## 概要

YouTube チャンネルから動画情報を取得し、ブラウザで見やすく表示するシンプルな Web アプリです。  
API から取得した時刻は JST に変換して表示します。

## 使用技術

- Python
- Flask
- requests
- python-dotenv
- YouTube Data API v3

## 動作要件

- Python 3.10 以降
- YouTube Data API v3 の API キー

## セットアップ

1. 依存パッケージをインストールします。

```bash
pip install flask requests python-dotenv
```

2. `.env` ファイルを作成します。`example.env` をコピーして編集しても構いません。

```env
API_KEY=YOUR_YOUTUBE_API_KEY
CHANNEL_ID=UC6eWCld0KwmyHFbAqK3V-Rw
```

`CHANNEL_ID` は省略可能です。未設定の場合は `UC6eWCld0KwmyHFbAqK3V-Rw` が使われます。

## 起動方法

```bash
python app.py
```

起動後、ブラウザで以下へアクセスしてください。

```text
http://127.0.0.1:5000
```

## 環境変数

- `API_KEY`: YouTube Data API v3 の API キー
- `CHANNEL_ID`: 取得対象の YouTube チャンネル ID

`.env` は `app.py` と同じディレクトリから読み込まれます。

## ディレクトリ構成

```text
koyori-schedule/
|-- app.py
|-- .env
|-- example.env
|-- README.md
`-- templates/
    `-- index.html
```

## アプリの動作

- YouTube Search API で動画 ID を取得
- YouTube Videos API で詳細情報を取得
- 動画を `LIVE`、`Upcoming`、`Archive` に分類
- セクション間の重複動画を除外
- 日時を JST に変換
- Flask テンプレートで画面表示

## 注意点

- `API_KEY` が未設定だと、起動時にエラーになります。
- `.env` の書式が正しくないと、環境変数を読み込めません。
- YouTube API のクォータ制限の影響を受けます。