const images = ["0.jpeg", "1.jpg", "2.jpg", "3.jpg"];

const randomImageNumber = Math.random();
const randomImageIndex = Math.floor(randomImageNumber * images.length);

const backgroundImage = document.createElement("img");
backgroundImage.src = "img/background/" + images[randomImageIndex];
document.body.appendChild(backgroundImage);
