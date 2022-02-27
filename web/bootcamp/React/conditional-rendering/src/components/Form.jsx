import React from "react";

function Register(props) {
  return (
    <form className="form">
      <input type="text" placeholder="Username" />
      <input type="password" placeholder="Password" />
      {!props.userRegister && (
        <input type="password" placeholder="Confirm Password" />
      )}
      <button type="submit">{props.userRegister ? "Login" : "Register"}</button>
    </form>
  );
}

export default Register;
