import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tipos_documentos_model import Tipo_Documento
from fastapi.encoders import jsonable_encoder

class TiposDocumentosController:
    def create_tipo_documento(self, tipo_documento: Tipo_Documento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tipos_documentos (nombre) VALUES (%s)", (tipo_documento.nombre,))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo de documento creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close() 
            
    def get_tipo_documento(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipos_documentos WHERE id = %s", (id,))
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
                raise HTTPException(status_code=404, detail="Tipo de documento no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_tipos_documentos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipos_documentos")
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
            
    def update_tipo_documento(self, id: int, tipo_documento: Tipo_Documento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tipos_documentos SET nombre = %s WHERE id = %s", (tipo_documento.nombre, id))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo de documento actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def disable_tipo_documento(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tipos_documentos SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo de documento deshabilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def enable_tipo_documento(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tipos_documentos SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo de documento habilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
    