var numbers = [3, 56, 2, 48, 5];

//const squareArray = numbers.map(function (x) {
//   return x * x;
// });
const squareArray = numbers.map((x) => x * x);
console.log(squareArray);

////Map -Create a new array by doing something with each item in an array.
// const newNumbers = numbers.map(function (x) {
//   return x * 2;
// });
const doubleArray = numbers.map((x) => x * 2);
console.log(doubleArray);

//////Filter - Create a new array by keeping the items that return true.
// const newNumbers = numbers.filter(function(num) {
//   return num < 10;
// });
const filterArray = numbers.filter((x) => x < 10);
console.log(filterArray);

//Reduce - Accumulate a value by doing something to each item in an array.
// var newNumber = numbers.reduce(function (accumulator, currentNumber) {
//     return accumulator + currentNumber;
// })
const reduceNumber = numbers.reduce((x, y) => x + y);
console.log(reduceNumber);

////Find - find the first item that matches from an array.
// const newNumber = numbers.find(function (num) {
//   return num > 10;
// })
const findNumber = numbers.find((x) => x > 10);
console.log(findNumber);

////FindIndex - find the index of the first item that matches.
// const newNumber = numbers.findIndex(function (num) {
//   return num > 10;
// })
const findIndexNumber = numbers.findIndex((x) => x > 10);
console.log(findIndexNumber);
