
let userinput = 0
let total=0; 
let guess = 0 // this will hold user guess input  
let numberOfGuess = 1
let screeninfo = "This is a screen"; //string used for screen output. 



for(let i=0; i<document.querySelectorAll(".box").length; i++){

    document.querySelectorAll(".box")[i].addEventListener("click", buttonPressed);
}


//Single Function for all buttons but clear
function buttonPressed(){
    if(this.innerHTML=="C"){
    
    currentdigit=0; 
    previouspush=0;
    maths = "none";
    screeninfo ="";
    document.querySelector('#screen').innerHTML = "Play Again?";
    }
    
    else if(this.innerHTML=="+"){
        
        total = Math.floor(Math.random() *100) +1
        document.querySelector("#screen p").innerHTML = "This is guess " + numberOfGuess  
        document.querySelector("#screen2").innerHTML = "Use numkeys on screen to enter guess."
        userinput = 0;
        while (userinput===0){
            if(this.innerHTML=="="){
                userinput = 1
            }
            else{
                iscorrect(total, "1234")
            }
        }
        
    }
    else if(this.innerHTML == 1 || this.innerHTML == 2 || this.innerHTML == 3 || this.innerHTML == 4 || this.innerHTML == 5 || this.innerHTML == 6 || this.innerHTML == 7 || this.innerHTML == 8 ||this.innerHTML == 9 || this.innerHTML == 0){
        document.querySelector("#screen p").innerHTML = this.innerHTML;
    }
    else{
        document.querySelector("#screen p").innerHTML = "The gnomes are working on this button.";
    }
}

// const add=(total, numnum) => if numnum = total{ } 



// function calculator(n1, n2, operator){
//     return(operator(n1, n2));

// }