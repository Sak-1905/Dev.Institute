function compareNumbers(userNumber,computerNumber){
    result=false;
    if (userNumber==computerNumber){
        alert("WINNER");
        result=true;
    }else if (userNumber<computerNumber){
        alert("Your number is smaller then the computers, guess again");
    }else if (userNumber>computerNumber){
        alert("Your number is bigger then the computers, guess again");
    }
    return result;
}

function input(){
    var userNumber=prompt("Enter a number between 0 and 10");
    // if (typeof(userNumber)!=Number){
    possibleNumbers=["0","1","2","3","4","5","6","7","8","9","10"];
    if (!(userNumber in possibleNumbers)){
        alert("Sorry Not a number, Goodbye");
    }else{
        var convertedUserNumber=parseInt(userNumber); //convert to integer
        var computerNumber=Math.floor(11*Math.random());
    }
    return {convertedUserNumber,computerNumber};

}



function playTheGame(){

    if (confirm("Do you want to play the game?") == true) {
        counter=0;
        result = false; //flag
        var computerNumber=Math.floor(11*Math.random());
        while (counter<3 && result==false){
            let numbers=input();
            var userNumber=numbers.convertedUserNumber;
            // var computerNumber=numbers.computerNumber;
            
            // console.log(`${userNumber} , ${computerNumber}`);
            result=compareNumbers(userNumber,computerNumber);
            counter=counter+1;
    
            if (counter==3 && result==false){
                alert("out of chances");
            }
        }
        
    }else{
        alert("No problem, Goodbye");
    }
}