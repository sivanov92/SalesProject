var userName = document.getElementById('UserName');
var userMail = document.getElementById('UserMail');
var userPosition = document.getElementById('UserPosition');

document.getElementById('SubmitUser').addEventListener('click',addUser);
console.log(document.getElementById('SubmitUser'));
function addUser(){
    console.log(111);
    fetch('http://127.0.0.1:8000/users/',{
        method:"POST",
        headers:{
            'Accept':'application/json, text/plain, */*',
            'Content-type':'application/json'
        },
        body:JSON.stringify({name:userName, email:userMail, position:userPosition})
    })
    .then((res)=>res.json)
    .then((data)=>console.log(data))
} 