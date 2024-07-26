document.addEventListener('DOMContentLoaded', function() {
    // URL de la API
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
    // Selecciona el elemento con id 'hello'
    const helloElement = document.querySelector('#hello');
  
    // Usa Fetch API para obtener datos de la API
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        // Actualiza el contenido del elemento 'hello' con la traducción
        helloElement.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error:', error);
      });
  });
