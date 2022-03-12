import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import Note from "./Note";
import CreateArea from "./CreateArea";

function App() {
  const [notes, setNote] = React.useState([]);

  function onAddCallback(note) {
    console.log(note);
    setNote([...notes, note]);
  }

  function onDeleteCallback(id) {
    console.log(id);
    setNote(
      notes.filter((note, index) => {
        return index !== id;
      })
    );
  }

  return (
    <div>
      <Header />
      <CreateArea onAdd={onAddCallback} />
      {notes.map((note, index) => (
        <Note
          key={index}
          id={index}
          title={note.title}
          content={note.content}
          onDelete={onDeleteCallback}
        />
      ))}
      <Footer />
    </div>
  );
}

export default App;
