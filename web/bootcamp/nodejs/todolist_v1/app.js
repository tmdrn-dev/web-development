const express = require("express");
const app = express();

app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

// Global variables
let itemList = [];

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
  let options = {
    weekday: "short",
    year: "numeric",
    month: "short",
    day: "2-digit",
  };

  let today = date.toLocaleDateString("en-US", options);
  res.render("list", { kindOfDay: today, todoList: itemList });
});

app.post("/", function (req, res) {
  let newItem = req.body.newItem;
  console.log(newItem);
  itemList.push(newItem);

  res.redirect("/");
});

app.listen(3000, function () {
  console.log("Server is running");
});
