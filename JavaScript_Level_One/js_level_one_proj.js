var cond = 0; //Checking if 4 conditions are met 
var fn = prompt("Please enter your First Name: ");
var ln = prompt("Please enter your Last Name: ");
if(fn[0] === ln[0]){
    cond++;
}

var age = prompt("How old are you?");
if(age > 20 && age < 30){
    cond++;
}

var height = prompt("How tall are you in centimeters?");
if(height => 170){
    cond++;
}

var pet = prompt("What is the name of your pet?");

alert("Thank you so much for the information.")
var last_ele = pet[pet.length-1];
if(last_ele === "y"){
    cond++;
}

if(cond === 4){
    console.log("Welcome Comrade! You've passed the Spy Test");
}else{
    console.log("Sorry, nothing to see here.");
}