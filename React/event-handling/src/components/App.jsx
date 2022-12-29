import React from "react";

function App() {
  const [heading, setHeading] = React.useState("Hello");
  const [mouseOver, setBtnBackground] = React.useState(null);

  function handleClick() {
    console.log("clicked!");
    setHeading("Submitted");
  }

  function handleMouseOver() {
    console.log("mouseOver!");
    setBtnBackground("mouse-over");
  }

  function handleMouseOut() {
    console.log("mouseOut!");
    setBtnBackground(null);
  }

  return (
    <div className="container">
      <h1>{heading}</h1>
      <input type="text" placeholder="What's your name?" />
      <button
        className={mouseOver}
        onMouseOver={handleMouseOver}
        onMouseOut={handleMouseOut}
        onClick={handleClick}
      >
        Submit
      </button>
    </div>
  );
}

export default App;
