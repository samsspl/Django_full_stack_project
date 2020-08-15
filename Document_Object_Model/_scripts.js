// getting object from document for styling, eg h1

var header = document.querySelector("h1");

//setting color to h1 u using js script through DOM.
// header.style.color = "blue";

//writing function to rotate different colors
// https://stackoverflow.com/questions/1484506/random-color-generator for the getRandomColor function

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
  
  
// function changeHeaderColor() {
//     colorInput = getRandomColor();
//     header.style.color = colorInput;
// }

// setInterval("changeHeaderColor()", 500);

setInterval("header.style.color = getRandomColor()", 500); // another way of writing the same code written above

var p = document.querySelector('p');

//modifing the first paragraph inside html through DOM.
p.innerHTML = ("You will use the javascript file to continually change the size of the header, but first we need to learn how to use JavaScript to actually grab the HTML objects from the DOM.<strong><em> Not in HTML file but Edited in Bold letter </em></strong>")

var 