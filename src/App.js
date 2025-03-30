import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import SourceAnalysis from "./components/source/SourceAnalysis";
import SinkAnalysis from "./components/sink/SinkAnalysis";
import PipeAnalysis from "./components/pipe/PipeAnalysis";
import NetworkAnalysis from "./components/network/NetworkAnalysis"

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/sink-analysis" element={<SinkAnalysis />} />
      <Route path="/source-analysis" element={<SourceAnalysis />} />
      <Route path="/pipe-analysis" element={<PipeAnalysis />} />
      <Route path="/network-analysis" element={<NetworkAnalysis />} />
    </Routes>
  );
};

export default App;
