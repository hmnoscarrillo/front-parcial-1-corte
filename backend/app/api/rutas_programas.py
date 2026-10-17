from fastapi import APIRouter, HTTPException
from app.models.programa import Programa
from app.repositories.programa_repo import ProgramaRepository

router = APIRouter(prefix="/programas", tags=["Programa"])

repo = ProgramaRepository()


@router.get("/")
def listar_programas():
    return repo.obtener_todos()


@router.get("/{programa_id}")
def obtener_programa(programa_id: int):
    registro = repo.obtener_por_id(programa_id)

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return registro


@router.post("/", status_code=201)
def crear_programa(programa: Programa):
    nuevo_id = repo.crear(programa)

    return {"mensaje": "Registro creado exitosamente", "id": nuevo_id}


@router.put("/{programa_id}")
def actualizar_programa(programa_id: int, programa: Programa):
    exito = repo.actualizar(programa_id, programa)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro actualizado correctamente"}


@router.delete("/{programa_id}")
def eliminar_programa(programa_id: int):
    exito = repo.eliminar(programa_id)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro eliminado correctamente"}
