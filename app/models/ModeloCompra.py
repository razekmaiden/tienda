
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