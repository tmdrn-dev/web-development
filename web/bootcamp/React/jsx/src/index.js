import React from "react";
import ReactDOM from "react-dom";

const author = "Seungku Choi";
const date = new Date();

ReactDOM.render(
  <div>
    <p>Created by {author}</p>
    <p>Copyright {date.getFullYear()}</p>
  </div>,
  document.getElementById("root")
);
