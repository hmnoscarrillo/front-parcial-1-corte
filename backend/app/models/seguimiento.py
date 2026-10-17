from datetime import date
from pydantic import BaseModel
from typing import Optional


class Seguimiento(BaseModel):
    seguimiento_id: Optional[int] = None
    practica_id: int
    tutor_academico_id: int
    fecha_seguimiento: date
    tipo: str
    observaciones: str
    estado: str
