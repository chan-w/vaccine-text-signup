import React from 'react';
import './Success.css';
import { Link } from "react-router-dom";

function Success() {
  return (
    <div className="success">
      <div className="success_box">
        <h3><b>Visit Type:</b>PAT MODERNA COV19 VACCINE 2ND DOSE</h3>
        <h3><b>Date and Time</b>5/8/2021 at 9:00AM PDT</h3>
        <h3><b>Location Address</b>9730 Hopkins Dr, La Jolla, 92093</h3>
        <h3>CSN: 66089117984</h3>
        <h3>Please bring email! Patients under 18 years old must be accompanied by guardian. After the vaccine you
        will be asked to remain on location for a 15-minute observation period. Please bring confirmation email
        and photo ID</h3>
      </div>
    </div>
  );
}

export default Success;
