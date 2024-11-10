import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.modulos_model import Modulo
from fastapi.encoders import jsonable_encoder

class ModulosController:
    
    def create_modulo(self, modulo: Modulo):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO modulos (nombre, descripcion) VALUES (%s, %s)", (modulo.nombre, modulo.descripcion))
            conn.commit()
            conn.close()
            return {"resultado": "Módulo creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_modulo(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM modulos WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:                 
                content = {
                    'id': result[0],
                    'nombre': result[1],
                    'descripcion': result[2],
                    'estado': result[3],
                    'fecha_registro': result[4],
                    'fecha_modificacion': result[5]
                }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Módulo no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_modulos(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM modulos")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'nombre': data[1],
                    'descripcion': data[2],
                    'estado': data[3],
                    'fecha_registro': data[4],
                    'fecha_modificacion': data[5]
                }
                payload.append(content)
            json_data = jsonable_encoder(payload)
            return {"resultado": json_data}
        except mysql.connector.Error as err:
            if conn:
                conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()          
            
    def update_modulo(self, id: int, modulo: Modulo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE modulos SET nombre = %s, descripcion = %s WHERE id = %s",
                           (modulo.nombre, modulo.descripcion, id))
            conn.commit()
            conn.close()
            return {"resultado": "Módulo actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def disable_modulo(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE modulos SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Módulo deshabilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()       
            
    def enable_modulo(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE modulos SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Módulo habilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()      
            