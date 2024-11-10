from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Categoria_Prod_Serv(BaseModel):
    id: Optional[int] = None
    usuario_id: int
    tipo_id: int
    nombre: str
    descripcion	: Optional[str] = None
    estado: Optional[bool] = None 
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None