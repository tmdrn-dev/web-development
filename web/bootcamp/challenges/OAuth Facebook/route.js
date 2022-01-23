const express = require("express");
const userDB = require(__dirname + "/database");

const router = express.Router();
router.route("/").get((req, res) => {
  res.render("home");
});

router.route("/login").get((req, res) => {
  res.render("login");
});

router.route("/register").get((req, res) => {
  res.render("register");
});

module.exports = router;
