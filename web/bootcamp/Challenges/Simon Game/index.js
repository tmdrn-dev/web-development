let playing = false;

function playSound(fileName) {
  let audio = new Audio(`sounds/${fileName}.mp3`);
  audio.play();
}

function onBtnClick(event) {
  let parent = event.target;
  parent.classList.add("pressed");
  setTimeout(function () {
    parent.classList.remove("pressed");
  }, 50);

  let btnColor = parent.innerText;
  playSound(btnColor);
}

function playGame() {
  console.log("play Game!");
  let buttons = document.querySelectorAll(".btn");
  for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", onBtnClick);
  }
  let h1 = document.querySelector("h1");
  h1.innerText = "Start!";
}

function onKeyDown(event) {
  playing = !playing;
  if (playing == true) {
    playGame();
  }
}

document.addEventListener("keydown", onKeyDown);
