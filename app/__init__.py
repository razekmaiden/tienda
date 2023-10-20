from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404 # El segundo es el codigo de error

def inicializar_app(config): # Aca se ingresa como argumento la configuracion definida en config.py
    app.config.from_object(config)
    app.register_error_handler(404, pagina_no_encontrada) # El manejador de errores permite redirigir a la vista correcta cuando hay un error 404 en este caso. 
    return app
