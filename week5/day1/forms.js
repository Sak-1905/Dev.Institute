form1=document.forms[0];
form2=document.forms[1];

// alert(form2.elements[1].value); 
alert(document.forms.length);

form2.elements[1].style.backgroundColor="red";


form2.elements[0].value="Test";

document.forms[0].elements[0].addEventListener("change",function(){
    alert(this.value);
});


document.forms[0].elements[1].addEventListener("input",function(){
    alert(this.value);
});

function getvalue(){
    myForm=document.querySelector("#form3");
    alert(myForm.elements[0].value);
    alert(myForm.elements[1].value);
}


document.querySelector("#A").options[1].value="Pineapple";
document.querySelector("#A").options[1].innerHTML="Pineapple";

document.querySelector("#A").options[1].selected=true;

alert(document.querySelector("#A").selectedIndex);  

document.querySelector("#A").options.add(new Option("Mango","Mango"));
document.querySelector("#A").options.remove(0);


document.forms[3].elements[1].checked=true;


document.querySelector("#form4").addEventListener("submit",function(e){
    alert("form submitted");
});