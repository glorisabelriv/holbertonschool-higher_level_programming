// URL de la API
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Selecciona el elemento con id 'list_movies'
const listMoviesElement = document.querySelector('#list_movies');

// Usa Fetch API para obtener datos de la API
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    // Itera sobre los resultados y agrega cada título de película a la lista
    data.results.forEach(film => {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      listMoviesElement.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });
