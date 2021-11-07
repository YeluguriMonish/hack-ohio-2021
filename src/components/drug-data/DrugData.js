import React, { Component } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import Table from "react-bootstrap/Table";
import Map from "./map/Map";

import "./DrugData.css";

import TrxCholeccap from "../../data/trx-choleccap.json";
import TrxZap from "../../data/trx-zap.json";
import TrxNasalclear from "../../data/trx-nasalclear.json";
import TrxNova from "../../data/trx-nova.json";
import TopDocsChloecap from "../../data/top-docs-chloecap.json";
import TopDocsZap from "../../data/top-docs-zap.json";
import TopDocsNasalclear from "../../data/top-docs-nasalclear.json";
import TopDocsNova from "../../data/top-docs-nova.json";

export default class DrugData extends Component {
  render() {
    switch (this.props.drug) {
      case "cholecap":
        return (
          <>
            <Map drug={"cholecap"} />
            <ResponsiveContainer aspect={5.0 / 2.0} width="85%">
              <LineChart
                data={TrxCholeccap}
                margin={{
                  top: 20,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis
                  dataKey="name"
                  label={{ value: "Month", position: "insideBottom" }}
                />
                <YAxis
                  label={{ value: "TRx", angle: -90, position: "insideLeft" }}
                />
                <Tooltip />
                <Line
                  type="monotone"
                  dataKey="prescriptions"
                  stroke="#82ca9d"
                />
              </LineChart>
            </ResponsiveContainer>
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
                {Object.values(TopDocsChloecap).map((doc, index) => (
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
          <>
            <div className="test">
              <Map drug={"zap"} />
              <ResponsiveContainer aspect={5.0 / 2.0} width="85%">
                <LineChart
                  width={500}
                  height={300}
                  data={TrxZap}
                  margin={{
                    top: 20,
                    right: 30,
                    left: 20,
                    bottom: 5,
                  }}
                >
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis
                    dataKey="name"
                    label={{ value: "Month", position: "insideBottom" }}
                  />
                  <YAxis
                    label={{ value: "TRx", angle: -90, position: "insideLeft" }}
                  />
                  <Tooltip />
                  <Line
                    type="monotone"
                    dataKey="prescriptions"
                    stroke="#82ca9d"
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
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
                {Object.values(TopDocsZap).map((doc, index) => (
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
      case "nasalclear":
        return (
          <>
            <ResponsiveContainer aspect={5.0 / 2.0} width="85%">
              <LineChart
                width={500}
                height={300}
                data={TrxNasalclear}
                margin={{
                  top: 20,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis
                  dataKey="name"
                  label={{ value: "Month", position: "insideBottom" }}
                />
                <YAxis
                  label={{ value: "TRx", angle: -90, position: "insideLeft" }}
                />
                <Tooltip />
                <Line
                  type="monotone"
                  dataKey="prescriptions"
                  stroke="#82ca9d"
                />
              </LineChart>
            </ResponsiveContainer>
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
                {Object.values(TopDocsNasalclear).map((doc, index) => (
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
            <Map drug={"nasalclear"} />
          </>
        );
      case "nova":
        return (
          <>
            <ResponsiveContainer aspect={5.0 / 2.0} width="85%">
              <LineChart
                width={500}
                height={300}
                data={TrxNova}
                margin={{
                  top: 20,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis
                  dataKey="name"
                  label={{ value: "Month", position: "insideBottom" }}
                />
                <YAxis
                  label={{ value: "TRx", angle: -90, position: "insideLeft" }}
                />
                <Tooltip />
                <Line
                  type="monotone"
                  dataKey="prescriptions"
                  stroke="#82ca9d"
                />
              </LineChart>
            </ResponsiveContainer>
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
                {Object.values(TopDocsNova).map((doc, index) => (
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
            <Map drug={"nova"} />
          </>
        );
      default:
        return <div>select drug</div>;
    }
  }
}
