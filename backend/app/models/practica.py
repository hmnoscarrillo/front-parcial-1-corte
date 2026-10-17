from datetime import date
from pydantic import BaseModel
from typing import Optional


class Practica(BaseModel):
    practica_id: Optional[int] = None
    estudiante_id: int
    empresa_id: int
    programa_id: int
    convenio_id: int
    tutor_academico_id: int
    tutor_empresarial_id: int
    cargo: str
    fecha_inicio: date
    fecha_fin: date
    modalidad: str
    estado: Optional[str] = "En proceso"
