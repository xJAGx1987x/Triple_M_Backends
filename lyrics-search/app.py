# backend/app.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os
import tempfile

app = FastAPI()

# Allow your frontend to access the backend (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or set to your domain if deployed
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/lyrics")
def get_lyrics(artist: str = Query(...), title: str = Query(...)):
    search_term = f"{artist} {title}"
    with tempfile.NamedTemporaryFile(delete=False, suffix=".lrc") as tmp:
        output_path = tmp.name

    cmd = ["syncedlyrics", search_term, "--enhanced", "-o", output_path]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
        if os.path.exists(output_path):
            with open(output_path, "r", encoding="utf-8") as f:
                lyrics = f.read()
            os.remove(output_path)
            return {"status": "success", "lyrics": lyrics}
        else:
            return {"status": "error", "message": "Lyrics not found"}
    except subprocess.TimeoutExpired:
        return {"status": "error", "message": "Timeout while fetching lyrics"}

