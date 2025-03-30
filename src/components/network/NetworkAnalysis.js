import React from "react";
import "./NetworkAnalysis.css";
import NetworkApiCard from "./NetworkApiCard";

const SinkAnalysis = () => {
  return (
    <div className="app-network-container">
      <div className="app-network-body">
        <p id="app-network-header-heading-1">Network analysis</p>
        <p id="app-network-header-heading-4">
          Access network API to control and simulate water discharge dynamically.
        </p>
      </div>
      <div className="app-network-api-card-container">
        <NetworkApiCard />
      </div>
    </div>
  );
};

export default SinkAnalysis;
