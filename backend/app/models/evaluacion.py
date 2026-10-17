from datetime import date
from pydantic import BaseModel
from typing import Optional


class Evaluacion(BaseModel):
    evaluacion_id: Optional[int] = None
    practica_id: int
    fecha_evaluacion: date
    evaluador: str
    nota_academica: float
    nota_empresarial: float
    nota_final: float
    comentarios: Optional[str] = None
