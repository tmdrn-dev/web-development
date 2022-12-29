import React from "react";

function strike() {
  document.getElementById("root").style.color = "red";
}

function unStrike() {
  document.getElementById("root").style.color = null;
}

function App() {
  return (
    <div>
      <p>Buy milk</p>
      <button onClick={strike}>Change to strike through</button>
      <button onClick={unStrike}>Change back</button>
    </div>
  );
}

export default App;
