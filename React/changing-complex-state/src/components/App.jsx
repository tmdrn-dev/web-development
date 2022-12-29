import React from "react";

function App() {
  const [contact, setContact] = React.useState({
    fName: "",
    lName: "",
    email: "",
  });

  function handleOnChange(event) {
    const { name, value } = event.target;

    setContact((prevContact) => {
      if (name === "fName") {
        return {
          fName: value,
          lName: prevContact.lName,
          email: prevContact.email,
        };
      } else if (name === "lName") {
        return {
          fName: prevContact.fName,
          lName: value,
          email: prevContact.email,
        };
      } else {
        // email
        return {
          fName: prevContact.fName,
          lName: prevContact.lName,
          email: value,
        };
      }
    });
  }

  return (
    <div className="container">
      <h1>
        Hello {contact.fName} {contact.lName}
      </h1>
      <p>{contact.email}</p>
      <form>
        <input
          onChange={handleOnChange}
          name="fName"
          placeholder="First Name"
          value={contact.fName}
        />
        <input
          onChange={handleOnChange}
          name="lName"
          placeholder="Last Name"
          value={contact.lName}
        />
        <input onChange={handleOnChange} name="email" placeholder="Email" value={contact.email} />
        <button>Submit</button>
      </form>
    </div>
  );
}

export default App;
