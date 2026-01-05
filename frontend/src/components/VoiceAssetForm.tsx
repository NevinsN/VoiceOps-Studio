import React, { useState } from "react";
import { createVoiceAsset } from "../api/api";

interface Props {
  projectId: number;
  onCreated: () => void;
}

const VoiceAssetForm: React.FC<Props> = ({ projectId, onCreated }) => {
  const [script, setScript] = useState("");
  const [params, setParams] = useState("{}");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await createVoiceAsset({
      project_id: projectId,
      script,
      parameters: JSON.parse(params),
    });
    setScript("");
    setParams("{}");
    onCreated();
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        placeholder="Script text"
        value={script}
        onChange={(e) => setScript(e.target.value)}
        required
      />
      <textarea
        placeholder='Parameters as JSON (e.g. {"voice":"male"})'
        value={params}
        onChange={(e) => setParams(e.target.value)}
      />
      <button type="submit">Create Voice Asset</button>
    </form>
  );
};

export default VoiceAssetForm;
