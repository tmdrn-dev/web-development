import React from "react";
import ReactDOM from "react-dom";

const img = "https://picsum.photos/200";

ReactDOM.render(
  <div>
    <h1 className="heading">My Favourite Foods</h1>
    <div>
      <img src={img + "?grayscale"} alt="random"></img>
    </div>
  </div>,
  document.getElementById("root")
);
