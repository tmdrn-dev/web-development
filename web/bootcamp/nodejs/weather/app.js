const express = require("express");
const https = require("https");

const app = express();

const openweathermapUrl =
  "https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=8f0ba11f8e0f1047f385635a8156bbff&units=metric";

app.get("/", function (req, res) {
  https.get(openweathermapUrl, function (weatherRes) {
    console.log(res.statusCode);
    weatherRes.on("data", (data) => {
      const weatherData = JSON.parse(data);
      const temp = weatherData.main.temp;
      const description = weatherData.weather[0].description;
      const icon = weatherData.weather[0].icon;

      res.write(`<p>${description}</p>`);
      res.write("<h1>" + temp.toString() + "</h1>");
      res.write(`<img src='http://openweathermap.org/img/wn/${icon}@2x.png'>`);
      res.send();
    });
  });
});

app.listen(3000, function () {
  console.log("Server is running on port:3000");
});
