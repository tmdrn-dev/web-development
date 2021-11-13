const express = require("express");
const app = express();

app.get("/", function (req, res) {
  res.send("greeting!");
});

app.listen(3000, function () {
  console.log("Server is running");
});
