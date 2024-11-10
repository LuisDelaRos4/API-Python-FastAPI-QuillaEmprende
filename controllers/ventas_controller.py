import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.ventas_model import Venta
from fastapi.encoders import jsonable_encoder

class VentasController:
    
    def create_venta(self, venta: Venta):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ventas (vendedor_id, comprador_id, producto_servicio_id, abono, saldo) VALUES (%s, %s, %s, %s, %s)", (venta.vendedor_id, venta.comprador_id, venta.producto_servicio_id, venta.abono, venta.saldo))
            conn.commit()
            conn.close()
            return {"resultado": "Venta creada"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_venta(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ventas WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:                 
                content = {
                    'id': result[0],
                    'vendedor_id': result[1],
                    'comprador_id': result[2],
                    'producto_servicio_id': result[3],
                    'abono': result[4],
                    'saldo': result[5],
                    'estado': result[6],
                    'fecha_creacion': result[7],
                    'fecha_modificacion': result[8]
                }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Venta no encontrada")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_ventas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ventas")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'vendedor_id': data[1],
                    'comprador_id': data[2],
                    'producto_servicio_id': data[3],
                    'abono': data[4],
                    'saldo': data[5],
                    'estado': data[6],
                    'fecha_creacion': data[7],
                    'fecha_modificacion': data[8]
                }
                payload.append(content)
            json_data = jsonable_encoder(payload)
            return json_data
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def update_venta(self, id: int, venta: Venta):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE ventas SET vendedor_id = %s, comprador_id = %s, producto_servicio_id = %s, abono = %s, saldo = %s WHERE id = %s", (venta.vendedor_id, venta.comprador_id, venta.producto_servicio_id, venta.abono, venta.saldo, id))
            conn.commit()
            conn.close()
            return {"resultado": "Venta actualizada"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def disable_venta(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE ventas SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Venta deshabilitada"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def enable_venta(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE ventas SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Venta habilitada"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()