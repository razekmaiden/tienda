from .entities.Usuario import Usuario
from .entities.TipoUsuario import TipoUsuario

class ModeloUsuario:
    
    @classmethod
    def login(self, db, usuario):
        try:
            db.connect()
            sql = f"""SELECT id, usuario, password FROM usuario WHERE usuario = '{usuario.usuario}'"""
            cursor = db.execute_sql(sql)
            data = cursor.fetchone()
            if data != None:
                coincide = Usuario.verificar_password(data[2], usuario.password)
                if coincide:
                    usuario_logueado = Usuario(data[0], data[1], None, None)
                    return usuario_logueado
                else:
                    return None
            return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def obtener_por_id(self, db, user_id):
        try:
            db.connect()
            sql = f"""SELECT USU.id, USU.usuario, TIP.id, TIP.nombre
                    FROM usuario USU JOIN tipousuario TIP ON USU.tipousuario_id = TIP.id
                    WHERE USU.id = {user_id}"""
            cursor = db.execute_sql(sql)
            data = cursor.fetchone()
            tipousuario = TipoUsuario(data[2], data[3]) # retorno los datos de tipo de usuario a un objeto de la clase TipoUsuario
            usuario_logueado = Usuario(data[0], data[1], None, tipousuario)
            return usuario_logueado
        except Exception as ex:
            raise Exception(ex)