const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/userDB");
UserSchema = new mongoose.Schema({
  name: String,
  email: String,
});

User = mongoose.model("user", UserSchema);

module.exports = User;
