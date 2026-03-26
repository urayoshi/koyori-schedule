# Koyori Schedule

Flask app for viewing Hakuikoyori YouTube stream information with YouTube Data API v3.

The app shows three categories:

- `LIVE`
- `Upcoming`
- `Archive`

## Overview

This project fetches videos from a YouTube channel and renders them in a simple web page.
Times from the API are converted to JST before display.

## Tech Stack

- Python
- Flask
- requests
- python-dotenv
- YouTube Data API v3

## Requirements

- Python 3.10 or later
- A YouTube Data API v3 key

## Setup

1. Install dependencies.

```bash
pip install flask requests python-dotenv
```

2. Create `.env`.

You can copy `example.env` and update it:

```env
API_KEY=YOUR_YOUTUBE_API_KEY
CHANNEL_ID=UC6eWCld0KwmyHFbAqK3V-Rw
```

`CHANNEL_ID` is optional. If omitted, the app uses `UC6eWCld0KwmyHFbAqK3V-Rw`.

## Run

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Environment Variables

- `API_KEY`: YouTube Data API v3 key
- `CHANNEL_ID`: target YouTube channel ID

The app loads `.env` from the same directory as `app.py`.

## Project Structure

```text
koyori-schedule/
|-- app.py
|-- .env
|-- example.env
|-- README.md
`-- templates/
    `-- index.html
```

## What The App Does

- Calls the YouTube Search API to get video IDs
- Calls the YouTube Videos API to get details
- Splits results into live, upcoming, and archived videos
- Removes duplicates between sections
- Converts timestamps to JST
- Renders the result with Flask templates

## Notes

- The app raises an error at startup if `API_KEY` is missing.
- Invalid `.env` syntax prevents environment variables from loading.
- YouTube API quota limits still apply.
