import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.modulosxrol_model import ModuloxRol
from fastapi.encoders import jsonable_encoder

class ModulosxRolController:
    
    def create_moduloxrol(self, moduloxrol: ModuloxRol):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO modulosxrol (modulo_id, rol_id) VALUES (%s, %s)", (moduloxrol.modulo_id, moduloxrol.rol_id))
            conn.commit()
            conn.close()
            return {"resultado": "Módulo por rol creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_moduloxrol(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM modulosxrol WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:                 
                content = {
                    'id': result[0],
                    'modulo_id': result[1],
                    'rol_id': result[2],
                    'estado': result[3],
                    'fecha_registro': result[4],
                    'fecha_modificacion': result[5]
                }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Módulo por rol no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_modulosxroles(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM modulosxrol")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'modulo_id': data[1],
                    'rol_id': data[2],
                    'estado': data[3],
                    'fecha_registro': data[4],
                    'fecha_modificacion': data[5]
                }
                payload.append(content)
            return payload
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def update_moduloxrol(self, id: int, moduloxrol: ModuloxRol):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE modulosxrol SET modulo_id = %s, rol_id = %s WHERE id = %s", (moduloxrol.modulo_id, moduloxrol.rol_id, id))
            conn.commit()
            conn.close()
            return {"resultado": "Módulo por rol actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def disable_moduloxrol(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE modulosxrol SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Módulo por rol deshabilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
            
    def enable_moduloxrol(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE modulosxrol SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Módulo por rol habilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()