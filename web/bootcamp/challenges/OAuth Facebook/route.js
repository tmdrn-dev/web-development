require("dotenv").config();
const express = require("express");
const passport = require("passport");
var FacebookStrategy = require("passport-facebook").Strategy;
const userDB = require(__dirname + "/database");

passport.use(
  new FacebookStrategy(
    {
      clientID: process.env.FACEBOOK_APP_ID,
      clientSecret: process.env.FACEBOOK_APP_SECRET,
      callbackURL: "http://localhost:3000/auth/facebook/callback",
    },
    function (accessToken, refreshToken, profile, cb) {
      userDB.findOrCreate({ facebookId: profile.id }, function (err, user) {
        return cb(err, user);
      });
    }
  )
);

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

router.get(
  "/auth/facebook",
  passport.authenticate("facebook", {
    scope: ["public_profile", "email"],
  })
);

router.get(
  "/auth/facebook/callback",
  passport.authenticate("facebook", { failureRedirect: "/login" }),
  function (req, res) {
    // Successful authentication, redirect home.
    res.redirect("/");
  }
);

module.exports = router;
