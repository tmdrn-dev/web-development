//jshint esversion:6

const express = require("express");
const ejs = require("ejs");
const _ = require("lodash");
const app = express();

app.set("view engine", "ejs");

app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

const systemDatabase = [
  {
    title: "home",
    body: "Lacus vel facilisis volutpat est velit egestas dui id ornare. Semper auctor neque vitae tempus quam. Sit amet cursus sit amet dictum sit amet justo. Viverra tellus in hac habitasse. Imperdiet proin fermentum leo vel orci porta. Donec ultrices tincidunt arcu non sodales neque sodales ut. Mattis molestie a iaculis at erat pellentesque adipiscing. Magnis dis parturient montes nascetur ridiculus mus mauris vitae ultricies. Adipiscing elit ut aliquam purus sit amet luctus venenatis lectus. Ultrices vitae auctor eu augue ut lectus arcu bibendum at. Odio euismod lacinia at quis risus sed vulputate odio ut. Cursus mattis molestie a iaculis at erat pellentesque adipiscing.",
  },
  {
    title: "about",
    body: "Hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Dictumst vestibulum rhoncus est pellentesque elit ullamcorper. Non diam phasellus vestibulum lorem sed. Platea dictumst quisque sagittis purus sit. Egestas sed sed risus pretium quam vulputate dignissim suspendisse. Mauris in aliquam sem fringilla. Semper risus in hendrerit gravida rutrum quisque non tellus orci. Amet massa vitae tortor condimentum lacinia quis vel eros. Enim ut tellus elementum sagittis vitae. Mauris ultrices eros in cursus turpis massa tincidunt dui.",
  },
  {
    title: "contact",
    body: "Scelerisque eleifend donec pretium vulputate sapien. Rhoncus urna neque viverra justo nec ultrices. Arcu dui vivamus arcu felis bibendum. Consectetur adipiscing elit duis tristique. Risus viverra adipiscing at in tellus integer feugiat. Sapien nec sagittis aliquam malesuada bibendum arcu vitae. Consequat interdum varius sit amet mattis. Iaculis nunc sed augue lacus. Interdum posuere lorem ipsum dolor sit amet consectetur adipiscing elit. Pulvinar elementum integer enim neque. Ultrices gravida dictum fusce ut placerat orci nulla. Mauris in aliquam sem fringilla ut morbi tincidunt. Tortor posuere ac ut consequat semper viverra nam libero.",
  },
];

// Need to fix
function findContentByTitle(title, database) {
  return database.find((element) => element.title == title);
}

function contentObject(content) {
  this.title = _.capitalize(content.title);
  this.body = content.body;
}

app.get("/", function (req, res) {
  const title = "home";
  const content = findContentByTitle(title, systemDatabase);
  res.render(title, {
    contents: new contentObject(content),
  });
});

app.get("/:id", function (req, res) {
  const title = req.params.id;
  if (title == "compose") {
    res.render("compose");
  } else {
    const content = findContentByTitle(title, systemDatabase);
    if (content) {
      res.render("menu", {
        contents: new contentObject(content),
      });
    } else {
      res.status(404).render("404");
    }
  }
});

// object should be saved into database
const userDatabase = [];
app.get("/posts/:id", function (req, res) {
  const title = _.lowerCase(req.params.id);
  const content = findContentByTitle(title, userDatabase);
  console.log(userDatabase);
  console.log(content);
  if (content) {
    res.render("post", {
      contents: new contentObject(content),
    });
  } else {
    res.status(404).render("404");
  }
});

app.post("/compose", function (req, res) {
  userDatabase.push({
    title: req.body.postTitle,
    body: req.body.postBody,
  });
  res.redirect("/");
});

const PORT = 2000;
app.listen(PORT, function () {
  console.log(`Server started on port ${PORT}`);
});
