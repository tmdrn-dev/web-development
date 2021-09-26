function onGlobalKeyDown(event) {
  if (event.code === "Space") {
    event.preventDefault();
  }

  if (gameStart === false) {
    startGame();
  }
}

function onButtonClick(event) {
  if (gameStart === false || gamePause === true) {
    return;
  }

  const color = event.target.innerText;
  const button = FindButtonByColor(color);
  button.Click();
  matchColor(button.color);
}

$(".btn").on("click", onButtonClick);
$(document).on("keydown", onGlobalKeyDown);
