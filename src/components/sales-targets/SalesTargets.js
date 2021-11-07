import React, { Component } from "react";
import Tabs from "react-bootstrap/Tabs";
import Tab from "react-bootstrap/Tab";
import UAC from "./uac/Uac";
import Rising from "./rising/Rising";
import Dropping from "./dropping/Dropping";

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
        <Tab eventKey="home" title="Up and Coming">
          <UAC drug={this.props.drug} />
        </Tab>
        <Tab eventKey="profile" title="Rising">
          <Rising drug={this.props.drug} />
        </Tab>
        <Tab eventKey="contact" title="Dropping">
          <Dropping drug={this.props.drug} />
        </Tab>
      </Tabs>
    );
  }
}
