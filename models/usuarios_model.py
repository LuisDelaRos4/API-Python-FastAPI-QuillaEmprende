from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    rol_id: int
    primer_nombre: str
    segundo_nombre	: Optional[str] = None
    primer_apellido: str
    segundo_apellido: Optional[str] = None
    fecha_nacimiento: datetime
    genero_id: int
    tipo_documento_id: int
    numero_documento: str
    correo: EmailStr
    contrasena: str
    telefono: str   
    google: Optional[bool] = None
    estado: Optional[bool] = None 
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None