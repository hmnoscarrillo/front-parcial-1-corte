from fastapi import APIRouter, HTTPException
from app.models.evaluacion import Evaluacion
from app.repositories.evaluacion_repo import EvaluacionRepository

router = APIRouter(prefix="/evaluaciones", tags=["Evaluación"])

repo = EvaluacionRepository()


@router.get("/")
def listar_evaluaciones():
    return repo.obtener_todos()


@router.get("/{evaluacion_id}")
def obtener_evaluacion(evaluacion_id: int):
    registro = repo.obtener_por_id(evaluacion_id)

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return registro


@router.get("/practica/{practica_id}")
def obtener_evaluaciones_por_practica(practica_id: int):
    return repo.obtener_por_practica(practica_id)


@router.post("/", status_code=201)
def crear_evaluacion(evaluacion: Evaluacion):
    nuevo_id = repo.crear(evaluacion)

    return {"mensaje": "Registro creado exitosamente", "id": nuevo_id}


@router.put("/{evaluacion_id}")
def actualizar_evaluacion(evaluacion_id: int, evaluacion: Evaluacion):
    exito = repo.actualizar(evaluacion_id, evaluacion)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro actualizado correctamente"}


@router.delete("/{evaluacion_id}")
def eliminar_evaluacion(evaluacion_id: int):
    exito = repo.eliminar(evaluacion_id)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro eliminado correctamente"}
