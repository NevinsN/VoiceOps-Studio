from fastapi import APIRouter, Body, HTTPException
from app.models.asset import VoiceAsset
from app.models.version import VoiceVersion
from app.storage.memory import ASSETS, VERSIONS
from app.services.voice_provider import VoiceProvider
from app.services.versioning import VersioningService

router = APIRouter()
voice_provider = VoiceProvider()
versioning_service = VersioningService()


# -----------------------------
# Routes
# -----------------------------

@router.post("/assets")
def create_asset(name: str = Body(...)):
    asset = VoiceAsset(name=name)
    ASSETS[asset.asset_id] = asset
    return asset
    

@router.post("/assets/{asset_id}/versions")
def create_version(asset_id: str, script: str = Body(...)):
    asset = ASSETS.get(asset_id)
    if not asset:
        raise HTTPException(404, "Asset not found")

    file_path = voice_provider.generate("temp", script)

    version = VoiceVersion(
        asset_id=asset_id,
        script=script,
        file_path=file_path
    )

    VERSIONS[version.version_id] = version
    asset.versions.append(version.version_id)

    return version
    
    
@router.post("/versions/{version_id}/approve")
def approve_version(version_id: str):
    version = VERSIONS.get(version_id)
    if not version:
        raise HTTPException(404, "Version not found")

    return versioning_service.approve(version)
