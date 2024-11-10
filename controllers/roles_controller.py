import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.roles_model import Rol
from fastapi.encoders import jsonable_encoder

class RolesController:
    def create_rol(self, rol: Rol):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO roles (nombre, descripcion) VALUES (%s, %s)", (rol.nombre, rol.descripcion))
            conn.commit()
            conn.close()
            return {"resultado": "Rol creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_rol(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles WHERE id = %s", (id,))
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
                raise HTTPException(status_code=404, detail="Rol no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_roles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM roles")
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
            return json_data
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def update_rol(self, id: int, rol: Rol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE roles SET nombre = %s, descripcion = %s WHERE id = %s", 
                           (rol.nombre, rol.descripcion, id))
            conn.commit()
            conn.close()
            return {"resultado": "Rol actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def disable_rol(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE roles SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Rol deshabilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def enable_rol(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE roles SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Rol habilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()