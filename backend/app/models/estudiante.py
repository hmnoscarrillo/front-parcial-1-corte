from pydantic import BaseModel
from typing import Optional


class Estudiante(BaseModel):
    estudiante_id: Optional[int] = None
    documento: str
    nombres: str
    apellidos: str
    correo: str
    telefono: Optional[str] = None
    semestre: int
    programa_id: int
    estado: Optional[str] = "Activo"
