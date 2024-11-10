import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.generos_model import Genero
from fastapi.encoders import jsonable_encoder

class GenerosController:
    
    def create_genero(self, genero: Genero):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO generos (nombre) VALUES (%s)", (genero.nombre,))
            conn.commit()
            conn.close()
            return {"resultado": "Género creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_genero(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM generos WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:                 
                content = {
                    'id': result[0],
                    'nombre': result[1],
                    'estado': result[2],
                    'fecha_registro': result[3],
                    'fecha_modificacion': result[4]
                }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Género no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_generos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM generos")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'nombre': data[1],
                    'estado': data[2],
                    'fecha_registro': data[3],
                    'fecha_modificacion': data[4]
                }
                payload.append(content)
            json_data = jsonable_encoder(payload)
            return json_data
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def update_genero(self, id: int, genero: Genero):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE generos SET nombre = %s WHERE id = %s", (genero.nombre, id))
            conn.commit()
            conn.close()
            return {"resultado": "Género actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
        
    def disable_genero(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE generos SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Género deshabilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def enable_genero(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE generos SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Género habilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()