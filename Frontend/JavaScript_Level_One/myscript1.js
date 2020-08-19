//uncomment them to test out and connected to html to view
// if else statement

var hot = false;
var temp = 100;

if(temp > 80){
    hot = true;
    console.log("Hot outside");
}else if(temp <= 80 && temp >= 50){
    console.log("Average temp outside");
}else if(temp < 50 && temp >= 32){
    console.log("Its pretty cold out!");
}else {
    console.log("Its very cold out!");
}

// console.log(hot);

// var ham = 10;
// var cheese = 20;

// var  report = "blank";

// if(ham >= 10 && cheese >= 10){
//     report = "Strong sales of both ham and cheese!"
// }else if(ham === 0 && cheese === 0 ){
//     report = "Nothing sold!"
// }else {
//     report = "We had some sales of items"
// }
// console.log(report);

// while loop

// var x = 0;

// while(x < 5){
//     console.log("x is currently: "+x);
//     console.log("x is still less than 5, adding 1 to x");
//     x = x+1;

// }
// console.log("after while loop ended, the value of x is: "+x);
 

// var y = 0;

// while(y < 5){
//     console.log("y is currently: "+y);
//     if(y === 3){
//         console.log("y is EQ to Three");
//         break;
//     }
//     console.log("y is still less than 5, adding 1 to y");
//     y++;
// }

//write a while loop that prints out only the even numbers from 1 to 10
var k = 0;
console.log("printing even numnbers:");
while(k <= 10){
    
    if(k%2 === 0){
        console.log(k);
    }
    k++;
}

// for loop

for(var i = 0; i < 5; i++){
    console.log("Number is: "+i); //iterate through from 0 to 4 
}


var word = "ABCDEFGHIJK"

for(var i = 0; i < word.length; i++){ //printing out letter A to K
    console.log(word[i]);
}

var word = "ABABABABAB"

for(var i = 0; i < word.length; i+=2){ //printing out 5 (A)s
    console.log(word[i]);
}