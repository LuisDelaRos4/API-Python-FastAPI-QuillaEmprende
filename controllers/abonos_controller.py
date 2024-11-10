import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.abonos_model import Abono
from fastapi.encoders import jsonable_encoder

class AbonosController:
    
    def create_abono(self, abono: Abono):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO abonos (venta_id, valor) VALUES (%s, %s)", (abono.venta_id, abono.valor))
            conn.commit()
            conn.close()
            return {"resultado": "Abono creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_abono(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM abonos WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:                 
                content = {
                    'id': result[0],
                    'venta_id': result[1],
                    'valor': result[2],
                    'estado': result[3],
                    'fecha_creacion': result[4],
                    'fecha_modificacion': result[5]
                }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Abono no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_abonos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM abonos")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'venta_id': data[1],
                    'valor': data[2],
                    'estado': data[3],
                    'fecha_creacion': data[4],
                    'fecha_modificacion': data[5]
                }
                payload.append(content)
            json_data = jsonable_encoder(payload)
            return json_data
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def update_abono(self, id: int, abono: Abono):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE abonos SET venta_id = %s, valor = %s WHERE id = %s", (abono.venta_id, abono.valor, id))
            conn.commit()
            conn.close()
            return {"resultado": "Abono actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def disable_abono(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE abonos SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Abono deshabilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()        
            
    def enable_abono(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE abonos SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Abono habilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
            
