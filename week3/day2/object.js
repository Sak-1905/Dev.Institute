
car={
    id:"12345",
    make:"BMW",
    model:"X5",
    color:"black",
    mileage: 100000,
    paid: true,
}

person={
    id:"12345",
    dob:"01/01/1990",
    gender: "Male",
    name: "John Doe",
}

console.log(car.id);

console.log(person.gender);

console.log(car.id+" "+person.gender);

person.id="763621083";
console.log(person.id);


console.log(person['name']);

person.married=true; //adding a new property

console.log(person);

delete person.dob;
console.log(person);


test={
    ids: [1,2,3,4,5,6,7,8,9,10],
    names: ["John","Jane","Jack","Jill","James","Jenny","Jesse","Jasmine","Jude","Jade"],
}

console.log(test.ids[9]);

test.ids.push(11);
console.log(test);