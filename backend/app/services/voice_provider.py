import os
from datetime import datetime

GENERATED_DIR = "generated_voices"

class VoiceProvider:
    def __init__(self):
        os.makedirs(GENERATED_DIR, exist_ok=True)

    def generate(self, version_id: str, script: str) -> str:
        file_path = f"{GENERATED_DIR}/{version_id}.txt"

        with open(file_path, "w") as f:
            f.write(f"Generated at {datetime.utcnow()}:\n{script}")

        return file_path
