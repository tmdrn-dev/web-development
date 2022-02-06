import React from "react";
import ReactDOM from "react-dom";

const myStyle = {
  color: "red",
  fontSize: "20px",
  border: "1px solid black",
};

myStyle.color = "blue";

ReactDOM.render(<h1 style={myStyle}>Hello World!</h1>, document.getElementById("root"));
