import React, { Component } from "react";
import USAMap from "react-usa-map";
import * as d3 from "d3";

import CholecapMapData from "../../../data/map-cholecap.json";
import NasalclearMapData from "../../../data/map-nasalclear.json";
import NovaMapData from "../../../data/map-nova.json";
import ZapMapData from "../../../data/map-zap.json";
import "./Map.css";

export default class Map extends Component {
  state = {
    dictionary_cholecap: {},
    dictionary_nasalclear: {},
    dictionary_nova: {},
    dictionary_zap: {},
  };
  componentDidMount() {
    let dict = {};
    var myColor = d3.scaleLinear().domain([0, 100]).range(["white", "orange"]);
    CholecapMapData.map((sta) => {
      dict[sta.State] = { fill: myColor(sta.AdjustedPercent * 100) };
    });
    this.setState({ dictionary_cholecap: dict });
    dict = {};
    NasalclearMapData.map((sta) => {
      dict[sta.State] = { fill: myColor(sta.AdjustedPercent * 100) };
    });
    this.setState({ dictionary_nasalclear: dict });
    dict = {};
    NovaMapData.map((sta) => {
      dict[sta.State] = { fill: myColor(sta.AdjustedPercent * 100) };
    });
    this.setState({ dictionary_nova: dict });
    dict = {};
    ZapMapData.map((sta) => {
      dict[sta.State] = { fill: myColor(sta.AdjustedPercent * 100) };
    });
    this.setState({ dictionary_zap: dict });
    dict = {};
  }
  /* mandatory */
  mapHandler = (event) => {
    alert(event.target.dataset.name);
  };

  render() {
    switch (this.props.drug) {
      case "cholecap":
        return (
          <div className="map">
            <USAMap
              customize={this.state.dictionary_cholecap}
              onClick={this.mapHandler}
            />
          </div>
        );
      case "nasalclear":
        return (
          <div className="map">
            <USAMap
              customize={this.state.dictionary_nasalclear}
              onClick={this.mapHandler}
            />
          </div>
        );
      case "nova":
        return (
          <div className="map">
            <USAMap
              customize={this.state.dictionary_nova}
              onClick={this.mapHandler}
            />
          </div>
        );
      case "zap":
        return (
          <div className="map">
            <USAMap
              customize={this.state.dictionary_zap}
              onClick={this.mapHandler}
            />
          </div>
        );
    }
  }
}
