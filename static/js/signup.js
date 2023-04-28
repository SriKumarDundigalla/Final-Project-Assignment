$(function () {
    $('[data-bs-toggle="tooltip"]').tooltip();
  });



check_pass = (e) => {

    const password = e.target.value;
    let e1 = document.getElementById("e1")
    let e2 = document.getElementById("e2")
    let e3 = document.getElementById("e3")
    e1.hidden=e2.hidden=e3.hidden=false;
    if(password=="")
    {
        e1.hidden=e2.hidden=e3.hidden=true;
    }
    let specail_cha_rex = /(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?])/;
    let atleat_one_Capt_lett_rex =/([A-Z])/
    if(password.length>=6){
        console.log("HII")
        e1.hidden=true;
    }
    if(specail_cha_rex.test(password))
    {

       e2.hidden=true;
    }
    if(atleat_one_Capt_lett_rex.test(password)){
        e3.hidden=true;
    }

}

chech_match = (e) =>{
    let alert1 = document.getElementById("alert1")
    alert1.hidden =false;
    let password = document.getElementById("Password1").value
    let button = document.getElementById('btnlogin')
    let password2 = e.target.value
    if(password2=="")
    {
        alert1.hidden =true;
    }
    if(password===password2)
    {
        alert1.hidden =true;
        button.disabled =false;
    }

}

email_required = (e) =>
{
    let email = e.target.value
    let Emailalert = document.getElementById("Emailalert")
    Emailalert.hidden =false;
    let emial_rex =/^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/
    Emailalert.hidden =false;

    if(email=="")
    {
        Emailalert.hidden =true;
    }
    if(emial_rex.test(email))
    {
        Emailalert.hidden =true;
    }
}

lnreuired =(e) =>
{
    let ln = e.target.value;
    let lnalert = document.getElementById("lnalert");
    lnalert.hidden= false;
    if(ln.length>0){
        lnalert.hidden= true;
    }
}
ln_on_focus = (e) =>
{
    let lnalert = document.getElementById("lnalert");
    lnalert.hidden= false;
    lnreuired(e)
}

fnreuired =(e) =>
{
    let fn = e.target.value;
    let fnalert = document.getElementById("fnalert");
    fnalert.hidden= false;
    if(fn.length>0){
        fnalert.hidden= true;
    }
}
fn_on_focus = (e) =>
{
    let fnalert = document.getElementById("fnalert");
    fnalert.hidden= false;
    fnreuired(e)
}

sshow_password =(e) =>
{
const passwordInput = document.getElementById('Password1');
const showp = document.getElementById('sigshowp');

  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    showp.classList.remove('bi-eye')
    showp.classList.add('bi-eye-fill')
  } else {
    passwordInput.type = 'password';
    showp.classList.remove('bi-eye-fill')
    showp.classList.add('bi-eye')
  }

}

sshow_cpassword =(e) =>
{
const passwordInput = document.getElementById('Password2');
const showp = document.getElementById('sigshowcp');

  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    showp.classList.remove('bi-eye')
    showp.classList.add('bi-eye-fill')
  } else {
    passwordInput.type = 'password';
    showp.classList.remove('bi-eye-fill')
    showp.classList.add('bi-eye')
  }

}