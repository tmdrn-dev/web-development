import React from "react";

function Entry(props) {
  return (
    <div className="term">
      <dt>
        <span className="emoji" role="img" aria-label="Tense Biceps">
          {props.info.emoji}
        </span>
        <span>{props.info.name}</span>
      </dt>
      <dd>{props.info.meaning}</dd>
    </div>
  );
}

export default Entry;
