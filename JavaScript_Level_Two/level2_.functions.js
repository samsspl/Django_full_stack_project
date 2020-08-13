// function hello() {
//     console.log("hello world!");
// }

// function helloYou(name) {
//     console.log("hello "+name);
// }

// function AddNum(num1,num2) { 
//     console.log(num1+num2);
// }

// function helloSomeone(name="Dunky") {  //this function has a default name set in place in the case of the function was called without passing arguments.
//     console.log("hello "+name);
// }
// function formal(name="Sam",title='sir') {
//     return title+ " "+name;
// } 

// function timeFive(numInput) { //numInput and result are local scope to the function. not able to access them from outside of the function
//     var result = numInput * 5;
//     return result;
// }

// var g = "global G"
// var stuff = "Global STUFF"

// function fun(stuff) {
//     console.log(g);
//     stuff = "Releasing stuff inside func";
//     console.log(stuff);
// }
// fun(stuff)
// console.log(stuff);
/* 
    global var "stuff" was never modified when passing to the function, stuff inside the function is different from the stuff outside the function
*/