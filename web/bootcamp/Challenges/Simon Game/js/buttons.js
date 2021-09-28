function Button(color) {
  this.color = color;
  this.object = $("." + color[0]);

  PlaySound = function (color) {
    const soundFile = color + ".mp3";
    const audio = new Audio("sounds/" + soundFile);
    audio.play();
  };

  this.Click = function () {
    PlaySound(this.color);
    this.object.addClass("pressed");
    setTimeout(
      function (target) {
        target.object.removeClass("pressed");
      },
      100,
      this
    );
  };
}

const colors = ["green", "red", "yellow", "blue"];
const buttons = [];
for (let i = 0; i < colors.length; i++) {
  buttons[i] = new Button(colors[i]);
}

function FindButtonByColor(color) {
  for (let i = 0; i < buttons.length; i++) {
    if (buttons[i].color === color) {
      return buttons[i];
    }
  }
}
