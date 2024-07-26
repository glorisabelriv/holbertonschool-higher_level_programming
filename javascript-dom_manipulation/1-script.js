// Selecciona el elemento con id 'red_header'
const redHeader = document.querySelector('#red_header');

// Selecciona el elemento header
const header = document.querySelector('header');

// Agrega un manejador de eventos de clic al elemento con id 'red_header'
redHeader.addEventListener('click', function() {
  // Cambia el color del texto del header a rojo (#FF0000)
  header.style.color = '#FF0000';
});
