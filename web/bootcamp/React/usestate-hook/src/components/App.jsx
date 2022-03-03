import React from "react";

function App() {
  const time = new Date().toLocaleTimeString();
  const [current, setTime] = React.useState(time);

  setInterval(updateTime, 1000);

  function updateTime() {
    const time = new Date().toLocaleTimeString();
    setTime(time);
  }

  return (
    <div className="container">
      <h1>{current}</h1>
      <button onClick={updateTime}>Get Time</button>
    </div>
  );
}

export default App;
