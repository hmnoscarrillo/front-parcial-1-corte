from pydantic import BaseModel
from typing import Optional


class Empresa(BaseModel):
    empresa_id: Optional[int] = None
    nit: str
    nombre: str
    sector: str
    ciudad: str
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[str] = None
    estado: Optional[str] = "Activa"
