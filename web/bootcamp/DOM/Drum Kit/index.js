const SOUND_TOM_1 = "sounds/tom-1.mp3";
const SOUND_TOM_2 = "sounds/tom-2.mp3";
const SOUND_TOM_3 = "sounds/tom-3.mp3";
const SOUND_TOM_4 = "sounds/tom-4.mp3";
const SOUND_CRASH = "sounds/crash.mp3";
const SOUND_KICK_BASS = "sounds/kick-bass.mp3";
const SOUND_SNARE = "sounds/snare.mp3";

function playAudio(path) {
  let audioSource = new Audio(path);
  audioSource.play();
}

function onKeyDown(event) {
  const keyName = event.key;
  console.log(keyName);

  switch (keyName) {
    case "w":
    case "W":
      playAudio(SOUND_TOM_1);
      break;

    case "a":
    case "A":
      playAudio(SOUND_TOM_2);
      break;

    case "s":
    case "S":
      playAudio(SOUND_TOM_3);
      break;

    case "d":
    case "D":
      playAudio(SOUND_TOM_4);
      break;

    case "j":
    case "J":
      playAudio(SOUND_CRASH);
      break;

    case "k":
    case "K":
      playAudio(SOUND_KICK_BASS);
      break;

    case "l":
    case "L":
      playAudio(SOUND_SNARE);
      break;
  }
}

document.addEventListener("keydown", onKeyDown);
