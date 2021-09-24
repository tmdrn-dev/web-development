function updateTitle(text) {
  let h1 = document.querySelector("h1");
  h1.innerHTML = text;
}

function findButtonByColor(color) {
  let buttons = document.querySelectorAll(".btn");
  for (let i = 0; i < buttons.length; i++) {
    if (buttons[i].innerText === color)
      return buttons[i];
  }
}

function clickButton(target) {
  target.classList.add("pressed");
  setTimeout(function () {
    target.classList.remove("pressed");
  }, 100);
}

function playSound(fileName) {
  let audio = new Audio(`sounds/${fileName}.mp3`);
  audio.play();
}

function getRandomButtonColor() {
  let randomNumber = Math.floor(Math.random()*4);
  switch(randomNumber) {
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
  let button = findButtonByColor(color);

  setTimeout(function() {
    clickButton(button);
    playSound(color);
    simonQueue.push(color);
    console.log(simonQueue);
  }, 1000);

  gamePause = false;
}

function matchColor(userPickedColor) {
  console.log(userPickedColor, simonQueue[userStage])
  if (userPickedColor != simonQueue[userStage]) {
    stopGame();
    return;
  }

  if (userStage === simonQueue.length-1) {
    userStage = 0;
    levelUp();
  } else {
    userStage++;
  }
}

function startGame() {
  console.log("Start Game!");
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