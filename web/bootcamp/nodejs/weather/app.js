const express = require("express");
const https = require("https");

const app = express();
app.use(express.urlencoded({ extended: true }));

app.get("/", function (req, res) {
  res.sendFile(__dirname + "/index.html");
});

app.post("/", function (req, res) {
  const city = req.body.cityName;
  const appId = "8f0ba11f8e0f1047f385635a8156bbff";
  const units = "metric";
  const openweathermapUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${appId}&units=${units}`;

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
