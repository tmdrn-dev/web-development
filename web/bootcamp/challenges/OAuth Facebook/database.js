const mongoose = require("mongoose");
var findOrCreate = require("mongoose-findorcreate");

mongoose.connect("mongodb://localhost:27017/userDB");
UserSchema = new mongoose.Schema({
  email: String,
  password: String,
  facebookId: String,
});

UserSchema.plugin(findOrCreate);

User = mongoose.model("user", UserSchema);

module.exports = User;
