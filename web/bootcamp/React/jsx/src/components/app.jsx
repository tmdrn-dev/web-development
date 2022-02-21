import React from "react";
import Card from "./card";
import contacts from "../contracts";

function App() {
  return (
    <div>
      <h1 className="heading">My Contacts</h1>
      {contacts.map((element) => (
        <Card info={element} />
      ))}
    </div>
  );
}

export default App;
