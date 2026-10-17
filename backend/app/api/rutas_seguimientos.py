from fastapi import APIRouter, HTTPException
from app.models.seguimiento import Seguimiento
from app.repositories.seguimiento_repo import SeguimientoRepository

router = APIRouter(prefix="/seguimientos", tags=["Seguimiento"])

repo = SeguimientoRepository()


@router.get("/")
def listar_seguimientos():
    return repo.obtener_todos()


@router.get("/{seguimiento_id}")
def obtener_seguimiento(seguimiento_id: int):
    registro = repo.obtener_por_id(seguimiento_id)

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return registro


@router.get("/practica/{practica_id}")
def obtener_seguimientos_por_practica(practica_id: int):
    return repo.obtener_por_practica(practica_id)


@router.post("/", status_code=201)
def crear_seguimiento(seguimiento: Seguimiento):
    nuevo_id = repo.crear(seguimiento)

    return {"mensaje": "Registro creado exitosamente", "id": nuevo_id}


@router.put("/{seguimiento_id}")
def actualizar_seguimiento(seguimiento_id: int, seguimiento: Seguimiento):
    exito = repo.actualizar(seguimiento_id, seguimiento)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro actualizado correctamente"}


@router.delete("/{seguimiento_id}")
def eliminar_seguimiento(seguimiento_id: int):
    exito = repo.eliminar(seguimiento_id)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro eliminado correctamente"}
