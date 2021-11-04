const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  //   res.send(Buffer.from("<p>index.html</p>"));
  res.sendFile(__dirname + "/index.html");
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
