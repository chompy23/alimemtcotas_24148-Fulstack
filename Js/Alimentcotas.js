var nom;
var ape;
var calle;
var num;
var ciud;
var codPost;
var tel;
var correo;

function leer() {
  nom = document.querySelector(".item3-page2 p #nombre").value;
  let valNom = verificarLiterales(nom);
  if (valNom) {
    alert("Nombre mal escrito");
  }
  ape = document.querySelector(".item3-page2 p #apellido").value;
  let valApe = verificarLiterales(ape);
  if (valApe) {
    alert("Apellido mal escrito");
  }
  calle = document.querySelector(".item3-page2 p #calle").value;
  let valCalle = verificarLiterales(calle);
  if (valCalle) {
    alert("Nombre de Calle mal escrito");
  }
  num = document.querySelector(".item3-page2 p #numero").value;
  let valDir = verificarDireccion(num);
  if (valDir) {
    alert("Dirección mal escrito");
  }
  ciud = document.querySelector(".item3-page2 p #ciudad").value;
  let valCiud = verificarLiterales(ciud);
  if (valCiud) {
    alert("Nombre de ciudad mal escrito");
  }
  codPost = document.querySelector(".item3-page2 p #codigoPostal").value;
  let valCodigo = validarCodigoPostal(codPost);
  if (!valCodigo) {
    alert("Codigo Postal mal escrito");
  }
  tel = document.querySelector(".item3-page2 p #telefono").value;
  let valTel = verificar(tel);
  if (valTel) {
    alert("Numero de Telefono mal escrito");
  }
  correo = document.querySelector(".item3-page2 p #correo").value;
  let valEmail = validarEmail(correo);
  if (!valEmail) {
    alert("Direccion de correo incorrecta");
  }
  if (
    !valNom &&
    !valApe &&
    !valCalle &&
    !valDir &&
    !valCiud &&
    valCodigo &&
    !valTel &&
    valEmail
  ) {
    console.log("confirmado");
    document.querySelector(".item3-page2 p #enviar").style.visibility =
      "visible";
  }
}

function verificar(datos) {
  for (let i = 0; i < datos.length; i++) {
    if (datos.charCodeAt(i) >= 48 && datos.charCodeAt(i) <= 57) {
    } else {
      return true;
    }
  }
}
function validarEmail(email) {
  // Expresión regular para validar un correo electrónico
  const regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
  return regex.test(email);
}
function verificarDireccion(datos) {
  if (datos instanceof String && datos.length <= 11) {
    return true;
  }
}
function validarCodigoPostal(codPost) {
  // Expresión regular para validar un coódigo postal
  const pattern = /[a-zA-Z]{1}[0-9]{4}[a-zA-Z]{3}/;
  return pattern.test(codPost);
}

function verificarLiterales(datos) {
  if (datos == "") {
    return true;
  }
  for (const iterator of datos) {
    if (
      iterator == "0" ||
      iterator == "1" ||
      iterator == "2" ||
      iterator == "3" ||
      iterator == "4" ||
      iterator == "5" ||
      iterator == "6" ||
      iterator == "7" ||
      iterator == "8" ||
      iterator == "9" ||
      iterator == "/" ||
      iterator == "?" ||
      iterator == "+" ||
      iterator == "-" ||
      iterator == "$" ||
      iterator == "%"
    ) {
      return true;
    }
  }
}

var disparo = document.querySelector(".item3-page2 p #envio");
disparo.onclick = leer;
