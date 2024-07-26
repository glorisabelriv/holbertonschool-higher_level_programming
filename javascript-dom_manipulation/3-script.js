// Selecciona el elemento con id 'toggle_header'
const toggleHeader = document.querySelector('#toggle_header');

// Selecciona el elemento header
const header = document.querySelector('header');

// Agrega un manejador de eventos de clic al elemento con id 'toggle_header'
toggleHeader.addEventListener('click', function() {
  // Alterna la clase del header entre 'red' y 'green'
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
