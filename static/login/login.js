window.onload = all;

function all() {
    console.log("served login.js")
    var formLogin                       = document.getElementById("loginFormId")
    var formRegister                    = document.getElementById("registerFormId")
    var registerLink                    = document.getElementById("register")
    var passwordRecovery                = document.getElementById("recoverPW")

    formLogin.style.display             = "table"
    formRegister.style.display          = "none"
    
    registerLink.onclick                = toggleRegister

    function toggleRegister() {
        //formLogin.style.display         = "none"
        formRegister.style.display      = "table"

        //registerLink.style.display      = "none"
        passwordRecovery.style.display  = "none"

        return false
    }
}