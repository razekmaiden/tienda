from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST']) # Aca se indican los metodos permitidos, por defecto solo es GET
def login():
    # print(request.method)
    # print(request.form['usuario'])
    # print(request.form['password'])
    # NOTE: COn el metodos POST los datos del formaulario van en la URL, lo que no es seguro
    if request.method == 'POST': # Si el metodo es post, entonces los datoss estan presentes y los puedo imprimir
        print(request.form['usuario'])
        print(request.form['password'])
        return render_template('index.html')
    else:
        return render_template('auth/login.html')

def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404 # El segundo es el codigo de error

def inicializar_app(config): # Aca se ingresa como argumento la configuracion definida en config.py
    app.config.from_object(config)
    app.register_error_handler(404, pagina_no_encontrada) # El manejador de errores permite redirigir a la vista correcta cuando hay un error 404 en este caso. 
    return app
