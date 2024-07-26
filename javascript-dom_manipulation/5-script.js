// Selecciona el elemento con id 'update_header'
const updateHeader = document.querySelector('#update_header');

// Selecciona el elemento header
const header = document.querySelector('header');

// Agrega un manejador de eventos de clic al elemento con id 'update_header'
updateHeader.addEventListener('click', function() {
  // Actualiza el texto del header
  header.textContent = 'New Header!!!';
});
