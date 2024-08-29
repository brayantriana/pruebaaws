# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>
from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta básica
@app.route('/')
def home():
    return "¡Hola, Mundo! Esta es una prueba de Flask."

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
