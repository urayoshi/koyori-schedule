import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, render_template
import requests
from datetime import datetime, timedelta, timezone

ENV_PATH = Path(__file__).with_name(".env")
load_dotenv(dotenv_path=ENV_PATH)  # Always resolve .env relative to this file.

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError(
        "API_KEY が設定されていません。.env を作成して API_KEY=あなたのキー を書いてください。"
    )

CHANNEL_ID = os.getenv("CHANNEL_ID", "UC6eWCld0KwmyHFbAqK3V-Rw")

app = Flask(__name__)

class YouTubeAPIClient:
    def __init__(self, youtube_api_key, youtube_channel_id):
        self.youtube_api_key = youtube_api_key
        self.youtube_channel_id = youtube_channel_id
        self.japan_standard_time = timezone(timedelta(hours=9))

    def search_youtube_video_ids(self, event_type: str, max_results: int):
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "id",
            "channelId": self.youtube_channel_id,
            "maxResults": max_results,
            "order": "date",
            "type": "video",
            "key": self.youtube_api_key,
        }

        if event_type:
            params["eventType"] = event_type

        youtube_api_response = requests.get(url, params=params).json()
        return [item["id"]["videoId"] for item in youtube_api_response.get("items", [])]

    def fetch_youtube_video_details(self, video_ids, expected_status=None, time_field=None):
        if not video_ids:
            return []

        url = "https://www.googleapis.com/youtube/v3/videos"
        params = {
            "part": "snippet,liveStreamingDetails",
            "id": ",".join(video_ids),
            "key": self.youtube_api_key,
        }

        youtube_api_response = requests.get(url, params=params).json()

        def format_datetime_to_jst_string(dt_str):
            if not dt_str:
                return ""
            dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00")).astimezone(self.japan_standard_time)
            return dt.strftime("%Y/%m/%d %H:%M")

        video_details_list = []

        for item in youtube_api_response.get("items", []):
            video_snippet = item["snippet"]
            live_streaming_details = item.get("liveStreamingDetails", {})
            broadcast_status = video_snippet.get("liveBroadcastContent")

            if expected_status and broadcast_status != expected_status:
                continue

            video_details_list.append({
                "id": item["id"],
                "title": video_snippet["title"],
                "url": f"https://www.youtube.com/watch?v={item['id']}",
                "thumbnail_url": video_snippet["thumbnails"].get("maxres", video_snippet["thumbnails"]["high"])["url"],
                "scheduled_time": format_datetime_to_jst_string(live_streaming_details.get(time_field)) if time_field else "",
            })

        return video_details_list

    def get_live_stream_videos(self, max_results):
        ids = self.search_youtube_video_ids("live", max_results)
        return self.fetch_youtube_video_details(ids, expected_status="live", time_field="scheduledStartTime")

    def get_upcoming_stream_videos(self, max_results):
        ids = self.search_youtube_video_ids("upcoming", max_results)
        return self.fetch_youtube_video_details(ids, expected_status="upcoming", time_field="scheduledStartTime")

    def get_archived_stream_videos(self, max_results):
        ids = self.search_youtube_video_ids("completed", max_results)
        return self.fetch_youtube_video_details(ids, time_field="actualStartTime")

def remove_duplicate_videos(primary_videos, secondary_videos):
    primary_video_ids = {v["id"] for v in primary_videos}
    return [v for v in secondary_videos if v["id"] not in primary_video_ids]

api_client = YouTubeAPIClient(API_KEY, CHANNEL_ID)

@app.route("/")
def index():
    live_videos = api_client.get_live_stream_videos(10)
    upcoming_videos_raw = api_client.get_upcoming_stream_videos(10)
    archived_videos_raw = api_client.get_archived_stream_videos(10)

    upcoming_videos = remove_duplicate_videos(live_videos, upcoming_videos_raw)
    archived_videos = remove_duplicate_videos(live_videos + upcoming_videos, archived_videos_raw)

    return render_template("index.html", live=live_videos, up=upcoming_videos, arc=archived_videos)

if __name__ == "__main__":
    app.run(debug=True)
