from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from backend.model import generate_captions
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

class CaptionRequest(BaseModel):
    theme: str
    tone: str
    mood: str
    platform: str
    hashtags: list

@app.post("/generate")
async def generate(req: CaptionRequest):
    captions = generate_captions(req.theme, req.tone, req.mood, req.platform, req.hashtags)
    return {"captions": captions}

@app.get("/")
async def serve_index():
    return FileResponse(os.path.join("frontend", "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
