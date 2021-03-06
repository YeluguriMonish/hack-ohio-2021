import React, { Component } from "react";
import Table from "react-bootstrap/Table";

import CholecapUAC from "../../../data/targetUACCholecap.json";
import NasalclearUAC from "../../../data/targetUACNasalclear.json";
import NovaUAC from "../../../data/targetUACNova_itch.json";
import ZapUAC from "../../../data/targetUACZap_a_Pain.json";

export default class DrugData extends Component {
  render() {
    switch (this.props.drug) {
      case "cholecap":
        return (
          <>
            <Table striped bordered hover>
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>First Name</th>
                  <th>Last Name</th>
                  <th>TRx Total</th>
                  <th>State</th>
                </tr>
              </thead>
              <tbody>
                {Object.values(CholecapUAC).map((doc, index) => (
                  <tr>
                    <td>{index + 1}</td>
                    <td>{doc.first_name}</td>
                    <td>{doc.last_name}</td>
                    <td>{doc.TRx_sum}</td>
                    <td>{doc.State}</td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </>
        );
      case "zap":
        return (
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Rank</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>TRx Total</th>
                <th>State</th>
              </tr>
            </thead>
            <tbody>
              {Object.values(ZapUAC).map((doc, index) => (
                <tr>
                  <td>{index + 1}</td>
                  <td>{doc.first_name}</td>
                  <td>{doc.last_name}</td>
                  <td>{doc.TRx_sum}</td>
                  <td>{doc.State}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        );
      case "nasalclear":
        return (
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Rank</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>TRx Total</th>
                <th>State</th>
              </tr>
            </thead>
            <tbody>
              {Object.values(NasalclearUAC).map((doc, index) => (
                <tr>
                  <td>{index + 1}</td>
                  <td>{doc.first_name}</td>
                  <td>{doc.last_name}</td>
                  <td>{doc.TRx_sum}</td>
                  <td>{doc.State}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        );
      case "nova":
        return (
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Rank</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>TRx Total</th>
                <th>State</th>
              </tr>
            </thead>
            <tbody>
              {Object.values(NovaUAC).map((doc, index) => (
                <tr>
                  <td>{index + 1}</td>
                  <td>{doc.first_name}</td>
                  <td>{doc.last_name}</td>
                  <td>{doc.TRx_sum}</td>
                  <td>{doc.State}</td>
                </tr>
              ))}
            </tbody>
          </Table>
        );
      default:
        return <div>Select product</div>;
    }
  }
}
