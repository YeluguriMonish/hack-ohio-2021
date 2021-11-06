import React, { Component } from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import { Dropdown } from "semantic-ui-react";

import "./Header.css";

const products = [
  { key: "cholecap", value: "cholecap", text: "Cholecap" },
  { key: "zap", value: "zap", text: "Zap-a-Pain" },
  { key: "nasalclear", value: "nasalclear", text: "Nasalclear" },
  { key: "nova", value: "nova", text: "Nova-itch" },
];

export default class Header extends Component {
  render() {
    return (
      <Navbar bg="light" expand="lg">
        <Navbar.Brand href="#home">Veena Data Visualizer</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="drug-data">Drug Data</Nav.Link>
            <Nav.Link href="sales-targets">Sales Targets</Nav.Link>
          </Nav>
          <Dropdown
            placeholder="Select Drug"
            fluid
            search
            selection
            options={products}
            onChange={this.props.handleChange}
          />
        </Navbar.Collapse>
      </Navbar>
    );
  }
}
