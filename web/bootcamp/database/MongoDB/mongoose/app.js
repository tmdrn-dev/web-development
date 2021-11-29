const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/fruitDB');

const fruitSchema = mongoose.Schema({
    name: String,
    rating: Number,
    review: String
})

const Fruit = mongoose.model('Fruit', fruitSchema);

const apple = new Fruit({ 
    name: 'Apple',
    rating: 7,
    review: "Pretty solid as a fruit."
});

const kiwi = new Fruit({ 
    name: 'Kiwi',
    rating: 6,
    review: "Pretty solid as a fruit."
});

const banana = new Fruit({ 
    name: 'Banana',
    rating: 5,
    review: "Pretty solid as a fruit."
});

// Insert many documents
const arr = [apple, kiwi, banana];
Fruit.insertMany(arr, function(error, docs) {
    if (error) {
        console.error("error: " + error);
    } else {
        console.log("Saved successfully.");
    }
    // console.log("docs: " + docs);
});

const personSchema = mongoose.Schema({
    name: String,
    age: Number
})

const Person = mongoose.model('Person', personSchema);
const person = new Person({
    name: "Jonh",
    age: 37
})

// Insert only one document
person.save();
