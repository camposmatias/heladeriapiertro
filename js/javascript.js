// =========== // do... While // ======= //

// =========== // do... While // ======= //

function florNacional() {
  let rtacorrecta = 3; // Respuesta correcta
  let opcion; // Declaración única de la variable

  do {
    alert("Ingrese el N° que corresponde a la flor nacional de Argentina?:\n1. Jazmín\n2. Rosa\n3. Ceibo\n4. Margarita");
    opcion = parseInt(prompt("Ingresa tu respuesta: "));

    if (opcion === rtacorrecta) {
      console.log("¡Respuesta Correcta!");
      console.log("FELICITACIONES\nEl Ceibo es la flor nacional de Argentina");
      break; // Salir del bucle si la respuesta es correcta
    } else {
      console.log("* ¡Respuesta incorrecta! *");
      alert("Respuesta incorrecta, intenta nuevamente.");
    }
  } while (true); // El bucle termina con `break`
}

florNacional();


 /*

| Explicación | 

Este es un ejemplo la función sumar(), al ser invicada, solicita al usuario dos números mediante un prompt() que convierte a enteros con parseInt(), luego se crea la variable resultado para sumarlos y se muestra el resultado con un alert() concatenado  la variable con el resultado que almacenó la suma. 
*/
/*
// funciones

// var edad = 8

function saludar() {
  console.log("Hola Mundo!")
  let edad = 8
  return edad
}

valorRetornado = saludar()

console.log(valorRetornado)

*/