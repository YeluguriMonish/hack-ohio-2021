import React, { Component } from "react";
import Tabs from "react-bootstrap/Tabs";
import Tab from "react-bootstrap/Tab";

import "./SalesTargets.css";

export default class SalesTargets extends Component {
  render() {
    return (
      <Tabs
        fill
        justify
        defaultActiveKey="profile"
        id="uncontrolled-tab-example"
        className="mb-3"
      >
        <Tab eventKey="home" title="Home">
          cock
        </Tab>
        <Tab eventKey="profile" title="Profile">
          bals
        </Tab>
        <Tab eventKey="contact" title="Contact">
          cock and balls
        </Tab>
      </Tabs>
    );
  }
}
