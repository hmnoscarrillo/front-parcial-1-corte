from fastapi import APIRouter, HTTPException
from app.models.practica import Practica
from app.repositories.practica_repo import PracticaRepository

router = APIRouter(prefix="/practicas", tags=["Práctica"])

repo = PracticaRepository()


@router.get("/")
def listar_practicas():
    return repo.obtener_todos()


@router.get("/{practica_id}")
def obtener_practica(practica_id: int):
    registro = repo.obtener_por_id(practica_id)

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return registro


@router.get("/estudiante/{estudiante_id}")
def obtener_practicas_por_estudiante(estudiante_id: int):
    return repo.obtener_por_estudiante(estudiante_id)


@router.post("/", status_code=201)
def crear_practica(practica: Practica):
    nuevo_id = repo.crear(practica)

    return {"mensaje": "Registro creado exitosamente", "id": nuevo_id}


@router.put("/{practica_id}")
def actualizar_practica(practica_id: int, practica: Practica):
    exito = repo.actualizar(practica_id, practica)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro actualizado correctamente"}


@router.delete("/{practica_id}")
def eliminar_practica(practica_id: int):
    exito = repo.eliminar(practica_id)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro eliminado correctamente"}
