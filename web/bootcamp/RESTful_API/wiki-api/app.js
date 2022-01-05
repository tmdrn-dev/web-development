const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));
app.use("/static", express.static(__dirname + "/public"));

mongoose.connect("mongodb://localhost:27017/wikiDB");

const articleSchema = new mongoose.Schema({
  title: String,
  content: String,
});

const Article = mongoose.model("article", articleSchema);

app
  .route("/articles")
  .get(function (req, res) {
    Article.find(function (err, docs) {
      if (err) {
        res.send(err);
      } else {
        res.send(docs);
      }
    });
  })
  .post(function (req, res) {
    const article = new Article({
      title: req.body.title,
      content: req.body.content,
    });
    article.save(function (err) {
      if (!err) {
        res.sendStatus(200);
      } else {
        res.send(err);
      }
    });
  })
  .delete(function (req, res) {
    Article.deleteOne({ title: req.body.title }, function (err) {
      if (!err) {
        res.sendStatus(200);
      } else {
        res.send(err);
      }
    });
  });

const port = 3000;
app.listen(port, function () {
  console.log(`wiki-api app listening at http://localhost:${port}`);
});
