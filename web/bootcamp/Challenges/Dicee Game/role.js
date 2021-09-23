let h1 = document.querySelector("h1");
let diceImg = document.querySelectorAll("img");

function roleDice() {
  return Math.floor(Math.random() * 6) + 1;
}

function getWinner(p1, p2) {
  if (p1 > p2) {
    return "Winner is player1";
  } else if (p2 > p1) {
    return "Winner is player2";
  }

  return "Draw";
}

function setDiceImg(idx, value) {
  diceImg[idx].setAttribute("src", "images/dice" + value + ".png");
}

function onBtnClick() {
  let player1 = roleDice();
  setDiceImg(0, player1);
  let player2 = roleDice();
  setDiceImg(1, player2);
  h1.innerText = getWinner(player1, player2);
}

const button = document.querySelector("button");
button.addEventListener("click", onBtnClick);
