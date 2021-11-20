const express = require("express");
const date = require(__dirname + "/date.js");
const app = express();

app.use("/", express.static(__dirname + "/public"));
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

// Global variables
const todoList = [];
const workList = [];

app.get("/", function (req, res) {
  let today = date.getDate();
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
