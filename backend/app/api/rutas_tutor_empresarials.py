from fastapi import APIRouter, HTTPException
from app.models.tutor_empresarial import TutorEmpresarial
from app.repositories.tutor_empresarial_repo import TutorEmpresarialRepository

router = APIRouter(prefix="/tutores-empresariales", tags=["Tutor Empresarial"])
router_compat = APIRouter(prefix="/tutores_empresariales", tags=["Tutor Empresarial"])

repo = TutorEmpresarialRepository()


def listar_tutores_empresariales():
    return repo.obtener_todos()


def obtener_tutor_empresarial(tutor_empresarial_id: int):
    registro = repo.obtener_por_id(tutor_empresarial_id)
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return registro


def obtener_tutores_por_empresa(empresa_id: int):
    return repo.obtener_por_empresa(empresa_id)


def crear_tutor_empresarial(tutor: TutorEmpresarial):
    nuevo_id = repo.crear(tutor)
    return {"mensaje": "Registro creado exitosamente", "id": nuevo_id}


def actualizar_tutor_empresarial(tutor_empresarial_id: int, tutor: TutorEmpresarial):
    exito = repo.actualizar(tutor_empresarial_id, tutor)
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"mensaje": "Registro actualizado correctamente"}


def eliminar_tutor_empresarial(tutor_empresarial_id: int):
    exito = repo.eliminar(tutor_empresarial_id)
    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return {"mensaje": "Registro eliminado correctamente"}


for r in [router, router_compat]:
    r.add_api_route("/", listar_tutores_empresariales, methods=["GET"])
    r.add_api_route("/{tutor_empresarial_id}", obtener_tutor_empresarial, methods=["GET"])
    r.add_api_route("/empresa/{empresa_id}", obtener_tutores_por_empresa, methods=["GET"])
    r.add_api_route("/", crear_tutor_empresarial, methods=["POST"], status_code=201)
    r.add_api_route("/{tutor_empresarial_id}", actualizar_tutor_empresarial, methods=["PUT"])
    r.add_api_route("/{tutor_empresarial_id}", eliminar_tutor_empresarial, methods=["DELETE"])
