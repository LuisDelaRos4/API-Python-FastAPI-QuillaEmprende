import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tipos_prod_serv_model import Tipo_Prod_Serv
from fastapi.encoders import jsonable_encoder

class TiposProdServController:
    
    def create_tipo_prod_serv(self, tipo_prod_serv: Tipo_Prod_Serv):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tipos_prod_serv (nombre) VALUES (%s)", (tipo_prod_serv.nombre,))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo de producto/servicio creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_tipo_prod_serv(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipos_prod_serv WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:                 
                content = {
                    'id': result[0],
                    'nombre': result[1],
                    'estado': result[2],
                    'fecha_creacion': result[3],
                    'fecha_modificacion': result[4]
                }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Tipo de producto/servicio no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_tipos_prod_serv(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipos_prod_serv")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'nombre': data[1],
                    'estado': data[2],
                    'fecha_creacion': data[3],
                    'fecha_modificacion': data[4]
                }
                payload.append(content)
            json_data = jsonable_encoder(payload)
            return json_data
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def update_tipo_prod_serv(self, id: int, tipo_prod_serv: Tipo_Prod_Serv):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tipos_prod_serv SET nombre = %s WHERE id = %s", (tipo_prod_serv.nombre, id))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo de producto/servicio actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def disable_tipo_prod_serv(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tipos_prod_serv SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo de producto/servicio deshabilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def enable_tipo_prod_serv(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tipos_prod_serv SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo de producto/servicio habilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close
            
            