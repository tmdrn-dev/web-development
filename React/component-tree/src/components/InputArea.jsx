import React from "react";

function InputArea(prop) {
  return (
    <div className="form">
      <input onChange={prop.onChange} type="text" value={prop.value} />
      <button onClick={prop.onClick}>
        <span>Add</span>
      </button>
    </div>
  );
}

export default InputArea;
