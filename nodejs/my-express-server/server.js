const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("<h1>Greeting!</h1");
  // res.sendFile(__dirname + "/index.html");
});

app.get("/contact", (req, res) => {
  res.send("seungku.dev@gmail.com");
});

app.get("/about", (req, res) => {
  res.send("web developer newbie");
});

app.get("/hobbies", (req, res) => {
  res.send("study😋");
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
