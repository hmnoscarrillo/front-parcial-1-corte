from datetime import date
from pydantic import BaseModel
from typing import Optional


class Convenio(BaseModel):
    convenio_id: Optional[int] = None
    codigo: str
    empresa_id: int
    programa_id: int
    fecha_inicio: date
    fecha_fin: date
    estado: Optional[str] = "Vigente"
