function read(){
    var name=document.getElementById("getname").value;
    var roll=document.getElementById("getnum").value;
    var admission=document.getElementById("getadm").value;
    var age=document.getElementById("getage").value
    console.log(name);
    console.log(roll);
    console.log(admission);
    console.log(age);
    if(age==18){
        alert("eligible");}
        else{ alert("no no no")}
    }