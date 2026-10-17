from fastapi import APIRouter, HTTPException
from app.models.estudiante import Estudiante
from app.repositories.estudiante_repo import EstudianteRepository

router = APIRouter(prefix="/estudiantes", tags=["Estudiante"])

repo = EstudianteRepository()


@router.get("/")
def listar_estudiantes():
    return repo.obtener_todos()


@router.get("/{estudiante_id}")
def obtener_estudiante(estudiante_id: int):
    registro = repo.obtener_por_id(estudiante_id)

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return registro


@router.get("/programa/{programa_id}")
def obtener_estudiantes_por_programa(programa_id: int):
    return repo.obtener_por_programa(programa_id)


@router.post("/", status_code=201)
def crear_estudiante(estudiante: Estudiante):
    nuevo_id = repo.crear(estudiante)

    return {"mensaje": "Registro creado exitosamente", "id": nuevo_id}


@router.put("/{estudiante_id}")
def actualizar_estudiante(estudiante_id: int, estudiante: Estudiante):
    exito = repo.actualizar(estudiante_id, estudiante)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro actualizado correctamente"}


@router.delete("/{estudiante_id}")
def eliminar_estudiante(estudiante_id: int):
    exito = repo.eliminar(estudiante_id)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro eliminado correctamente"}
