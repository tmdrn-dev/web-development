import React from "react";

function CreateArea(props) {
  const [note, setNote] = React.useState({ title: "", content: "" });

  function onChangeCallback(event) {
    const { name, value } = event.target;
    setNote({ ...note, [name]: value });
  }

  function onSubmitCallback(event) {
    event.preventDefault();

    props.onAdd(note);
    setNote({ title: "", content: "" });
  }

  return (
    <div>
      <form onSubmit={onSubmitCallback}>
        <input
          onChange={onChangeCallback}
          name="title"
          placeholder="Title"
          value={note.title}
        />
        <textarea
          onChange={onChangeCallback}
          name="content"
          placeholder="Take a note..."
          rows="3"
          value={note.content}
        />
        <button>Add</button>
      </form>
    </div>
  );
}

export default CreateArea;
