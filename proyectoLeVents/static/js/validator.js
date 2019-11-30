$("#formulario").validate(
    {
        rules:{
            "first_name":{
                required:true,
                myField: { lettersonly: true }
            },
            "last_name":{
                required:true,
                myField: { lettersonly: true }
            },
            "username":{
                required:true,
                minlength:4,
                myField: { lettersonly: true }
            },
            "email":{
                required:true,
                email:true
            },
            "password1":{
                required:true,
                minlength:8
            },
            "password2":{
                required:true,
                minlength: 8
            }
        },  // -----> Fin de las reglas
        messages:{
            "first_name":{
                required:"* Te falto el Nombre",
                myField: "* Este campo solo permite letras"
            },
           "last_name":{
                required: "* Te falto poner el Apellido",
                myField: "* Este campo solo permite letras"
            },
            "username":{
                required: "* Te falto escribir el usuario",
                minlength: "* Tu nombre de usuario debe tener mas de 4 caracteres",
                myField: "* Solo se permiten letras"
            },
            "email":{
                required: "* Tienes que introducir un mail",
                email: "* No tiene formato de email"
            },
            "password1":{
                required:"* Tienes que introducir una contraseña",
                minlength: "* Tiene que tener minimo 8 caracteres"
            },
            "password2":{
                required:"* Tienes que introducir una contraseña",
                minlength: "* Tiene que tener minimo 8 caracteres"
            }
        }
    }   // ---> final del objeto json
    
);

$('#first_name').keypress(function (e) {
    var regex = new RegExp("^[a-zA-Z]+$");
    var str = String.fromCharCode(!e.charCode ? e.which : e.charCode);
    if (regex.test(str)) {
        return true;
    }
    else
    {
    return false;
    }
}); 
$('#last_name').keypress(function (e) {
    var regex = new RegExp("^[a-zA-Z]+$");
    var str = String.fromCharCode(!e.charCode ? e.which : e.charCode);
    if (regex.test(str)) {
        return true;
    }
    else
    {
    return false;
    }
}); 