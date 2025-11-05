# 博衣こより 配信スケジュール自動取得アプリ

## 🧪 概要
ホロライブ所属「博衣こより」さんのYouTube配信スケジュールを  
自動で取得して表示するWebアプリです。

Flask と YouTube Data API v3 を使用し、  
配信中・配信予定・直近のアーカイブを自動で分類して表示します。

---

## 🧰 使用技術
- Python (Flask)
- HTML / CSS
- YouTube Data API v3

---

## 💡 こだわりポイント
- 実際にAPIを利用してYouTubeのリアルタイムデータを取得  
- デザイン面で公式スケジュールサイトを参考に調整  
- 個人利用を想定し、Flaskで簡単にローカル実行可能  

---

## 🚀 実行方法
1. Pythonをインストール  
2. 以下のコマンドを実行  
   ```bash
   pip install flask requests python-dotenv
   python app.py

ブラウザで http://127.0.0.1:5000 にアクセス

このアプリは非公式のファン制作であり、
カバー株式会社およびホロライブプロダクションとは関係ありません。
