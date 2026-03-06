from fastapi import FastAPI, UploadFile, File
import whisper

app = FastAPI()

model = whisper.load_model("base")

@app.get("/")
def home():
    return {"message": "Subtitle API Running"}

@app.post("/subtitle")
async def subtitle(file: UploadFile = File(...)):

    with open(file.filename, "wb") as f:
        f.write(await file.read())

    result = model.transcribe(file.filename)

    return {
        "subtitles": result["text"]
    }
