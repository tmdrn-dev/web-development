//jshint esversion:6

const express = require("express");
const mongoose = require("mongoose");
const _ = require("lodash");
const account = require(__dirname + "/account.js");

const app = express();
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));
app.use("/", express.static(__dirname + "/public"));
app.locals._ = _;

mongoose.connect(
  `mongodb+srv://${account.id}:${account.passwd}@cluster0.zzv9r.mongodb.net/blogDB?retryWrites=true&w=majority`
);

const contentSchema = new mongoose.Schema({
  title: String,
  body: String,
});

const SystemContent = mongoose.model("systemcontent", contentSchema);
const UserContent = mongoose.model("usercontent", contentSchema);

const homeContent = new SystemContent({
  title: "home",
  body: "Lacus vel facilisis volutpat est velit egestas dui id ornare. Semper auctor neque vitae tempus quam. Sit amet cursus sit amet dictum sit amet justo. Viverra tellus in hac habitasse. Imperdiet proin fermentum leo vel orci porta. Donec ultrices tincidunt arcu non sodales neque sodales ut. Mattis molestie a iaculis at erat pellentesque adipiscing. Magnis dis parturient montes nascetur ridiculus mus mauris vitae ultricies. Adipiscing elit ut aliquam purus sit amet luctus venenatis lectus. Ultrices vitae auctor eu augue ut lectus arcu bibendum at. Odio euismod lacinia at quis risus sed vulputate odio ut. Cursus mattis molestie a iaculis at erat pellentesque adipiscing.",
});
const aboutContent = new SystemContent({
  title: "about",
  body: "Lacus vel facilisis volutpat est velit egestas dui id ornare. Semper auctor neque vitae tempus quam. Sit amet cursus sit amet dictum sit amet justo. Viverra tellus in hac habitasse. Imperdiet proin fermentum leo vel orci porta. Donec ultrices tincidunt arcu non sodales neque sodales ut. Mattis molestie a iaculis at erat pellentesque adipiscing. Magnis dis parturient montes nascetur ridiculus mus mauris vitae ultricies. Adipiscing elit ut aliquam purus sit amet luctus venenatis lectus. Ultrices vitae auctor eu augue ut lectus arcu bibendum at. Odio euismod lacinia at quis risus sed vulputate odio ut. Cursus mattis molestie a iaculis at erat pellentesque adipiscing.",
});
const contactContent = new SystemContent({
  title: "contact",
  body: "Scelerisque eleifend donec pretium vulputate sapien. Rhoncus urna neque viverra justo nec ultrices. Arcu dui vivamus arcu felis bibendum. Consectetur adipiscing elit duis tristique. Risus viverra adipiscing at in tellus integer feugiat. Sapien nec sagittis aliquam malesuada bibendum arcu vitae. Consequat interdum varius sit amet mattis. Iaculis nunc sed augue lacus. Interdum posuere lorem ipsum dolor sit amet consectetur adipiscing elit. Pulvinar elementum integer enim neque. Ultrices gravida dictum fusce ut placerat orci nulla. Mauris in aliquam sem fringilla ut morbi tincidunt. Tortor posuere ac ut consequat semper viverra nam libero.",
});
const systemContents = [homeContent, aboutContent, contactContent];

SystemContent.find(function (err, docs) {
  if (docs) {
    if (docs.length === 0) {
      SystemContent.insertMany(systemContents, function (err) {
        if (err) {
          console.log("error: " + err);
        }
      });
    }
  }
});

app.get("/", function (req, res) {
  const systemQuery = SystemContent.where({ title: "home" });
  systemQuery.findOne(function (err, doc) {
    if (doc) {
      UserContent.find(function (err, docs) {
        if (docs.length !== 0) {
          res.render("home", {
            contents: doc,
            userContents: docs,
          });
        } else {
          res.status(404).render("404");
        }
      });
    } else {
      res.status(404).render("404");
    }
  });
});

app.get("/:id", function (req, res) {
  const title = req.params.id;
  if (title == "compose") {
    res.render("compose");
  } else {
    const query = SystemContent.where({ title: _.lowerCase(title) });
    query.findOne(function (err, doc) {
      if (doc) {
        res.render("menu", {
          contents: doc,
        });
      } else {
        res.status(404).render("404");
      }
    });
  }
});

app.get("/posts/:id", function (req, res) {
  const id = req.params.id;
  const query = UserContent.where({ _id: id });
  query.findOne(function (err, doc) {
    if (doc) {
      res.render("post", {
        contents: doc,
      });
    } else {
      res.status(404).render("404");
    }
  });
});

app.post("/compose", function (req, res) {
  const userContent = new UserContent({
    title: _.lowerCase(req.body.postTitle),
    body: req.body.postBody,
  });
  userContent.save(function (err) {
    if (!err) {
      res.redirect("/");
    }
  });
});

const PORT = 2000;
app.listen(PORT, function () {
  console.log(`Server started on port ${PORT}`);
});
