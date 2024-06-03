from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos en memoria para usuarios
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


# Ruta raíz
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Ruta para obtener datos en formato JSON
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


# Ruta para verificar el estado del API
@app.route('/status')
def get_status():
    return "OK"


# Ruta para obtener datos de un usuario específico
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# Ruta para agregar un nuevo usuario
@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.get_json()
    username = new_user.get('username')
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user})


if __name__ == "__main__":
    app.run()
