function displayMessage() {
    alert('helloWorld');
  }
  
  
  // document.querySelector('#btn2').addEventListener('click', function(){ //anonymous function
  //     alert("Btn 2 cliucked");
  // });
  //document.querySelector('#btn2').addEventListener('click', displayMessage); //named function
  
  document.getElementById('btn2').onclick = function() { //onclick
      alert("Btn 2 clicked");
  }
  
  
  
  document.body.onload = function() { //onload
      alert("Page loaded");
  }
  
  document.querySelector('#myLink').addEventListener('mouseover', function(){
      alert(this.innerHTML); //using this to access the current selected object
  });
  
  document.querySelector('#myInput').addEventListener('keydown', function(){
      alert("key pressed");
  });
  
  
  function insertRow() {
      new_row=document.createElement('tr'); //create element table row
      col1=document.createElement('td');  //table data 1
      col2=document.createElement('td'); //table data 2
  
      col1.innerHTML="Row3 cell1";
      col2.innerHTML="Row3 cell2";
  
      new_row.appendChild(col1);
      new_row.appendChild(col2);
  
      table=document.getElementById('sampleTable');
      table.appendChild(new_row);
  }