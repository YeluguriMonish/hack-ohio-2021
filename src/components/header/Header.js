import React, { Component } from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import { Dropdown } from "semantic-ui-react";

import "./Header.css";
import veevaLogo from "./logo/veeva-logo.png";

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
        <Navbar.Brand href="#home">
          <img src={veevaLogo} height={36} width={150} />
          <br/>
          Product Visualizer
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="drug-data">Product Data</Nav.Link>
            <Nav.Link href="sales-targets">Sales Targets</Nav.Link>
          </Nav>
          <Dropdown
            placeholder="Select Product"
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
