import axios from "axios";

const API_BASE = "http://127.0.0.1:8000";

export const api = axios.create({
    baseURL: API_BASE,
})

// Project endpoints
export const fetchProjects = () => api.get("/projects");
export const createProject = (data: {name: string; owner_id: number }) =>
    api.post("/projects", data);

// Voice asset endpoints
export const fetchVoiceAssets = () => api.get("/voice_assets");
export const createVoiceAsset = (data: { project_id: number; script: string; parameters: object }) => api.post("/voice_assets", data);

// Approve version
export const approveVersion = (asset_id: number, version_id: string) => api.put('/voice_assets/${asset_id}/versions/${version_id}/approve');