from flask import Flask, render_template
import requests
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

API_KEY = "YOUR_API_KEY_HERE"  # ← 実際のキーは削除
CHANNEL_ID = "UC6eWCld0KwmyHFbAqK3V-Rw"  # 博衣こより

# ==============================
# 最新の動画IDを取得
# ==============================
def get_video_ids():
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "id",
        "channelId": CHANNEL_ID,
        "maxResults": 20,   # 20件まで取得
        "order": "date",
        "type": "video",
        "key": API_KEY
    }
    res = requests.get(url, params=params).json()
    return [item["id"]["videoId"] for item in res.get("items", [])]

# ==============================
# 各動画の詳細を取得
# ==============================
def get_video_details(video_ids):
    if not video_ids:
        return [], [], []

    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,liveStreamingDetails",
        "id": ",".join(video_ids),
        "key": API_KEY
    }
    res = requests.get(url, params=params).json()

    live_now, upcoming, archived = [], [], []
    JST = timezone(timedelta(hours=9))

    for item in res.get("items", []):
        snippet = item["snippet"]
        title = snippet["title"]
        video_id = item["id"]
        url = f"https://www.youtube.com/watch?v={video_id}"
        thumb = snippet["thumbnails"]["medium"]["url"]
        live_status = snippet.get("liveBroadcastContent", "none")
        live_info = item.get("liveStreamingDetails", {})

        # 予定・開始時刻を整形
        scheduled = live_info.get("scheduledStartTime")
        actual = live_info.get("actualStartTime")

        def fmt(dt_str):
            if not dt_str:
                return ""
            dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00")).astimezone(JST)
            return dt.strftime("%Y/%m/%d %H:%M")

        if live_status == "live":
            live_now.append({"title": title, "url": url, "thumb": thumb})
        elif live_status == "upcoming":
            upcoming.append({
                "title": title, "url": url, "thumb": thumb,
                "time": fmt(scheduled)
            })
        else:
            # 🎯 「ライブ配信アーカイブのみ」判定：過去ライブは actualStartTime がある
            if actual:
                archived.append({
                    "title": title, "url": url, "thumb": thumb,
                    "time": fmt(actual)
                })

    return live_now, upcoming, archived

@app.route("/")
def index():
    ids = get_video_ids()
    live, up, arc = get_video_details(ids)
    return render_template("index.html", live=live, up=up, arc=arc)

if __name__ == "__main__":
    app.run(debug=True)
