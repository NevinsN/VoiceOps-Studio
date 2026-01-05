from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import router

app = FastAPI(title="VoiceOps Studio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Seerve generated audio files
app.mount("/audio", StaticFiles(directory="generated_voices"), name="audio")

app.include_router(router)
