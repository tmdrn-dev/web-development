import React from "react";

function App() {
  const [name, setName] = React.useState("");
  const [heading, setHeading] = React.useState("");

  function handleChange(event) {
    console.log(event.target.value);
    // console.log(event.target.placeholder);
    // console.log(event.target.type);
    setName(event.target.value);
  }

  function handleOnSubmit(event) {
    setHeading(name);
    event.preventDefault();
  }

  return (
    <div className="container">
      <h1>Hello {heading}</h1>
      <form onSubmit={handleOnSubmit}>
        <input
          onChange={handleChange}
          type="text"
          placeholder="What's your name?"
          value={name}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
