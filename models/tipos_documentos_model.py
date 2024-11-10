from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Tipo_Documento(BaseModel):
    id: Optional[int] = None
    nombre: str
    estado: Optional[bool] = None 
    fecha_registro: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None