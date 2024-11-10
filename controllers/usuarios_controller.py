import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.usuarios_model import Usuario
from fastapi.encoders import jsonable_encoder

class UsuariosController:
    
    def create_usuario(self, usuario: Usuario):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (rol_id, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, genero_id, tipo_documento_id, numero_documento, correo, contrasena, telefono, google) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (usuario.rol_id, usuario.primer_nombre, usuario.segundo_nombre, usuario.primer_apellido, usuario.segundo_apellido, usuario.fecha_nacimiento, usuario.genero_id, usuario.tipo_documento_id, usuario.numero_documento, usuario.correo, usuario.contrasena, usuario.telefono, usuario.google))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))      
        finally:
            conn.close()
            
    def get_usuario(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
            result = cursor.fetchone()
            if result:                 
                content = {
                    'id': result[0],
                    'rol_id': result[1],
                    'primer_nombre': result[2],
                    'segundo_nombre': result[3],
                    'primer_apellido': result[4],
                    'segundo_apellido': result[5],
                    'fecha_nacimiento': result[6],
                    'genero_id': result[7],
                    'tipo_documento_id': result[8],
                    'numero_documento': result[9],
                    'correo': result[10],
                    'contrasena': result[11],
                    'telefono': result[12],
                    'google': result[13],
                    'estado': result[14],
                    'fecha_creacion': result[15],
                    'fecha_modificacion': result[16]
                }
                json_data = jsonable_encoder(content)
                return json_data
            else:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def get_usuarios(self): 
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id': data[0],
                    'rol_id': data[1],
                    'primer_nombre': data[2],
                    'segundo_nombre': data[3],
                    'primer_apellido': data[4],
                    'segundo_apellido': data[5],
                    'fecha_nacimiento': data[6],
                    'genero_id': data[7],
                    'tipo_documento_id': data[8],
                    'numero_documento': data[9],
                    'correo': data[10],
                    'contrasena': data[11],
                    'telefono': data[12],
                    'google': data[13],
                    'estado': data[14],
                    'fecha_creacion': data[15],
                    'fecha_modificacion': data[16]
                }
                payload.append(content)
            json_data = jsonable_encoder(payload)
            return json_data
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def update_usuario(self, id: int, usuario: Usuario):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET rol_id = %s, primer_nombre = %s, segundo_nombre = %s, primer_apellido = %s, segundo_apellido = %s, fecha_nacimiento = %s, genero_id = %s, tipo_documento_id = %s, numero_documento = %s, correo = %s, contrasena = %s, telefono = %s, google = %s WHERE id = %s", (usuario.rol_id, usuario.primer_nombre, usuario.segundo_nombre, usuario.primer_apellido, usuario.segundo_apellido, usuario.fecha_nacimiento, usuario.genero_id, usuario.tipo_documento_id, usuario.numero_documento, usuario.correo, usuario.contrasena, usuario.telefono, usuario.google, id))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario actualizado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
    
    def disable_usuario(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET estado = 0 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario deshabilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
            
    def enable_usuario(self, id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET estado = 1 WHERE id = %s", (id,))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario habilitado"}
        except mysql.connector.Error as err:
            conn.rollback()
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            conn.close()
                   
