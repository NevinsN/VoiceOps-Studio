import React, { useEffect, useState } from "react";
import { fetchProjects, fetchVoiceAssets } from "../api/api";
import ProjectForm from "../components/ProjectForm";
import VoiceAssetForm from "../components/VoiceAssetForm";
import VoiceAssetList from "../components/VoiceAssetList";

const Dashboard: React.FC = () => {
  const [projects, setProjects] = useState<any[]>([]);
  const [assets, setAssets] = useState<any[]>([]);

  const loadProjects = async () => {
    const res = await fetchProjects();
    setProjects(res.data);
  };

  const loadAssets = async () => {
    const res = await fetchVoiceAssets();
    setAssets(res.data);
  };

  useEffect(() => {
    loadProjects();
    loadAssets();
  }, []);

  return (
    <div>
      <h1>VoiceOps Studio Dashboard</h1>
      <ProjectForm onCreated={loadProjects} />
      <hr />
      {projects.map((p) => (
        <div key={p.id} style={{ border: "1px solid black", padding: 8, marginBottom: 8 }}>
          <h2>{p.name}</h2>
          <VoiceAssetForm projectId={p.id} onCreated={loadAssets} />
        </div>
      ))}
      <hr />
      <VoiceAssetList assets={assets} onUpdated={loadAssets} />
    </div>
  );
};

export default Dashboard;
