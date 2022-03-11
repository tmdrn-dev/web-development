import React from "react";

function ToDoItem(prop) {
  return (
    <div
      onClick={() => {
        console.log(prop.id);

        prop.callback(prop.id);
      }}
    >
      <li>{prop.text}</li>
    </div>
  );
}

export default ToDoItem;
