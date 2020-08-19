var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var HeadThree = document.querySelector("#three");


headOne.addEventListener("mouseover",function () {
    headOne.textContent = "Mouse Currently Over";
    headOne.style.color = "red";
})

headOne.addEventListener("mouseout",function () {
    headOne.textContent = "Hover over me!";
    headOne.style.color = "black";
})


headTwo.addEventListener("click", function () {
    headTwo.textContent = "YOU CLCKED ME!"
    headTwo.style.color = "green";
})

HeadThree.addEventListener("dblclick", function () {
    HeadThree.textContent = "I WAS DOUBLE CLICKED!"
    HeadThree.style.color = "purple";
})