import React from "react";
import Header from "./header";
import Footer from "./footer";
import Note from "./note";
import notes from "../notes";

function App() {
  return (
    <div>
      <Header></Header>
      {notes.map((note) => (
        <Note key={note.key} obj={note} />
      ))}
      <Footer />
    </div>
  );
}

export default App;
