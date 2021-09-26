let gameStart = false;
let gamePause = false;
let gameLevel = 0;

let simonQueue = [];
let userStage = 0;

function updateTitle(text) {
  $("h1").html(text);
}

function getRandomButtonColor() {
  let randomNumber = Math.floor(Math.random() * 4);
  switch (randomNumber) {
    case 0:
      return "green";
    case 1:
      return "red";
    case 2:
      return "yellow";
    case 3:
      return "blue";
  }
}

function levelUp() {
  gamePause = true;
  gameLevel += 1;
  updateTitle("Level " + gameLevel);

  let color = getRandomButtonColor();
  let button = FindButtonByColor(color);

  setTimeout(function () {
    button.Click();
    simonQueue.push(color);
    console.log(simonQueue);
  }, 1000);

  gamePause = false;
}

function matchColor(userPickedColor) {
  console.log(userPickedColor, simonQueue[userStage]);
  if (userPickedColor != simonQueue[userStage]) {
    stopGame();
    return;
  }

  if (userStage === simonQueue.length - 1) {
    userStage = 0;
    levelUp();
  } else {
    userStage++;
  }
}

function startGame() {
  console.log("Start Game!");
  gameStart = true;
  levelUp();
}

function stopGame() {
  console.log("Game Over!");
  updateTitle("Game Over!<br>Press Any Key");
  gameStart = false;
  gameLevel = 0;
  simonQueue = [];
  userStage = 0;
}
