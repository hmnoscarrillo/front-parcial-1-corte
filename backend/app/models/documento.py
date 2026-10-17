from datetime import date
from pydantic import BaseModel
from typing import Optional


class Documento(BaseModel):
    documento_id: Optional[int] = None
    practica_id: int
    nombre_documento: str
    tipo_documento: str
    fecha_subida: date
    ruta_archivo: Optional[str] = None
    estado: Optional[str] = "Pendiente"
