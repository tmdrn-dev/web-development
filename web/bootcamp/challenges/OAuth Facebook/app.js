const express = require("express");
const router = require(__dirname + "/route");

const app = express();
app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));
app.use(express.urlencoded({ extended: true }));
app.use(router);

const port = 3000;
app.listen(port, function () {
  console.log(`Server stated on port ${port}`);
});
