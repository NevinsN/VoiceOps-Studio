import React, { useState } from "react";
import { createProject } from "../api/api";

interface Props {
  onCreated: () => void;
}

const ProjectForm: React.FC<Props> = ({ onCreated }) => {
  const [name, setName] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await createProject({ name, owner_id: 1 }); // owner_id=1 for MVP
    setName("");
    onCreated();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Project Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />
      <button type="submit">Create Project</button>
    </form>
  );
};

export default ProjectForm;
