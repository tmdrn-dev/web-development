//Create a React app from scratch.
//Show a single h1 that says "Good morning" if between midnight and 12PM.
//or "Good Afternoon" if between 12PM and 6PM.
//or "Good evening" if between 6PM and midnight.
//Apply the "heading" style in the styles.css
//Dynamically change the color of the h1 using inline css styles.
//Morning = red, Afternoon = green, Night = blue.
import React from "react";
import ReactDOM from "react-dom";

class Greeting {
  constructor() {
    const date = new Date();
    const hours = date.getHours();

    if (hours >= 0 && hours < 12) {
      this.style = { color: "red" };
      this.text = "Good morning";
    } else if (hours >= 12 && hours < 19) {
      this.style = { color: "green" };
      this.text = "Good afternoon";
    } else {
      this.style = { color: "blue" };
      this.text = "Good evening";
    }
  }
}

const greeting = new Greeting();
// const greeting = getGrettingObj();
console.log(greeting);

ReactDOM.render(
  <div>
    <h1 className="heading" style={greeting.style}>
      {greeting.text}
    </h1>
  </div>,
  document.getElementById("root")
);
