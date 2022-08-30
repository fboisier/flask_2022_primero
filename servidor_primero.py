from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"


@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    print("HOLA")
    return 'Hola Mundo2!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/pancho')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def pancho():
    return 'FRANCISCO'  # Devuelve la cadena '¡Hola Mundo!' como respuesta


@app.route('/success')
def success():
    return "success"


@app.route('/hola/<name>') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def hola(name):
    print(name)
    return "Hola, " + name

@app.route('/m/<track>/<unidad>/<ejercicio>') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def module_coding_dojo(track,unidad, ejercicio ):
    print(track,unidad, ejercicio )
    return f"{track} - {unidad}- {ejercicio}"


@app.route('/usuario/<id>/editar') # para una ruta '/hola /____' cualquier cosa después de que '/hola/' se pase como una variable 'name'
def usuario_editar(id):
    print(id)
    return f"{id}"


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración