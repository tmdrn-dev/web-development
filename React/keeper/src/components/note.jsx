import React from "react";

function Note(props) {
  return (
    <div className="note">
      <h1>{props.obj.title}</h1>
      <p>{props.obj.content}</p>
    </div>
  );
}

export default Note;
