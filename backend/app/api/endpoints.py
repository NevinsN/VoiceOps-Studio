from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from ..services.voice_provider import VoiceProvider, Script
from ..services.versioning import VoiceVersion

router = APIRouter()


# -----------------------------
# Pydantic models for requests
# -----------------------------
class ProjectCreate(BaseModel):
    name: str
    owner_id: int


class VoiceAssetCreate(BaseModel):
    project_id: int
    script: str
    parameters: Optional[dict] = {}


# -----------------------------
# In-memory storage for MVP
# -----------------------------
projects = []
voice_assets = []


# -----------------------------
# Routes
# -----------------------------
@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/projects")
def create_project(project: ProjectCreate):
    project_id = len(projects) + 1
    new_project = project.model_dump()
    new_project["id"] = project_id
    projects.append(new_project)
    return new_project


@router.get("/projects", response_model=List[dict])
def list_projects():
    return projects


@router.post("/voice_assets")
def create_voice_asset(asset: VoiceAssetCreate):
    asset_id = len(voice_assets) + 1
    new_asset = asset.model_dump()
    new_asset["id"] = asset_id

    # -----------------------------
    # Create Script object
    # -----------------------------
    script_obj = Script(asset.script, asset.parameters)

    # -----------------------------
    # Generate voice file
    # -----------------------------
    vp = VoiceProvider()
    file_path = vp.generate(script_obj)

    # -----------------------------
    # Create initial version
    # -----------------------------
    version = VoiceVersion(
        asset_id=asset_id,
        script=script_obj.text,
        params=script_obj.parameters,
        file_path=file_path
    )

    new_asset["versions"] = [version.to_dict()]
    voice_assets.append(new_asset)
    return new_asset


@router.get("/voice_assets", response_model=List[dict])
def list_voice_assets():
    return voice_assets


# -----------------------------
# Example route: approve a version
# -----------------------------
@router.put("/voice_assets/{asset_id}/versions/{version_id}/approve")
def approve_version(asset_id: int, version_id: str):
    # Find asset
    asset = next((a for a in voice_assets if a["id"] == asset_id), None)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    # Find version
    version_dict = next((v for v in asset["versions"] if
                         v["version_id"] == version_id), None)
    if not version_dict:
        raise HTTPException(status_code=404, detail="Version not found")

    # Convert dict back to VoiceVersion object
    version = VoiceVersion(
        asset_id=version_dict["asset_id"],
        script=version_dict["script"],
        params=version_dict["params"],
        file_path=version_dict["file_path"]
    )
    version.version_id = version_dict["version_id"]
    version.status = version_dict["status"]

    # Approve
    version.approve()

    # Save back to dict
    version_dict.update(version.to_dict())
    return version_dict
