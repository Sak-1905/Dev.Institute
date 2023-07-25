// Standard propagation
// document.querySelector("#btn1").addEventListener("click", function(){
//     alert("btn1 clicked");
// });

// document.querySelector("#form1").addEventListener("click", function(){
//     alert("form1 clicked");
// });

// document.querySelector("#container").addEventListener("click", function(){
//     alert("container clicked");
// });

//Event capturing (reverse propagration)
// document.querySelector("#btn1").addEventListener("click", function(){
//     alert("btn1 clicked");
// }, true);

// document.querySelector("#form1").addEventListener("click", function(){
//     alert("form1 clicked");
// },true);

// document.querySelector("#container").addEventListener("click", function(){
//     alert("container clicked");
// }, true);

//event bubbling (stop progration)
document.querySelector("#btn1").addEventListener("click", function(event){ //add event as parameter to function
    alert("btn1 clicked");
    // event.preventDefault();
    event.stopPropagation(); //function to stop progration of event
});

document.querySelector("#form1").addEventListener("click", function(){
    alert("form1 clicked");
});

document.querySelector("#container").addEventListener("click", function(){
    alert("container clicked");
});


document.body.children[1].addEventListener("click", function(){
    alert("div clicked");
});


document.querySelector("#jsstyle").addEventListener("click", function(e){
    this.style.color = "red";
    // alert("jsstyle clicked");
    e.stopPropagation();
});