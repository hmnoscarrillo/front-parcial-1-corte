from pydantic import BaseModel
from typing import Optional


class TutorEmpresarial(BaseModel):
    tutor_empresarial_id: Optional[int] = None
    documento: str
    nombres: str
    apellidos: str
    correo: str
    telefono: Optional[str] = None
    cargo: str
    empresa_id: int
