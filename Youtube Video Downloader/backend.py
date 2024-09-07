from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins =["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers = ["*"]
)

import os
import yt_dlp as youtube_dl # type: ignore
curl_dir = os.getcwd()
@app.post("/download")
def download_video(link: str = Form(...)):
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(curl_dir , "file_name.mp4")
    }
    with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"message": "Video download started successfully"}