function onKeyDown(event) {
  if(event.code === "Space") {
    event.preventDefault();
  }

  if (gameStart === false) {
    gameStart = true;
    startGame();
  }
}

function onBtnClick(event) {
  if (gameStart === false || gamePause === true) {
    return;
  }

  let button = event.target;
  clickButton(button);
  playSound(button.innerText);
  matchColor(button.innerText);
}

document.addEventListener("keydown", onKeyDown);

let buttons = document.querySelectorAll(".btn");
for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", onBtnClick);
}
