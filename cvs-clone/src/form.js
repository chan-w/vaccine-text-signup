import React from 'react';
import './form.css';
import { Link } from "react-router-dom";

function Form() {
  return (
    <div className="form">
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap');
    </style>
      <div className="Page 1">
        <h1>Sudo-Vaccine Form</h1>
        {/*True or False Questions*/}
        <h2>1. In the past 14 days, have you tested positive for COVID-19?</h2>
        <input type="text"/>
        <h2>2. In the past 14 days, have you been in close contact with anyone who tested positive for COVID-19?</h2>
        <input type="text"/>
        <h2>3. Do you currently have fever, chills, cough, shortness of breath, difficulty breathing, fatigue, muscle or body aches, headache, new loss of taste or smell, sore throat, nausea, vomiting, or diarrhea?</h2>
        <input type="text"/>
      </div>
      <div className="Page 2">
        <h2>4. Tell us what you need. Do you need to start vaccination or schedule a second dose.</h2>
        <input type="text"/>
      </div>
      <div className="Page 3">
        <h2>5. Where do you want to be vaccinated?</h2>
        <input type="text"/>
      </div>
      <div className="Page 4">
        <h2>6. What is your age?</h2>
        <input type="text"/>
      </div>
      <div className="Page 5">
        <h2>7. Do you qualify for Teachers and staff or 16 years and over?</h2>
        <input type="text"/>
      </div>
      <div className="Page 6">
        <h2>8. When do you want to schedule a vaccine</h2>
        <input type="text"/>
      </div>
      <div className="Page 7">
        <h2>9. What is your First Name and Last Name</h2>
        <input type="text"/>
        <h2>10. Date of birth </h2>
        <input type="text"/>
        <h2>11. Gender</h2>
        <input type="text"/>
        <h2>12. What is your Address (include city, state, zip-code)</h2>
        <input type="text"/>
        <h2>13. Email Address</h2>
        <input type="text"/>
        <h2>14. Mobile Number</h2>
        <input type="text"/>
        <h2>15. What kind of coverage do you have?</h2>
        <input type="text"/>
      </div>
      <Link to= "/success" style={{ textDecoration: "none" }}><button>Submit</button></Link>
    </div>
  );
}

export default Form;
