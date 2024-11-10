from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Rol(BaseModel):
    id: Optional[int] = None
    nombre: str
    descripcion	: Optional[str] = None
    estado: Optional[bool] = None 
    fecha_registro: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None