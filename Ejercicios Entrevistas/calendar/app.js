/*-------------------------------------------------------
	A partir de una Hora de Inicio y una de Término
	devuelve una matriz
-------------------------------------------------------*/

function generaDia(horario, lun, mar, mie, jue, vie, sab, dom) {
  this.horario = horario;
  this.lun = lun;
  this.mar = mar;
  this.mie = mie;
  this.jue = jue;
  this.vie = vie;
  this.sab = sab;
  this.dom = dom;
}

/*-------------------------------------------------------
	A partir de una Hora de Inicio y una de Término
	devuelve una matriz
-------------------------------------------------------*/
function generaMatriz(Ini, Fin) {
  var ArrAgenda = [];
  Ini = Ini.split(":");
  Fin = Fin.split(":");

  // Obtener horas y minutos (hora Ini)
  var hhIni = parseInt(Ini[0], 10);
  var mmIni = parseInt(Ini[1], 10);

  // Obtener horas y minutos (hora Fin)
  var hhFin = parseInt(Fin[0], 10);
  var mmFin = parseInt(Fin[1], 10);

  var i = 0;
  while (hhIni <= hhFin) {
    x = i++;
    ArrAgenda[x] = hhIni + ":00";
    ArrAgenda[i] = hhIni + ":30";

    hhIni++;
    i++;
  }
  return ArrAgenda;
}

/*-------------------------------------------------------
	Compara dos horas y devuelve la Mayor o la menor
	dependiendo del parametro sTipo donde:
		1 = Hora Menor  
		2 = Hora Mayor
		3 = Hora iguales
-------------------------------------------------------*/
function CompararHoras(sHora1, sHora2, sTipo) {
  if (sTipo === 3)
    console.log("hora1: [" + sHora1 + "]  hora2: [" + sHora2 + "]");

  var arHora1 = sHora1.split(":");
  var arHora2 = sHora2.split(":");

  // Obtener horas y minutos (hora 1)
  var hh1 = parseInt(arHora1[0], 10);
  // hh1 = hh1.toString();
  var mm1 = parseInt(arHora1[1], 10);
  // mm1 = mm1.toString();

  //    if (hh1.length < 2) {
  // 	hh1 = "0"+hh1;
  // }

  // if (mm1.length < 2) {
  // 	mm1 = "0"+mm1;
  // }

  // Obtener horas y minutos (hora 2)
  var hh2 = parseInt(arHora2[0], 10);
  var mm2 = parseInt(arHora2[1], 10);

  // if (sTipo === 3)
  console.log("arHora1: " + hh1 + "-" + mm1);
  console.log("arHora2: " + hh2 + "-" + mm2);
  //console.log("arHora2: " + parseInt(arHora2[0],10) + "-" + parseInt(arHora2[1],10));

  if (sTipo === 1) {
    //1=Retorna la hora mayor
    if (hh1 < hh2 || (hh1 == hh2 && mm1 < mm2)) return sHora1;
    else return sHora2;
  } else if (sTipo === 2) {
    if (hh1 < hh2 || (hh1 == hh2 && mm1 < mm2)) return sHora2;
    else return sHora1;
  } else if (sTipo === 3) {
    if (hh1 === hh2 || (hh1 == hh2 && mm1 === mm2)) return 1;
    else return 0;
  }
}

