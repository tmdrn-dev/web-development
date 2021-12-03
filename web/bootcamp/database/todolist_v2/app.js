const express = require("express");
const mongoose = require("mongoose");
const app = express();

app.use("/", express.static(__dirname + "/public"));
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

mongoose.connect("mongodb://localhost:27017/todoListDB");
const TodoItemSchem = { name: String };
const TodoItem = mongoose.model("TodoItem", TodoItemSchem);

// const item_1 = new TodoItem({
//   name: "Sleep on time",
// });
// const item_2 = new TodoItem({
//   name: "Work hard",
// });
// const item_3 = new TodoItem({
//   name: "Study harder",
// });

// const itemList = [item_1, item_2, item_3];
// TodoItem.insertMany(itemList, function (err) {
//   if (err) {
//     console.error(err);
//   }
// });

app.get("/", function (req, res) {
  TodoItem.find(function (err, items) {
    if (err) {
      console.error(err);
    } else {
      res.render("list", { listTitle: "Today", todoList: items });
    }
  });
});

app.post("/", function (req, res) {
  let itemName = req.body.newItem;
  const todoItem = new TodoItem({name: itemName});
  todoItem.save();
  res.redirect("/");
});

// Global variables
// const workList = [];
// app.get("/work", function (req, res) {
//   res.render("list", { listTitle: "work List", todoList: workList });
// });

// app.post("/work", function (req, res) {
//   let item = req.body.newItem;
//   workList.push(item);

//   res.redirect("/work");
// });

// app.get("/about", function (req, res) {
//   res.render("about");
// });

app.listen(3000, function () {
  console.log("Server is running");
});
