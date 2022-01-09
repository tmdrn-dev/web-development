const express = require("express");
const app = express();

app.use(express.static(__dirname + "/public"));
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

app.route("/").get(function (req, res) {
  res.render("home");
});

app.route("/login").get(function (req, res) {
  res.render("login");
});

app.route("/register").get(function (req, res) {
  res.render("register");
});

const port = 3000;
app.listen(port, function () {
  console.log(`Server stated on port ${port}`);
});
