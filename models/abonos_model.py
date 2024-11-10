from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class Abono(BaseModel):
    id: Optional[int] = None
    venta_id: int
    valor: Decimal
    estado: Optional[bool] = None 
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None