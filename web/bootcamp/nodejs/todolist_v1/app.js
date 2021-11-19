const express = require("express");
const app = express();

app.use("/", express.static(__dirname + "/public"));
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

// Global variables
let todoList = [];
let workList = [];

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
  res.render("list", { listTitle: today, todoList: todoList });
});

app.post("/", function (req, res) {
  let item = req.body.newItem;
  if (req.body.list === "work") {
    workList.push(item);
    res.redirect("/work");
  } else {
    todoList.push(item);
    res.redirect("/");
  }
});

app.get("/work", function (req, res) {
  res.render("list", { listTitle: "work List", todoList: workList });
});

app.post("/work", function (req, res) {
  let item = req.body.newItem;
  workList.push(item);

  res.redirect("/work");
});

app.get("/about", function (req, res) {
  res.render("about");
});

app.listen(3000, function () {
  console.log("Server is running");
});
