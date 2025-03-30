import React, { useEffect, useState } from "react";
import axios from "axios";
import "./NextHour.css";
import heater from "../../../img/heater.png";
import { LoadingBar } from "../../misc/LoadingBar";
import FadingTexts from "../../misc/FadingTexts";

const NextHour = ({ setIsTimeDisabled }) => {
  const [temp, setTemp] = useState(() => {
    // Retrieve stored temp if available
    const storedTemp = localStorage.getItem("temp");
    return storedTemp ? parseFloat(storedTemp) : "--.--";
  });

  const [lastRunAt, setLastRunAt] = useState(() => {
    // Retrieve stored lastRunAt if available
    return localStorage.getItem("lastRunAt") || null;
  });

  const [loading, setLoading] = useState(false);

  const fetchTemp = async () => {
    setLoading(true);
    setIsTimeDisabled(true);
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/next_hour/");
      const tempData = JSON.parse(response.data);
      console.log(tempData);

      // Store new values in state
      setTemp(tempData["temp"]);
      setLastRunAt(new Date().toISOString());
      setIsTimeDisabled(false);

      // Save to localStorage
      localStorage.setItem("temp", tempData["temp"]);
      localStorage.setItem("lastRunAt", new Date().toISOString());
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  const messages = ["Fetching Temperature...", "Almost Done..."];

  return (
    <div
      className="network-api-form-next-hour"
      style={{ position: "relative", paddingBottom: "10px" }}
    >
      <div className="network-api-form-header-next-hour">
        Temperature of Source
      </div>
      <div className="network-api-form-subheader-next-hour">
        Last Fetched: {lastRunAt ? new Date(lastRunAt).toLocaleString() : "--"}
      </div>
      <div className="network-api-form-input-next-hour">
        <img id="heater-img" src={heater} alt="Heater" />
        {temp !== "--.--" ? temp.toFixed(2) + "°C" : "--.--°C"}
      </div>
      <div className="network-api-form-fade-container">
        {loading ? (
          <FadingTexts messages={messages} />
        ) : (
          <button className="run-button fade-in" onClick={fetchTemp}>
            Run
          </button>
        )}
      </div>
      {loading && <LoadingBar />}
    </div>
  );
};

export default NextHour;
