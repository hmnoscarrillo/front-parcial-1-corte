from pydantic import BaseModel
from typing import Optional


class Programa(BaseModel):
    programa_id: Optional[int] = None
    nombre: str
    facultad: str
    nivel: str
    duracion_semestres: int
    estado: Optional[str] = "Activo"
