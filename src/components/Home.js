import React, { useEffect, useState } from "react";
import "bootstrap/dist/css/bootstrap.css";
import axios from "axios";
import "./Home.css";
import AppCard from "./AppCard";
import sink from "../img/sink.jpeg";
import pipe from "../img/pipe.jpeg";
import source from "../img/source.jpeg";
import network from "../img/network.jpeg";
import "./misc/Card.css"

const Home = () => {
  return (
    <div className="app-container">
      <div className="app-body">
        <p id="app-header-heading-1">Regional Heating Network</p>
        <p id="app-header-heading-4">
          Sustainable Heat Distribution for the Future
        </p>
        <br />
        <div className="app-card-section">
          <AppCard
            url="/sink-analysis"
            img={sink}
            header="Sink analysis"
            body="Access sink API to control and simulate water discharge dynamically."
          />
          <AppCard
            url="/source-analysis"
            img={source}
            header="Source analysis"
            body="Access source API to control and simulate water discharge dynamically."
          />
          <AppCard
            url="/pipe-analysis"
            img={pipe}
            header="Pipe analysis"
            body="Access pipe API to control and simulate water discharge dynamically."
          />
          <AppCard
            url="/network-analysis"
            img={network}
            header="Network analysis"
            body="Access network API to control and simulate water discharge dynamically."
          />
        </div>
      </div>
    </div>
  );
};

export default Home;
