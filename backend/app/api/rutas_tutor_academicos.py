from fastapi import APIRouter, HTTPException
from app.models.tutor_academico import TutorAcademico
from app.repositories.tutor_academico_repo import TutorAcademicoRepository

router = APIRouter(prefix="/tutores-academicos", tags=["Tutor Académico"])
router_compat = APIRouter(prefix="/tutores_academicos", tags=["Tutor Académico"])

repo = TutorAcademicoRepository()


def listar_tutores_academicos():
    return repo.obtener_todos()


def obtener_tutor_academico(tutor_academico_id: int):
    registro = repo.obtener_por_id(tutor_academico_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro


def obtener_tutores_por_programa(programa_id: int):
    return repo.obtener_por_programa(programa_id)


def crear_tutor_academico(tutor: TutorAcademico):
    nuevo_id = repo.crear(tutor)
    return {"mensaje": "Registro creado exitosamente", "id": nuevo_id}


def actualizar_tutor_academico(tutor_academico_id: int, tutor: TutorAcademico):
    exito = repo.actualizar(tutor_academico_id, tutor)
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"mensaje": "Registro actualizado correctamente"}


def eliminar_tutor_academico(tutor_academico_id: int):
    exito = repo.eliminar(tutor_academico_id)
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"mensaje": "Registro eliminado correctamente"}


for r in [router, router_compat]:
    r.add_api_route("/", listar_tutores_academicos, methods=["GET"])
    r.add_api_route("/{tutor_academico_id}", obtener_tutor_academico, methods=["GET"])
    r.add_api_route("/programa/{programa_id}", obtener_tutores_por_programa, methods=["GET"])
    r.add_api_route("/", crear_tutor_academico, methods=["POST"], status_code=201)
    r.add_api_route("/{tutor_academico_id}", actualizar_tutor_academico, methods=["PUT"])
    r.add_api_route("/{tutor_academico_id}", eliminar_tutor_academico, methods=["DELETE"])
