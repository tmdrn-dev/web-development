import React from "react";
import Login from "./Login";

let isLoggedIn = false;
let currentTime = new Date(2022, 2, 28, 13).getHours();

function App() {
  return (
    <div className="container">
      {
        // Ternary operator
        isLoggedIn ? <h1>Hello</h1> : <Login />
        // And operator
        //currentTime > 12 && <h1>asdfasf</h1>
      }
    </div>
  );
}

export default App;
