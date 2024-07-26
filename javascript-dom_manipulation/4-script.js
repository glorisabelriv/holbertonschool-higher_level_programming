// Selecciona el elemento con id 'add_item'
const addItem = document.querySelector('#add_item');

// Selecciona el elemento ul con la clase 'my_list'
const myList = document.querySelector('.my_list');

// Agrega un manejador de eventos de clic al elemento con id 'add_item'
addItem.addEventListener('click', function() {
  // Crea un nuevo elemento li
  const newItem = document.createElement('li');
  // Establece el contenido del nuevo li
  newItem.textContent = 'Item';
  // Agrega el nuevo li a la lista ul
  myList.appendChild(newItem);
});
