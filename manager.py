from app import inicializar_app  # Arquitectura Singleton
from config import config


#configuracion = config['development']
app = inicializar_app(config['development'])

if __name__=='__main__':
    app.run()