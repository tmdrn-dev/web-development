const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost:27017/fruitDB");

const fruitSchema = mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  rating: Number,
  review: String,
});

const Fruit = mongoose.model("Fruit", fruitSchema);

const apple = new Fruit({
  name: "Apple",
  rating: 7,
  review: "Pretty solid as a fruit.",
});

const kiwi = new Fruit({
  name: "Kiwi",
  rating: 6,
  review: "Pretty solid as a fruit.",
});

const banana = new Fruit({
  name: "Banana",
  rating: 5,
  review: "Pretty solid as a fruit.",
});

// Insert many documents
// const arr = [apple, kiwi, banana];
// Fruit.insertMany(arr, function(error, docs) {
//     if (error) {
//         console.error("error: " + error);
//     } else {
//         console.log("Saved successfully.");
//     }
//     // console.log("docs: " + docs);
// });

// Delete document
// Fruit.deleteOne({ name: "Peach" });

// Update document
// Fruit.updateOne(
//   { _id: "61a60dc7ea06f05bbc024230" },
//   { review: "Best fruit in my life" },
//   function (err) {
//     if (err) {
//       console.error(err);
//     }
//   }
// );

Fruit.find(function (error, fruits) {
  if (error) {
    console.error(error);
  } else {
    // 2 way Disconnecting connections
    // mongoose.connection.close();
    // mongoose.disconnect();
    fruits.forEach(function (fruit) {
      if (fruit.name === undefined) {
        // fruit.name = "Peach";
        // fruit.save();
      } else {
        console.log(fruit.name);
      }
    });
  }
});

const personSchema = mongoose.Schema({
  name: {
    type: String,
    required: [true, "Please check name field"],
  },
  age: Number,
  favoriteFruit: fruitSchema,
});

const Person = mongoose.model("Person", personSchema);
// const person = new Person({
//   name: "Amy",
//   age: 12,
//   favoriteFruit: apple,
// });

// Insert only one document
// person.save();

// Update document
Person.updateOne(
  // { _id: "61a60dc7ea06f05bbc024233" },
  { name: "Jonh" },
  { favoriteFruit: banana },
  function (err) {
    if (err) {
      console.error(err);
    }
  }
);

Person.deleteMany({ name: "Tom", age: { $gte: 40 } }, function (err) {
  if (err) {
    console.error(err);
  }
});
