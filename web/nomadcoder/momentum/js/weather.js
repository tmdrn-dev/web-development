const API_KEY = '8f0ba11f8e0f1047f385635a8156bbff';

function onPositionOk(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${API_KEY}`;
    fetch(url).then(response => response.json()).then(data => {
        const city = document.querySelector("#weather span:first-child");
        const temperature = document.querySelector("#weather span:nth-child(2)");
        const weather = document.querySelector("#weather span:last-child");

        city.innerText = data.name;
        temperature.innerText = data.main.temp;
        weather.innerText = data.weather[0].main;
    });
}

function onPositionError(error) {
    console.log(error);
}

navigator.geolocation.getCurrentPosition(onPositionOk, onPositionError);
