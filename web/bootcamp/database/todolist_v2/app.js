const express = require("express");
const mongoose = require("mongoose");
const _ = require("lodash");
const app = express();

app.use("/", express.static(__dirname + "/public"));
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

mongoose.connect("mongodb://localhost:27017/todoListDB");
const TodoItemSchem = { name: String };
const TodoItem = mongoose.model("TodoItem", TodoItemSchem);

const UserItemSchem = { name: String, items: [TodoItemSchem] };
const UserItem = mongoose.model("UserItem", UserItemSchem);

const todoItem_1 = new TodoItem({
  name: "Sleep on time",
});
const todoItem_2 = new TodoItem({
  name: "Work hard",
});
const todoItem_3 = new TodoItem({
  name: "Study harder",
});
const todoItemList = [todoItem_1, todoItem_2, todoItem_3];

app.get("/", function (req, res) {
  TodoItem.find(function (err, items) {
    if (err) {
      console.error(err);
    } else {
      if (items.length === 0) {
        TodoItem.insertMany(todoItemList, function (err) {
          if (err) {
            console.error(err);
          }
        });
      }

      res.render("list", { listTitle: "Today", todoList: items });
    }
  });
});

app.post("/", function (req, res) {
  let itemName = req.body.newItem;
  const todoItem = new TodoItem({ name: itemName });
  todoItem.save();
  res.redirect("/");
});

app.post("/delete", function (req, res) {
  let itemId = req.body.checked;
  TodoItem.findByIdAndRemove(itemId, function (err) {
    //TodoItem.deleteOne({id:itemId}, function(err) {
    if (err) console.error(err);
  });

  res.redirect("/");
});

app.get("/:userList", function (req, res) {
  const userListTitle = req.params.userList;
  UserItem.findOne({ name: userListTitle }, function (err, userList) {
    if (err) {
      console.error(err);
    } else {
      if (userList) {
        res.render("list", {
          listTitle: userList.name,
          todoList: userList.items,
        });
      } else {
        const userItem = new UserItem({
          name: userListTitle,
          items: todoItemList,
        });
        userItem.save();
        res.redirect("/" + userListTitle);
      }
    }
  });
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
