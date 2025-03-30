import React, { useState } from "react";
import "./AddSink.css";
import { LoadingBar } from "../../misc/LoadingBar";
import FadingTexts from "../../misc/FadingTexts";

const AddSink = () => {
  const [loading, setLoading] = useState(false);
  const messages = ["Fetching Temperature...", "Almost Done..."];
  return (
    <div
      className="sink-api-form-add-sink"
      style={{ position: "relative", paddingBottom: "10px" }}
    >
      <div className="sink-api-form-header-add-sink">Add sink</div>
      <div className="sink-api-form-subheader-add-sink">Last Fetched:</div>
      <div className="sink-api-form-input-add-sink">
        <input placeholder="Junction ID" />
        <input placeholder="X-coordinate" />
        <input placeholder="Y-coordinate" />
        <input placeholder="Base Demand" />
      </div>
      <div className="network-api-form-fade-container">
        {loading ? (
          <FadingTexts messages={messages} />
        ) : (
          <button className="add-sink-button fade-in">Add</button>
        )}
      </div>
      {loading && <LoadingBar />}
    </div>
  );
};

export default AddSink;
