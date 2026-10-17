from pydantic import BaseModel
from typing import Optional


class TutorAcademico(BaseModel):
    tutor_academico_id: Optional[int] = None
    documento: str
    nombres: str
    apellidos: str
    correo: str
    telefono: Optional[str] = None
    cargo: str
    programa_id: int
