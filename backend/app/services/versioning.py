from datetime import datetime
from app.models.version import VoiceVersion

class VersioningService:
    def approve(self, version: VoiceVersion) -> VoiceVersion:
        if version.status == "approved":
            return version

        version.status = "approved"
        version.approved_at = datetime.utcnow()
        return version
