var planets=[
    {name:"Mercury",moon:true},
    {name:"Venus",moon:false},
    {name:"Earth",moon:true},
    {name:"Mars",moon:true},
    {name:"Jupyter",moon:false}
    ];
    
    map=document.body.querySelector("#map");
    
    
    // for(i=0;i<planets.length;i++){
    
    
    // function displayPlanet(planet){
    //     map.appendChild(planet);
    // }
    
    counter=0;
    function displayPlanet(){
    
        if (counter==planets.length){
            return;
        }else{
            myplanet=planets[counter];
            console.log(myplanet);
            planet=document.createElement("div"); //creating div element
            // planet.setAttribute("class","planet"); 
            planet.classList.add("planet"); //adding class planet to div element
            // planet.classList.add("hidden");
        
            var name=myplanet.name;
            planetName=document.createElement("p"); 
            planetName.innerHTML=myplanet.name;
            planet.appendChild(planetName);
        
        
            if (myplanet.moon==true){
                moon=document.createElement("div");
                moon.classList.add("moon");
                planet.appendChild(moon);
            }
    
            map.appendChild(planet);
            counter=counter+1;
            // if (counter==1){
            //     clearTimeout(displayPlanet);
            // }
            setTimeout(displayPlanet,2000);
            // setInterval(displayPlanet, 500);
    
           
            // displayPlanet(planet);
        } 
    }
    
    displayPlanet(planets[0]);
    
    
    
    // setInterval(function(){
    //     status=document.querySelector("#map").classList.toggle("hidden");
    // },5000);
    
    
    
    