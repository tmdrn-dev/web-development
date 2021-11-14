const express = require("express");
const app = express();

app.set("view engine", "ejs");

app.get("/", function (req, res) {
  let weekday = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];

  let date = new Date();
  let today = date.getDay();

  res.render("list", { kindOfDay: weekday[today] });
});

app.listen(3000, function () {
  console.log("Server is running");
});
