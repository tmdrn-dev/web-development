import React from "react";

function App() {
  const [itemList, setItemList] = React.useState(["An item"]);
  const [newItem, setNewItem] = React.useState("");

  function handleOnChange(event) {
    const { value } = event.target;
    setNewItem(value);
  }

  function handleOnClick() {
    //setItemList([...itemList, newItem]);
    setItemList((itemList) => {
      return [...itemList, newItem];
    });
    setNewItem("");
  }

  return (
    <div className="container">
      <div className="heading">
        <h1>To-Do List</h1>
      </div>
      <div className="form">
        <input onChange={handleOnChange} type="text" value={newItem} />
        <button onClick={handleOnClick}>
          <span>Add</span>
        </button>
      </div>
      <div>
        <ul>
          {itemList.map((item) => (
            <li>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
