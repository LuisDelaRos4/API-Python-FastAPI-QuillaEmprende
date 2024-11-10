from datetime import datetime
from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class Producto_Servicio(BaseModel):
    id: Optional[int] = None
    usuario_id: int
    nombre: str
    descripcion	: Optional[str] = None
    cantidad: int
    precio: Decimal
    categoria_id: int
    tipo_id: int
    estado: Optional[bool] = None 
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None