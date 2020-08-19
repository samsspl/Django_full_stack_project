console.log("connected to script");
//Grab the cells
var square_ = document.querySelectorAll('td')

//Restart Game 
var restart = document.querySelector("#b");


// Clear the cells
function clearBoard() {
    for(var i = 0; i < square_.length; i++){
        square_[i].textContent = ' ';
    }
}

restart.addEventListener("click",clearBoard);

// check if the square is already filled
function changeVal() {
    if(this.textContent === ''){
        this.textContent = 'X';
    }else if(this.textContent === 'X'){
        this.textContent = 'O'
    }else{
        this.textContent = '';
    } 
}

//Loops through x o with event listener for the cells
for(var i = 0; i < square_.length; i++){
    square_[i].addEventListener('click', changeVal);
}