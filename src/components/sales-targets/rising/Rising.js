import React, { Component } from "react";
import Table from "react-bootstrap/Table";

import CholecapRising from "../../../data/rising-cholecap.json";
import NasalclearRising from "../../../data/rising-nasalclear.json";
import NovaRising from "../../../data/rising-nova.json";
import ZapRising from "../../../data/rising-zap.json";

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
                {Object.values(CholecapRising).map((doc, index) => (
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
              {Object.values(ZapRising).map((doc, index) => (
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
              {Object.values(NasalclearRising).map((doc, index) => (
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
              {Object.values(NovaRising).map((doc, index) => (
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
