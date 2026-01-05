from pydantic import BaseModel, Field
from typing import List
import uuid

class VoiceAsset(BaseModel):
    asset_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    versions: List[str] = []