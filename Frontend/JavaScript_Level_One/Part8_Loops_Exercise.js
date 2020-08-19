/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var wo = "hello";
var len = wo.length;
while(len > 0){
    console.log(wo);
    len--;
}

// For Loop
for(var k = 0; k < wo.length; k++){
    console.log(wo);
}



/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
console.log("while loop");
// While Loop
var num = 0;
while(num != 26){
    if(num%2 === 1){
        console.log(num);
    }
    num++;
}

// METHOD TWO
// For Loop
console.log("for loop");
for(var l = 0; l <= 25; l++){
    if(!(l%2 === 0)){
        console.log(l);
    }
}