//grab the paragraph tag and do some modification

var p = document.querySelector("p");

p.innerHTML = ("This is not what you see in HTML in the <strong><em> paragraph </em></strong>for <p> tag");

// grab the id "special" from h4 in html

var special = document.querySelector("#special");
console.log(special);
var specialA = special.querySelector("a"); // grabbing a tag from id special 
console.log(specialA); 
specialA.setAttribute("href","https://www.google.com"); // now the link will take you to google instead of facebook.
specialA.textContent = ("Google Link");