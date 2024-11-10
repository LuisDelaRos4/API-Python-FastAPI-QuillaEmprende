from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class Venta(BaseModel):
    id: Optional[int] = None
    vendedor_id: int    
    comprador_id: int   
    producto_servicio_id: int
    abono: Decimal
    saldo: Decimal
    estado: Optional[bool] = None 
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None