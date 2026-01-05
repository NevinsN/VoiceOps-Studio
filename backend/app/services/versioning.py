from datetime import datetime
import uuid
from typing import Dict


class VoiceVersion:
    """
    Represents a version of a voice asset.
    Encapsulates both data and behavior for workflow.
    """
    def __init__(self, asset_id: int,
                 script: str,
                 params: Dict,
                 file_path: str):
        self.version_id = str(uuid.uuid4())
        self.asset_id = asset_id
        self.script = script
        self.params = params
        self.file_path = file_path
        self.status = "draft"  # draft, review, approved, rejected
        self.created_at = datetime.now()

    # -------------------------
    # Status workflow methods
    # -------------------------
    def approve(self):
        self.status = "approved"

    def reject(self):
        self.status = "rejected"

    def submit_for_review(self):
        self.status = "review"

    # -------------------------
    # Comparison method
    # -------------------------
    def compare(self, other_version) -> Dict:
        """
        Return differences between this version and another version.
        """
        diffs = {}
        if self.script != other_version.script:
            diffs["script"] = (self.script, other_version.script)
        if self.params != other_version.params:
            diffs["params"] = (self.params, other_version.params)
        return diffs

    # -------------------------
    # Serialization
    # -------------------------
    def to_dict(self) -> Dict:
        return {
            "version_id": self.version_id,
            "asset_id": self.asset_id,
            "script": self.script,
            "params": self.params,
            "file_path": self.file_path,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }
