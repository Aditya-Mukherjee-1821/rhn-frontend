import React from "react";
import "./SinkAnalysis.css";
import SinkApiCard from "./SinkApiCard";
import logo from "../../img/logo.png"

const SinkAnalysis = () => {
  return (
    <div className="app-sink-container">
      <div className="app-sink-body">
      <div className="app-api-logo-parent">
          <img className="app-api-logo" src={logo} />
        </div>
        <p id="app-sink-header-heading-1">Sink analysis</p>
        <p id="app-sink-header-heading-4">
          Access sink API to control and simulate water discharge dynamically.
        </p>
      </div>
      <div className="app-sink-api-card-container">
        <SinkApiCard />
      </div>
    </div>
  );
};

export default SinkAnalysis;
