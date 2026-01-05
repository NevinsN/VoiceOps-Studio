from datetime import datetime
import uuid
from typing import Dict


class VoiceVersion(BaseModel):
    version_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    asset_id: str
    script: str
    params: Dict = {}
    file_path: str
    status: str = "pending"
    approved_at: Optional[datetime] = None
