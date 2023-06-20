
i=0;

while (i<5){
    console.log("I love coding");
    i++;
}


// while loop
// total=0;
// while(total<5000){
//     item=prompt("Enter item price: ");
//     total=total+parseInt(item);
// }

// console.log(total);


// //do while
// total=6000;
// do{
//     item=prompt("Enter item price: ");
//     total=total+parseInt(item);
// }while(total<5000)
// console.log(total);


//break
// names=[];
// while(true){
//     name=prompt("Enter student name");
//     names.push(name);
//     if (name=="exit"){
//         break; //exit the loop
//     }
// }

// console.log(names);



//continue
for (var i=0; i<10; i++){
    if (i==2){
        continue; //skip the current iteration
    }
    console.log(i);
}