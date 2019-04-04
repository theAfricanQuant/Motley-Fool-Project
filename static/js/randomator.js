// Randomization of the Quotes in the Sidbar of article pages

function rearrangeQuotes() {
  // Select all elements with the class of 'quote'
  var quotes = $(".quote");

  // Loop through the quotes
  for (var i = 0; i < quotes.length; i++) {
    /*
      Randomly generates a number between 0-3 (three being the lenght of the array)
      Does some of the random math and assigns to two variables.
      Occasionally these are the same results due to the small array length and nothing changes.
    */
    var target = Math.floor(Math.random() * quotes.length - 1) + 1;
    var target2 = Math.floor(Math.random() * quotes.length - 1) + 1;

    // Uses the jQuery libray eq() -- https://api.jquery.com/eq/
    quotes.eq(target).before(quotes.eq(target2));
  }
}

// Event listener for the RANDOM-ATOR button click!
document.addEventListener("click", rearrangeQuotes);
