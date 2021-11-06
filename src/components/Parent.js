import React, { Component } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./header/Header";
import DrugData from "./drug-data/DrugData";
import SalesTargets from "./sales-targets/SalesTargets";

import "./Parent.css";

export default class Parent extends Component {
  state = {
    drug: null,
  };

  onChangeHandler = (e, data) => {
    this.setState({ drug: data.value }, () => {
      console.log(this.state.drug);
    });
  };

  render() {
    return (
      <>
        <Header handleChange={this.onChangeHandler} drug={this.state.drug} />
        <Router>
          <Routes>
            <Route path="/" element={<DrugData />} />
            <Route path="/drug-data" element={<DrugData />} />
            <Route path="/sales-targets" element={<SalesTargets />} />
          </Routes>
        </Router>
      </>
    );
  }
}
