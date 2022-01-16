const express = require("express");
const mongoose = require("mongoose");
const md5 = require("md5");
const app = express();

app.use(express.static(__dirname + "/public"));
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

mongoose.connect("mongodb://localhost:27017/userDB");
const userSchema = new mongoose.Schema({
  email: String,
  password: String,
});

const User = mongoose.model("user", userSchema);

app.route("/").get(function (req, res) {
  res.render("home");
});

app
  .route("/login")
  .get(function (req, res) {
    res.render("login");
  })
  .post(function (req, res) {
    const email = req.body.username;
    const password = md5(req.body.password);

    User.findOne({ email: email }, function (err, doc) {
      if (err) {
        res.send(err);
      } else {
        if (doc) {
          if (doc.password == password) {
            res.render("secrets");
          } else {
            res.sendStatus(401);
          }
        } else {
          res.sendStatus(404);
        }
      }
    });
  });

app
  .route("/register")
  .get(function (req, res) {
    res.render("register");
  })
  .post(function (req, res) {
    const userEmail = req.body.username;
    User.findOne({ email: userEmail }, function (err, doc) {
      if (err) {
        res.send(err);
      } else {
        if (doc) {
          res.sendStatus(409);
        } else {
          const newUser = new User({
            email: userEmail,
            password: md5(req.body.password),
          });

          newUser.save(function (err) {
            if (err) {
              res.send(err);
            } else {
              res.render("secrets");
            }
          });
        }
      }
    });
  });

const port = 3000;
app.listen(port, function () {
  console.log(`Server stated on port ${port}`);
});
