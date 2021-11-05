$(document).ready(function () {
  console.log("loading complete!");
});

let h1 = $("h1");
/* Style */
// style getter
console.log(h1.css("color"));
console.log(h1.css("font-size"));

// style setter
h1.css("color", "tomato");

/* Class */
// add class
h1.addClass("big-title");
h1.addClass("big-title margin-50");
if (h1.hasClass("margin-50")) {
  console.log(true);
}

// remove class
// h1.removeClass("big-title");

/* Attribute */
// attribute getter
console.log($("a").attr("href"));
// attribute setter
console.log($("a").attr("href", "http://naver.com"));

/* Text&HTML*/
let buttons = $("button");
// access innerText
buttons.text("<em>Don't click me<em>");
// access innerHtml
buttons.html("<em>Don't click me<em>");

buttons.click(function () {
  h1.css("color", "purple");
});

/* Callback*/
// method
$("input").keydown(function (event) {
  h1.text(event.key);
});

// on method
// $("input").on("keydown", function (event) {
//   h1.text(event.key);
// });

$("h1").on("mouseover", function (event) {
  h1.css("color", "gold");
});
