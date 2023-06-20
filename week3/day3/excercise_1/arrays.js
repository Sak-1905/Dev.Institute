var names=["Tom","Paul","Rita","Pierre","Jack","Jill","James","Jenny","Jesse","Jasmine","Jude","Jade"];

// console.log(names[0]);
// console.log(names[1]);
// console.log(names[2]);
// console.log(names[3]);
// console.log(names[4]);

// console.log(names.length); //get the length of an array (number of elements)

// for (var i=0; i<names.length; i++){
//     console.log(names[i]);
// }

for (var name in names){
    console.log(names[name]);
}


ages=[10,20,30,40,50,60,70,80,90,100];

//for in loop (for accessing the index of arrays)
// for (var age in ages){
//     console.log(ages[age]);
// }

//for of loop (for directly accessing values of arrays)
for (var age of ages){
    console.log(age);
}

person={
    name: "John",
    lastName: "Doe",
    age: 30,
    phone: "1234567890",
    address: "123 Main St",
    married: true,
    children:["Tom","Paul"]
}

for (var key in person){
    console.log(key);
    console.log(person[key]);
}


