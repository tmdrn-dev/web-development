const express = require("express");
const https = require("https");
const app = express();
const appPort = 3000;

app.use("/", express.static(__dirname + "/public"));
app.use(express.urlencoded({ extended: true }));

app.get("/", function (req, res) {
  res.sendFile(__dirname + "/signup.html");
});

app.post("/", function (req, res) {
  const firstName = req.body.fName;
  const lastName = req.body.lName;
  const email = req.body.email;
  const data = {
    members: [
      {
        email_address: email,
        status: "subscribed",
        merge_fields: {
          FNAME: firstName,
          LNAME: lastName,
        },
      },
    ],
  };

  const url = "https://us20.api.mailchimp.com/3.0/lists/52d0bfaedc";
  const options = {
    method: "post",
    auth: "seungku:33cc250fb5672d25264307aca2a78a6d-us20",
  };

  const request = https.request(url, options, function (response) {
    if (response.statusCode === 200) {
      res.sendFile(__dirname + "/success.html");
    } else {
      res.sendFile(__dirname + "/failure.html");
    }

    response.on("data", function (data) {
      console.log(JSON.parse(data));
    });
  });

  const jsonData = JSON.stringify(data);
  request.write(jsonData);
  request.end();
});

app.post("/failure", function (req, res) {
  res.redirect("/");
});

app.listen(appPort, function () {
  console.log(`Server is running`);
});
