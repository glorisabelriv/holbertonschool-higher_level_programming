import requests
import csv

def fetch_and_print_posts():
    # Hacer la solicitud GET a JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Imprimir el código de estado de la respuesta
    print(f"Status Code: {response.status_code}")

    # Si la solicitud fue exitosa, analizar y mostrar los datos
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    # Hacer la solicitud GET a JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Si la solicitud fue exitosa, analizar y guardar los datos
    if response.status_code == 200:
        posts = response.json()
        data_to_save = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Guardar los datos en un archivo CSV
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data_to_save)
