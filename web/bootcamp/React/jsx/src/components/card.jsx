import React from "react";

function Card(props) {
  console.log(props);
  return (
    <div className="card">
      <div className="top">
        <h2 className="name">{props.info.name}</h2>
        <img className="circle-img" src={props.info.imgURL} alt="avatar_img" />
      </div>
      <div className="bottom">
        <p className="info">{props.info.phone}</p>
        <p className="info">{props.info.email}</p>
      </div>
    </div>
  );
}

export default Card;