/*-------------------------------------------------------
	Genero el html para pintar la agenda
-------------------------------------------------------*/
function VerificaDia(Dia, Hora, citas) {
  var txt = "<i class='icon ion-plus-circled txtVerde'></i>  ";
  var obj = JSON.parse(citas);
  //console.log(obj);

  //console.log("Dia:" + Dia + " -Hora:" + Hora + " - obj" + JSON.stringify(obj));
  //console.log(JSON.stringify(obj));
  if (Dia === 1)
    //Lunes
    for (var i in obj) {
      for (var x in obj[i]) {
        if (i === "lunes")
          if (CompararHoras(obj[i][x].hora_inicio, Hora, 3) === 1)
            //dia=i;
            txt = "<i class='icon ion-calendar'> " + obj[i][x].nombre + "</i>";
      }
    }
  if (Dia === 2)
    //Martes
    for (var i in obj) {
      for (var x in obj[i]) {
        if (i === "martes")
          if (CompararHoras(obj[i][x].hora_inicio, Hora, 3) === 1)
            txt = "<i class='icon ion-calendar'> " + obj[i][x].nombre + "</i>";
      }
    }
  if (Dia === 3)
    //Miercoles
    for (var i in obj) {
      for (var x in obj[i]) {
        if (i === "miercoles")
          if (CompararHoras(obj[i][x].hora_inicio, Hora, 3) === 1)
            txt = "<i class='icon ion-calendar'> " + obj[i][x].nombre + "</i>";
      }
    }
  if (Dia === 4)
    //Jueves
    for (var i in obj) {
      for (var x in obj[i]) {
        if (i === "jueves")
          if (CompararHoras(obj[i][x].hora_inicio, Hora, 3) === 1)
            txt = "<i class='icon ion-calendar'> " + obj[i][x].nombre + "</i>";
      }
    }
  if (Dia === 5)
    //Viernes
    for (var i in obj) {
      for (var x in obj[i]) {
        if (i === "viernes")
          if (CompararHoras(obj[i][x].hora_inicio, Hora, 3) === 1)
            txt = "<i class='icon ion-calendar'> " + obj[i][x].nombre + "</i>";
        //console.log("Hora Viernes: " + Hora  + "-" + obj[i][x].hora_inicio);
      }
    }
  if (Dia === 6)
    //Sabado
    for (var i in obj) {
      for (var x in obj[i]) {
        if (i === "sabado")
          if (CompararHoras(obj[i][x].hora_inicio, Hora, 3) === 1) {
            txt = "<i class='icon ion-calendar'></i> " + obj[i][x].nombre;
          }
      }
    }
  if (Dia === 7)
    //Domingo
    for (var i in obj) {
      for (var x in obj[i]) {
        if (i === "domingo")
          if (CompararHoras(obj[i][x].hora_inicio, Hora, 3) === 1)
            txt = "<i class='icon ion-calendar'></i> " + obj[i][x].nombre;
      }
    }

  return txt;
}

/*-------------------------------------------------------
	Genero el html para pintar la agenda
-------------------------------------------------------*/
function GeneraHtml(MatrizHrs, citas) {
  //console.log(JSON.stringify(obj));
  var obj = JSON.parse(citas);
  //console.log(obj);

  var Header = "";
  var Body = "";
  Header =
    "<div class='container'><div class='menu ico left'><<</div>" +
    "<div class='menu dia'>Lunes 09</div>" +
    "<div class='menu dia'>Martes 10</div>  " +
    "<div class='menu dia'>Miercoles 11</div>  " +
    "<div class='menu dia'>Jueves 12</div>  " +
    "<div class='menu dia'>Viernes 13</div>  " +
    "<div class='menu dia'>Sabádo 14</div>  " +
    "<div class='menu dia'>Domingo 15</div> " +
    "<div class='menu ico right'>>></div></div>";

  var HoraConsulta = "";
  for (i = 0; i < MatrizHrs.length; i++) {
    //console.log("HoraMatriz:" + MatrizHrs[i] + " -Hora:" + Hora + " - obj" + JSON.stringify(obj));
    //CompararHoras(MatrizHrs[i], obj.martes[1].hora_inicio, 3)
    //HoraConsulta = MatrizHrs[i] + ":00";
    Body +=
      "<div class='container'><div class='menu horaAgenda left'>" +
      MatrizHrs[i] +
      "</div>" +
      "<div class='menu diaAgenda'>" +
      VerificaDia(1, MatrizHrs[i], citas) +
      "</div>" +
      "<div class='menu diaAgenda'>" +
      VerificaDia(2, MatrizHrs[i], citas) +
      "</div>  " +
      "<div class='menu diaAgenda'>" +
      VerificaDia(3, MatrizHrs[i], citas) +
      "</div>  " +
      "<div class='menu diaAgenda'>" +
      VerificaDia(4, MatrizHrs[i], citas) +
      "</div>  " +
      "<div class='menu diaAgenda'>" +
      VerificaDia(5, MatrizHrs[i], citas) +
      "</div>  " +
      "<div class='menu diaAgenda'>" +
      VerificaDia(6, MatrizHrs[i], citas) +
      "</div>  " +
      "<div class='menu diaAgenda'>" +
      VerificaDia(7, MatrizHrs[i], citas) +
      "</div> " +
      "<div class='menu horaAgenda right'>" +
      MatrizHrs[i] +
      "</div></div>";
  }

  return Header + Body; // The function returns the product of p1 and p2
}

