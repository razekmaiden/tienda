from .entities.Libro import Libro
from .entities.Compra import Compra

class ModeloCompra():

    @classmethod
    def registrar_compra(self, db, compra):
        try:
            
            db.connect()
            sql = f"""INSERT INTO compra (uuid, libro_isbn, usuario_id)
                        VALUES (uuid(), '{compra.libro.isbn}', {compra.usuario.id})"""
            cursor = db.execute_sql(sql)
            db.commit()
            db.close()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def listar_compras_usuario(self, db, usuario):
        try:
            
            db.connect()
            sql = f"""SELECT COM.fecha, LIB.isbn, LIB.titulo, LIB.precio 
                    FROM compra COM JOIN libro LIB ON COM.libro_isbn = LIB.isbn
                    WHERE COM.usuario_id = {usuario.id}
                    """
            cursor = db.execute_sql(sql)
            data = cursor.fetchall()
            db.close()
            compras = []
            for row in data:
                libro = Libro(row[1], row[2], None, None, row[3])
                compra = Compra(None, libro, usuario, row[0])
                compras.append(compra)
            return compras
        except Exception as ex:
            raise Exception(ex)
    