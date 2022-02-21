import React from "react";
import ReactDOM from "react-dom";

function Card(props) {
  console.log(props);
  return (
    <div>
      <h2>{props.info.name}</h2>
      <img src={props.info.src} alt="avatar_img" />
      <p>{props.info.phone}</p>
      <p>{props.info.email}</p>
    </div>
  );
}

const beyonce = {
  name: "Beyonce",
  src: "https://blackhistorywall.files.wordpress.com/2010/02/picture-device-independent-bitmap-119.jpg",
  phone: "+123 456 789",
  email: "b@beyonce.com",
};

const jackBauer = {
  name: "Jack Bauer",
  src: "https://pbs.twimg.com/profile_images/625247595825246208/X3XLea04_400x400.jpg",
  phone: "+987 654 321",
  email: "jack@nowhere.com",
};

const chuckNorris = {
  name: "Chuck Norris",
  src: "https://i.pinimg.com/originals/e3/94/47/e39447de921955826b1e498ccf9a39af.png",
  phone: "+918 372 574",
  email: "gmail@chucknorris.com",
};

ReactDOM.render(
  <div>
    <h1>My Contacts</h1>
    <Card info={beyonce} />
    <Card info={jackBauer} />
    <Card info={chuckNorris} />
  </div>,
  document.getElementById("root")
);
