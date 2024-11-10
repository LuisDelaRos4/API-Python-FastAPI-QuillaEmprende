import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.categorias_prod_serv_model import Categoria_Prod_Serv
from fastapi.encoders import jsonable_encoder

class Categorias_Prod_ServController:
    
    def create_categoria_prod_serv(self, categoria_prod_serv: Categoria_Prod_Serv):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO categorias_prod_serv (usuario_id, tipo_id, nombre, descripcion) VALUES (%s, %s, %s, %s)", (categoria_prod_serv.usuario_id, categoria_prod_serv.tipo_id, categoria_prod_serv.nombre, categoria_prod_serv.descripcion))
            conn.commit()
            conn.close()
            return {"resultado": "Categoría de producto y servicio creada"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_categoria_prod_serv(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM categorias_prod_serv WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:                 
                content = {
                    'id': result[0],
                    'usuario_id': result[1],
                    'tipo_id': result[2],
                    'nombre': result[3],
                    'descripcion': result[4],
                    'estado': result[5],
                    'fecha_creacion': result[6],
                    'fecha_modificacion': result[7]
                }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Categoría de producto y servicio no encontrada")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_categorias_prod_serv(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM categorias_prod_serv")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'usuario_id': data[1],
                    'tipo_id': data[2],
                    'nombre': data[3],
                    'descripcion': data[4],
                    'estado': data[5],
                    'fecha_creacion': data[6],
                    'fecha_modificacion': data[7]
                }
                payload.append(content)
            json_data = jsonable_encoder(payload)
            return json_data
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def update_categoria_prod_serv(self, id: int, categoria_prod_serv: Categoria_Prod_Serv):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE categorias_prod_serv SET usuario_id = %s, tipo_id = %s, nombre = %s, descripcion = %s WHERE id = %s", (categoria_prod_serv.usuario_id, categoria_prod_serv.tipo_id, categoria_prod_serv.nombre, categoria_prod_serv.descripcion, id))
            conn.commit()
            conn.close()
            return {"resultado": "Categoría de producto y servicio actualizada"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def disable_categoria_prod_serv(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE categorias_prod_serv SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Categoría de producto y servicio deshabilitada"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def enable_categoria_prod_serv(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE categorias_prod_serv SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Categoría de producto y servicio habilitada"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
            