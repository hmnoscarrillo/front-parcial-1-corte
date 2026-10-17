from pydantic import BaseModel
from typing import Optional


class Rol(BaseModel):
    rol_id: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None
    nivel_jerarquia: Optional[int] = 1
    estado: Optional[str] = "Activo"
