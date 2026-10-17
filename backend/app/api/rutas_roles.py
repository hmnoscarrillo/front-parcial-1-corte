from fastapi import APIRouter, HTTPException
from app.repositories.rol_repo import RolRepository

router = APIRouter(prefix="/roles", tags=["Roles"])
repo = RolRepository()


@router.get("/")
def listar_roles():
    return repo.obtener_todos()


@router.get("/{rol_id}")
def obtener_rol(rol_id: int):
    registro = repo.obtener_por_id(rol_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return registro


@router.get("/{rol_id}/modulos")
def obtener_modulos_del_rol(rol_id: int):
    modulos = repo.obtener_modulos_por_rol(rol_id)
    return modulos
