



mycheck_pass = (e) => {

    const password = e.target.value;
    let e1 = document.getElementById("mye1")
    let e2 = document.getElementById("mye2")
    let e3 = document.getElementById("mye3")
    e1.hidden=e2.hidden=e3.hidden=false;
    if(password=="")
    {
        e1.hidden=e2.hidden=e3.hidden=true;
    }
    let specail_cha_rex = /(?=.*[!@#$%^&*()_+\-=[\]{};':"\\|,.<>/?])/;
    let atleat_one_Capt_lett_rex =/([A-Z])/
    if(password.length>=6){
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



myemail_required = (e) =>
{
    let email = e.target.value
    let Emailalert = document.getElementById("myEmailalert")
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

mylnreuired =(e) =>
{
    let ln = e.target.value;
    let lnalert = document.getElementById("mylnalert");
    lnalert.hidden= false;
    if(ln.length>0){
        lnalert.hidden= true;
    }
}
myln_on_focus = (e) =>
{
    let lnalert = document.getElementById("mylnalert");
    lnalert.hidden= false;
    lnreuired(e)
}

myfnreuired =(e) =>
{
    let fn = e.target.value;
    let fnalert = document.getElementById("myfnalert");
    fnalert.hidden= false;
    if(fn.length>0){
        fnalert.hidden= true;
    }
}
myfn_on_focus = (e) =>
{
    let fnalert = document.getElementById("myfnalert");
    fnalert.hidden= false;
    fnreuired(e)
}

mysshow_password =(e) =>
{
const passwordInput = document.getElementById('myPassword1');
const showp = document.getElementById('mysigshowp');

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
