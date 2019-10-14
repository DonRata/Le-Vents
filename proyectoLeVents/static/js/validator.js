$("#formulario").validate(
    {
        rules:{
            "txtNombre":{
                required:true,
                minlength:5,
                myField: { lettersonly: true }
            },
            "txtEmail":{
                required:true,
                email:true
            },
            "txtRun":{
                required:true
            },
            "txtTelefono":{
                number:true
            },
            "txtFechaNacimiento":{
                required:true,
                date: true
            }
        },  // -----> Fin de las reglas
        messages:{
            "txtNombre":{
                required:"Te falto el nombre!!!!",
                minlength: "Min. Cinco caracteres minimo",
                myField: "Este campo solo permite letras"
            },
           "txtEmail":{
                required: "Te falto el email",
                email:"No tiene el formato email"
            },
            "txtRun":{
                required: "Te falto poner run"
            },
            "txtTelefono":{
                number: "Este campo permite solo numeros"
            },
            "txtFechaNacimiento":{
                required:"Tienes que poner la fecha de nacimiento"
            }
        }
    }   // ---> final del objeto json
    
);

$('#txtNombre').keypress(function (e) {
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