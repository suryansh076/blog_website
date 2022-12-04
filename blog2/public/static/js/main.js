
var reg_username = document.getElementById('form3Example1c').value;
var reg_pass1 = document.getElementById('form3Example4c').value;
var reg_pass2 = document.getElementById('form3Example4cd').value;
var reg_email = document.getElementById('form3Example3c').value;
var csrf = document.getElementById('csrf').value

function logout_user()
{
    var csrf = document.getElementById('csrf').value
    var p=fetch('/api/logging_out/',{ method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf
    }})
    p.then(request =>{
        console.log(request.status)
        return request.json()
    }).then(request =>{
        console
        if (request.status==200)
        { 
            
            alert("wanna log out")
            window.location.href=('/');
        }
    })
}

function login() {
    var username = document.getElementById('loginUsername').value;
    var password = document.getElementById('loginPassword').value;
    
    if (username == '' && password == '') {
        alert("you must enter both the fields");
    }
    var data = {
        'username': username,
        'password': password
    }
    var p=fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf
        },
        body: JSON.stringify(data),
        
    })
    p.then(response => {
        // console.log(response)
        // console.log(request.message)
        return response.json()
    }).then(response => {
        console.log(response.status)
        console.log(response);
        if (response.status==200)
        {
            // console.log("hello and welcome")
            window.location.href=('/');
        }
        else{
            alert(response.message);
            window.location.reload();
        }
    })
    .catch(function(error){
        console.log(error);
    });
}
function signup(){
    console.log("hello sighnup😘😘😘");

}