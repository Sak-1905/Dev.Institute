var temp = 24;

if (temp >= 24) { //greater than comparison operator
    console.log("Turn on the Ai conditionning");
}else{
    console.log("Turn on the heater");
}

// if (temp == 26){ //equality comparison operator
//     console.log("The temperature is 26");
// }

// if (temp != 25){ //inequality comparison operator
//     console.log("The temperature is not 25");
// }


//if else elseif statements
price=101;

if (price<=100){
    console.log("Its cheap");
}else if (price<= 1000){
    console.log("Its affordable");
}else if (price<= 10000){
    console.log("Its expensive");
}else{
    console.log("Its very expensive");
}

//switch
switch(price){
    case 100:
        console.log("Its cheap 2");
        break;
    case 1000:
        console.log("Its affordable 2");
        break;
    case 10000:
        console.log("Its expensive 2");
        break;

    default:
        console.log("Its very expensive 2");
        break;
}
debugger;

//switch
switch(true){
    case (price<=100):
        console.log("Its cheap 3");
        break;
    case (price<=1000):
        console.log("Its affordable 3");
        break;
    case (price<=10000):
        console.log("Its expensive 3");
        break;

    default:
        console.log("Its very expensive 3");
        break;
}
//boolean operators
// && (and) - all conditions should be satisfied
// || (or) - at least one condition should be satisfied
// ! (not)

let total=5000;
let premiumCustomer= true;

if (total>10000 && premiumCustomer==true){  false && true
    console.log("You get a 10% discount");
}else if (total>10000 || premiumCustomer==true){
    console.log("You get a 5% discount");
}else{
    console.log("You get no discount");
}

//input from user
    // var newtemp=prompt("Enter the temperature");
    // console.log(newtemp);
