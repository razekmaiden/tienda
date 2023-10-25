from werkzeug.security import check_password_hash

from .entities.Usuario import Usuario

class ModeloUsuario:
    
    @classmethod
    def login(self, db, usuario):
        try:
            db.connect()
            sql = f"""SELECT id, usuario, password FROM usuario WHERE usuario = '{usuario.usuario}'"""
            cursor = db.execute_sql(sql)
            data = cursor.fetchone()
            #print(data)
            coincide = check_password_hash(data[2], usuario.password)
            if coincide:
                usuario_logueado = Usuario(data[0], data[1], None, None)
                return usuario_logueado
            else:
                None
        except Exception as ex:
            raise Exception(ex)