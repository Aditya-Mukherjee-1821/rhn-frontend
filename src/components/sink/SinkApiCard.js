import React, { useState } from "react";
import "./SinkApiCard.css";
import RemoveSink from "./sinkAPIcomponents/RemoveSink";
import AddSink from "./sinkAPIcomponents/AddSink";

const SinkApiCard = () => {
  const [api, setApi] = useState("Remove sink");

  return (
    <div className="sink-api-card">
      <div className="sink-api-select-slider-parent">
        <div
          className="sink-api-select-slider-element"
          onClick={() => setApi("Remove sink")}
          style={{
            boxShadow:
              api === "Remove sink" ? "0px 6px 10px rgba(0, 0, 0, 0.3)" : "none",
            borderBottomLeftRadius: "0px",
            borderTopLeftRadius: api === "Remove sink" ? "10px" : "0px",
            backgroundColor: api === "Remove sink" ? "#fff" : "transparent",
            transition: "all 0.3s ease-in-out",
          }}
        >
          Remove sink
        </div>
      
        <div
          className="sink-api-select-slider-element"
          onClick={() => setApi("Add sink")}
          style={{
            boxShadow:
              api === "Add sink" ? "0px 6px 10px rgba(0, 0, 0, 0.3)" : "none",
            borderBottomRightRadius: "0px",
            borderTopRightRadius: api === "Add sink" ? "10px" : "0px",
            backgroundColor: api === "Add sink" ? "#fff" : "transparent",
            transition: "all 0.3s ease-in-out",
          }}
        >
          Add sink
        </div>
      </div>
      {api === "Remove sink" ? <RemoveSink /> : null}
      {api === "Add sink" ? <AddSink /> : null}
    </div>
  );
};

export default SinkApiCard;
