import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.productos_servicios_model import Producto_Servicio
from fastapi.encoders import jsonable_encoder

class ProductoServicioController:
    
    def create_producto_servicio(self, producto_servicio: Producto_Servicio):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO productos_servicios (usuario_id, nombre, descripcion, cantidad, precio, categoria_id, tipo_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", (producto_servicio.usuario_id, producto_servicio.nombre, producto_servicio.descripcion, producto_servicio.cantidad, producto_servicio.precio, producto_servicio.categoria_id, producto_servicio.tipo_id))
            conn.commit()
            conn.close()
            return {"resultado": "Producto o Servicio creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_producto_servicio(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos_servicios WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:                 
                content = {
                    'id': result[0],
                    'usuario_id': result[1],
                    'nombre': result[2],
                    'descripcion': result[3],
                    'cantidad': result[4],
                    'precio': result[5],
                    'categoria_id': result[6],
                    'tipo_id': result[7],
                    'estado': result[8],
                    'fecha_creacion': result[9],
                    'fecha_modificacion': result[10]
                }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Producto o Servicio no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_productos_servicios(self):      
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM productos_servicios")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'usuario_id': data[1],
                    'nombre': data[2],
                    'descripcion': data[3],
                    'cantidad': data[4],
                    'precio': data[5],
                    'categoria_id': data[6],
                    'tipo_id': data[7],
                    'estado': data[8],
                    'fecha_creacion': data[9],
                    'fecha_modificacion': data[10]
                }
                payload.append(content)
            json_data = jsonable_encoder(payload)
            return json_data
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def update_producto_servicio(self, id: int, producto_servicio: Producto_Servicio):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE productos_servicios SET nombre = %s, descripcion = %s, cantidad = %s, precio = %s, categoria_id = %s, tipo_id = %s WHERE id = %s", (producto_servicio.nombre, producto_servicio.descripcion, producto_servicio.cantidad, producto_servicio.precio, producto_servicio.categoria_id, producto_servicio.tipo_id, id))
            conn.commit()
            conn.close()
            return {"resultado": "Producto o Servicio actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def disable_producto_servicio(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE productos_servicios SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Producto o Servicio deshabilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def enable_producto_servicio(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE productos_servicios SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Producto o Servicio habilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    
    