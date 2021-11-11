const express = require("express");
const app = express();
const appPort = 3000;

app.use("/", express.static(__dirname + "/public"));
app.use(express.urlencoded({ extended: true }));

app.get("/", function (req, res) {
  res.sendFile(__dirname + "/signup.html");
});

app.post("/", function (req, res) {
  console.log(req.body.firstName);
  console.log(req.body.lastName);
  console.log(req.body.email);
});

app.listen(appPort, function () {
  console.log(`Server is running on port:${appPort}`);
});
