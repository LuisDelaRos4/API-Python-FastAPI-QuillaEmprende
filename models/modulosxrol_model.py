from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ModuloxRol(BaseModel):
    id: Optional[int] = None
    modulo_id: int
    rol_id: int
    estado: Optional[bool] = None 
    fecha_registro: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None