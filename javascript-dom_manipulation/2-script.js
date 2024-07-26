// Selecciona el elemento con id 'red_header'
const redHeader = document.querySelector('#red_header');

// Selecciona el elemento header
const header = document.querySelector('header');

// Agrega un manejador de eventos de clic al elemento con id 'red_header'
redHeader.addEventListener('click', function() {
  // Agrega la clase 'red' al header
  header.classList.add('red');
});
