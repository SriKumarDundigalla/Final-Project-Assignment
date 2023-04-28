$(function () {
    $('[data-bs-toggle="tooltip"]').tooltip();
  });
login_password = (e) =>{

    let password = e.target.value
    let Lpasswordalert = document.getElementById('Lpasswordalert')
    if(password!="" && password.length >= 6)
    {
        Lpasswordalert.hidden =true;

    }
    else{
        Lpasswordalert.hidden =false;

    }
    
}
login_password_focus = (e) =>
{
    let Lpasswordalert = document.getElementById("Lpasswordalert");
    Lpasswordalert.hidden= false;
    login_password(e)
}
show_password =(e) =>
{
const passwordInput = document.getElementById('lPassword1');
const showp = document.getElementById('showp');

  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    showp.classList.remove('bi-eye')
    showp.classList.add('bi-eye-fill')
  } 
  else {
    passwordInput.type = 'password';
    showp.classList.remove('bi-eye-fill')
    showp.classList.add('bi-eye')
  }

}
login_email = (e) =>
{
    let email = e.target.value
    let Lemailalert = document.getElementById("Lemailalert")
    Lemailalert.hidden =false;
    let emial_rex =/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/
    Lemailalert.hidden =false;

    if(email=="")
    {
        Lemailalert.hidden =true;
    }
    if(emial_rex.test(email))
    {
        Lemailalert.hidden =true;
    }
}




