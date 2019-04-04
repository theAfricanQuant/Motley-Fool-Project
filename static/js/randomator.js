// Randomization of the Quotes in the Sidbar of article pages

function rearrangeQuotes() {
  var quotes = $(".quote");
  for (var i = 0; i < quotes.length; i++) {
    var target = Math.floor(Math.random() * quotes.length - 1) + 1;
    var target2 = Math.floor(Math.random() * quotes.length - 2) + 1;
    quotes.eq(target).before(quotes.eq(target2));
  }
}

document.addEventListener("click", rearrangeQuotes);
