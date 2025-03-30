import React, { useState } from "react";
import "./NetworkApiCard.css";
import Time from "./networkAPIcomponents/Time";
import NextHour from "./networkAPIcomponents/NextHour";

const NetworkApiCard = () => {
  const [api, setApi] = useState("Next hour");
  const [isNextHourDisabled, setIsNextHourDisabled] = useState(false);
  const [isTimeDisabled, setIsTimeDisabled] = useState(false);

  return (
    <div className="network-api-card">
      <div className="network-api-select-slider-parent">
        {/* Next Hour Button - Disable when fetching Time API */}
        <div
          className="network-api-select-slider-element"
          onClick={!isNextHourDisabled ? () => setApi("Next hour") : undefined}
          style={{
            boxShadow:
              api === "Next hour" ? "0px 6px 10px rgba(0, 0, 0, 0.3)" : "none",
            borderBottomLeftRadius: "0px",
            borderTopLeftRadius: api === "Next hour" ? "10px" : "0px",
            backgroundColor: api === "Next hour" ? "#fff" : "transparent",
            transition: "all 0.3s ease-in-out",
            pointerEvents: isNextHourDisabled ? "none" : "auto",
            opacity: isNextHourDisabled ? 0.5 : 1,
            cursor: isNextHourDisabled ? "not-allowed" : "pointer",
          }}
        >
          Next hour
        </div>

        {/* Time Button - Disable when fetching Next Hour API */}
        <div
          className="network-api-select-slider-element"
          onClick={!isTimeDisabled ? () => setApi("Time") : undefined}
          style={{
            boxShadow:
              api === "Time" ? "0px 6px 10px rgba(0, 0, 0, 0.3)" : "none",
            borderBottomRightRadius: "0px",
            borderTopRightRadius: api === "Time" ? "10px" : "0px",
            backgroundColor: api === "Time" ? "#fff" : "transparent",
            transition: "all 0.3s ease-in-out",
            pointerEvents: isTimeDisabled ? "none" : "auto",
            opacity: isTimeDisabled ? 0.5 : 1,
            cursor: isTimeDisabled ? "not-allowed" : "pointer",
          }}
        >
          Time
        </div>
      </div>

      {api === "Next hour" ? <NextHour setIsTimeDisabled={setIsTimeDisabled} /> : null}
      {api === "Time" ? <Time setIsNextHourDisabled={setIsNextHourDisabled} /> : null}
    </div>
  );
};

export default NetworkApiCard;
