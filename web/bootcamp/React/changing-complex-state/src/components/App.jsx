import React from "react";

function App() {
  const [userName, setUserName] = React.useState({ fName: "", lName: "" });

  function handleOnChange(event) {
    const { name, value } = event.target;

    console.log(value);
    console.log(name);

    setUserName((preValue) => {
      if (name === "fName") {
        return {
          fName: value,
          lName: preValue.lName
        };
      } else {
        return {
          fName: preValue.fName,
          lName: value
        };
      }
    });
  }

  return (
    <div className="container">
      <h1>
        Hello {userName.fName} {userName.lName}
      </h1>
      <form>
        <input
          onChange={handleOnChange}
          name="fName"
          placeholder="First Name"
          value={userName.fName}
        />
        <input
          onChange={handleOnChange}
          name="lName"
          placeholder="Last Name"
          value={userName.lName}
        />
        <button>Submit</button>
      </form>
    </div>
  );
}

export default App;
