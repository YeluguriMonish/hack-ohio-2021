import React, { Component } from "react";
import Header from "./header/Header";

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
      </>
    );
  }
}
