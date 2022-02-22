import React from "react";
import Avatar from "./avatar";
import Detail from "./detail";

function Card(props) {
  return (
    <div className="card">
      <div className="top">
        <h2 className="name">{props.info.name}</h2>
        <Avatar img={props.info.imgURL} />
      </div>
      <div className="bottom">
        <Detail info={props.info.phone} />
        <Detail info={props.info.email} />
      </div>
    </div>
  );
}

export default Card;
