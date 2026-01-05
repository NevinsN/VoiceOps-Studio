import React from "react";
import { approveVersion } from "../api/api";

interface Version {
  version_id: string;
  status: string;
  file_path: string;
}

interface VoiceAsset {
  id: number;
  script: string;
  versions: Version[];
}

interface Props {
  assets: VoiceAsset[];
  onUpdated: () => void;
}

const VoiceAssetList: React.FC<Props> = ({ assets, onUpdated }) => {
  const handleApprove = async (assetId: number, versionId: string) => {
    await approveVersion(assetId, versionId);
    onUpdated();
  };

  return (
    <div>
      {assets.map((asset) => (
        <div key={asset.id} style={{ border: "1px solid gray", padding: 8, marginBottom: 8 }}>
          <p><strong>Script:</strong> {asset.script}</p>
          {asset.versions.map((v) => (
            <div key={v.version_id} style={{ marginLeft: 16 }}>
              <p>Status: {v.status}</p>
              <p>File: {v.file_path}</p>
              <button onClick={() => handleApprove(asset.id, v.version_id)}>Approve</button>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default VoiceAssetList;
