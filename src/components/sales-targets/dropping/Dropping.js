import React, { Component } from "react";
import Table from "react-bootstrap/Table";

import CholecapDropping from "../../../data/targetDropCholecap.json";
import NasalclearDropping from "../../../data/targetDropNasalclear.json";
import NovaDropping from "../../../data/targetDropNova_itch.json";
import ZapDropping from "../../../data/targetDropZap_a_Pain.json";

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
                {Object.values(CholecapDropping).map((doc, index) => (
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
              {Object.values(ZapDropping).map((doc, index) => (
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
              {Object.values(NasalclearDropping).map((doc, index) => (
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
              {Object.values(NovaDropping).map((doc, index) => (
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