function CalculaRangos(citas) {
  var obj = JSON.parse(citas);
  var arrayRangos = [];
  var horaIni,
    horaFin,
    horaTemp = "";

  for (var i in obj) {
    //console.log(obj[i]);
    for (var x in obj[i]) {
      //console.log(obj[i][x]);

      if (horaIni === undefined) horaIni = obj[i][x].hora_inicio;
      else horaIni = CompararHoras(horaIni, obj[i][x].hora_inicio, 1);

      if (horaFin === undefined) horaFin = obj[i][x].hora_inicio;
      else horaFin = CompararHoras(horaFin, obj[i][x].hora_termino, 2);
    }
    arrayRangos["inicio"] = horaIni;
    arrayRangos["termino"] = horaFin;
  }
  return arrayRangos;
}

/*-------------------------------------------------------
	
-------------------------------------------------------*/
function Agenda(citas) {
  var obj = JSON.parse(citas);
  var Rangos = CalculaRangos(citas);
  console.log("horaIni:" + Rangos["inicio"]);
  console.log("horaIni:" + Rangos["termino"]);
  //console.log("obj:" + JSON.parse(citas));

  var Matriz = generaMatriz(Rangos["inicio"], Rangos["termino"]);

  return GeneraHtml(Matriz, citas);
}

/*-------------------------------------------------------
	
-------------------------------------------------------*/

var citas =
  '{ "lunes" : [' +
  '{ "nombre":"Daniela" , "hora_inicio":"09:00", "hora_termino":"09:30" },' +
  '{ "nombre":"Juanita" , "hora_inicio":"11:30", "hora_termino":"12:00" },' +
  '{ "nombre":"Ignacia" , "hora_inicio":"15:00", "hora_termino":"16:00" },' +
  '{ "nombre":"María Paz" , "hora_inicio":"17:00", "hora_termino":"17:30" } ],' +
  '  "martes" : [' +
  '{ "nombre":"Daniel1" , "hora_inicio":"08:00", "hora_termino":"09:00" },' +
  '{ "nombre":"Juan" , "hora_inicio":"09:30", "hora_termino":"11:00" },' +
  '{ "nombre":"Gabriel" , "hora_inicio":"15:00", "hora_termino":"16:00" },' +
  '{ "nombre":"Esteban" , "hora_inicio":"17:00", "hora_termino":"19:30" } ],' +
  '  "miercoles" : [' +
  '{ "nombre":"Pepito" , "hora_inicio":"13:00", "hora_termino":"13:30" } ],' +
  '  "jueves" : [' +
  '{ "nombre":"Enrique" , "hora_inicio":"08:00", "hora_termino":"09:00" },' +
  '{ "nombre":"Sebastian" , "hora_inicio":"09:30", "hora_termino":"10:00" },' +
  '{ "nombre":"Alfonzo" , "hora_inicio":"15:00", "hora_termino":"16:00" },' +
  '{ "nombre":"Carolina" , "hora_inicio":"17:00", "hora_termino":"17:30" } ],' +
  '  "viernes" : [' +
  '{ "nombre":"Andres" , "hora_inicio":"16:00", "hora_termino":"16:30" },' +
  '{ "nombre":"Ingrid" , "hora_inicio":"18:00", "hora_termino":"18:30" } ]' +
  "}";
var obj = JSON.parse(citas);

// console.log(obj);

document.getElementById("containerData").innerHTML = Agenda(obj);
