import React from "react";
import Card from "./card";
import contacts from "../contacts";
import Avatar from "./avatar";

function createCard(contact) {
  return <Card key={contact.id} info={contact} />;
}

function App() {
  return (
    <div>
      <Avatar img="https://t1.daumcdn.net/cfile/tistory/99ECDF335E67C58135" />
      <h1 className="heading">My Contacts</h1>
      {/* {contacts.map((element) => (
        <Card info={element} />
      ))} */}
      {contacts.map(createCard)}
    </div>
  );
}

export default App;
