from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def html_inicio():
    return """
        <style>
        h1{
            color: red;
        }
        </style>

        <h1>Hola Mundo</h1>
        <p>Esto es un parrafo</p>
    
    """


@app.route('/con_template')
def html_inicio_render():
    return render_template("saludos/hola.html")
    

@app.route('/usuario/<name>')
def usuario_render(name):

    return render_template("saludos/usuario.html", nombre=name)



@app.route('/servicios')
def sitioweb_servicios():

    lista_servicios = [
        { 
            'titulo': 'Limpieza', 
            'descripcion':'Esto es la descripción de limpieza',
            'imagen': 'limpieza.jpg',
        },
        { 
            'titulo': 'Mantencion', 
            'descripcion':'Esto es la descripción de mantencion',
            'imagen': 'mantencion.jpg',
        },
        { 
            'titulo': 'Soporte', 
            'descripcion':'Esto es la descripción de soporte',
            'imagen': 'soporte.webp',
        },
    ]


    return render_template("sitioweb/servicios.html", servicios=lista_servicios)

@app.route('/quienes')
def sitioweb_quienes():
    return render_template("sitioweb/quienes.html")

@app.route('/contacto')
def sitioweb_contacto():
    return render_template("sitioweb/contacto.html")

@app.route('/historia')
def sitioweb_historia():
    return render_template("sitioweb/historia.html")

@app.route('/mision')
def sitioweb_mision():

    usuario = {'nombre': 'Francisco','edad': 37,}

    return render_template("sitioweb/mision.html", user=usuario)    


if __name__=="__main__":
    app.run(debug=True)