from fastapi import FastAPI, UploadFile
from faster_whisper import WhisperModel
import subprocess

app = FastAPI()

model = WhisperModel("base")

@app.post("/subtitle")
async def generate(video: UploadFile):

    video_path = "video.mp4"

    with open(video_path,"wb") as f:
        f.write(await video.read())

    segments, info = model.transcribe(video_path)

    result = []

    for s in segments:
        result.append({
            "start": s.start,
            "end": s.end,
            "text": s.text
        })

    return result
