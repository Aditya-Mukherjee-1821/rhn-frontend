import React, { useState } from "react";
import "./RemoveSink.css";
import { LoadingBar } from "../../misc/LoadingBar";
import FadingTexts from "../../misc/FadingTexts";

const RemoveSink = () => {
  const [loading, setLoading] = useState(false);
  const messages = ["Fetching Temperature...", "Almost Done..."];
  return (
    <div
      className="sink-api-form-remove-sink"
      style={{ position: "relative", paddingBottom: "10px" }}
    >
      <div className="sink-api-form-header-remove-sink">Remove sink</div>
      <div className="sink-api-form-subheader-remove-sink">Last Fetched:</div>
      <div className="sink-api-form-input-remove-sink">
        <input placeholder="Junction ID" />
      </div>
      <div className="network-api-form-fade-container">
        {loading ? (
          <FadingTexts messages={messages} />
        ) : (
          <button className="remove-sink-button fade-in">Remove</button>
        )}
      </div>
      {loading && <LoadingBar />}
    </div>
  );
};

export default RemoveSink;
