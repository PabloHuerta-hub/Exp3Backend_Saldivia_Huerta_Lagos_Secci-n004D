function colores(valor) {
  switch (valor) {
    case "morado":
      /* Crea vaiables con los css respectivos de diseño y las llama borrando las de otros colores no elegidos*/ 
      var a = undefined;
      var b = undefined;
      var link = undefined;
      var elemento = undefined;

      a = document.getElementsByTagName("HTML");
      b = a[0].getElementsByTagName("HEAD");
      elemento = b[0].getElementsByTagName("link")[3];
      elemento.parentElement.removeChild(elemento);
      link = document.createElement("link");
      link.rel = "stylesheet";
      link.type = "text/css";
      link.href = "{% static './css/stylepurlpe.css' %}" ;
      b[0].appendChild(link);

      break;
    case "cafe":
      var a = undefined;
      var b = undefined;
      var link = undefined;
      var elemento = undefined;
      /* selecciona elementos por tag name para realizar cambios de css*/ 
      a = document.getElementsByTagName("HTML");
      b = a[0].getElementsByTagName("HEAD");
      elemento = b[0].getElementsByTagName("link")[3];
      elemento.parentElement.removeChild(elemento);
      link = document.createElement("link");
      link.rel = "stylesheet";
      link.type = "text/css";
      link.href = "{% static './css/stylebrown.css' %}" ;
      b[0].appendChild(link);

      break;
    case "negro":
      var a = undefined;
      var b = undefined;
      var link = undefined;
      var elemento = undefined;

      a = document.getElementsByTagName("HTML");
      b = a[0].getElementsByTagName("HEAD");
      elemento = b[0].getElementsByTagName("link")[3];
      elemento.parentElement.removeChild(elemento);
      link = document.createElement("link");
      link.rel = "stylesheet";
      link.type = "text/css";
      link.href = "{% static './css/styleblack.css' %}" ;
      b[0].appendChild(link);
      break;
    default:
      console.log("Cae en un error");
      break;
  }
}

function validacion() {
  nom = document.getElementById("nom").value;
  ape = document.getElementById("ape").value;
  user = document.getElementById("user").value;
  dire = document.getElementById("direccion").value;
  email = document.getElementById("email").value;
  pass = document.getElementById("pass").value;
  if (nom == null || nom.length == 0 || /^\s+$/.test(nom)) {
    alert("Debe ingresar un nombre");
    document.getElementById("nom").value = "";
    document.datos.nom.focus();
    return false;
  }

  if (ape == null || ape.length == 0 || /^\s+$/.test(ape)) {
    alert("Debe ingresar un apellido válido");
    document.getElementById("ape").value = "";
    document.datos.ape.focus();
    return false;
  }

  if (user == null || user.length == 0 || /^\s+$/.test(user)) {
    alert("Debe ingresar un usuario válido");
    document.getElementById("user").value = "";
    document.datos.user.focus();
    return false;
  }

  if (dire == null || dire.length == 0 || /^\s+$/.test(dire)) {
    alert("Debe ingresar una dirección válida");
    document.getElementById("direccion").value = "";
    document.datos.dire.focus();
    return false;
  }

  if (email == null || email.length == 0 || /^\s+$/.test(email)) {
    alert("Debe ingresar un correo válido");
    document.getElementById("direccion").value = "";
    document.datos.email.focus();
    return false;
  }
  if (pass == null || pass.length == 0 || /^\s+$/.test(pass)) {
    alert("Debe ingresar una contraseña válida");
    document.getElementById("pass").value = "";
    document.datos.pass.focus();
    return false;
  }
  return alert("Te has registrado con exito");
}
