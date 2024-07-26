// URL de la API
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Selecciona el elemento con id 'character'
const characterElement = document.querySelector('#character');

// Usa Fetch API para obtener datos de la API
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    // Actualiza el contenido del elemento 'character' con el nombre del personaje
    characterElement.textContent = data.name;
  })
  .catch(error => {
    console.error('Error:', error);
  });
