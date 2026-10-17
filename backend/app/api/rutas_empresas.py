from fastapi import APIRouter, HTTPException
from app.models.empresa import Empresa
from app.repositories.empresa_repo import EmpresaRepository

router = APIRouter(prefix="/empresas", tags=["Empresa"])

repo = EmpresaRepository()


@router.get("/")
def listar_empresas():
    return repo.obtener_todos()


@router.get("/{empresa_id}")
def obtener_empresa(empresa_id: int):
    registro = repo.obtener_por_id(empresa_id)

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return registro


@router.post("/", status_code=201)
def crear_empresa(empresa: Empresa):
    nuevo_id = repo.crear(empresa)

    return {"mensaje": "Registro creado exitosamente", "id": nuevo_id}


@router.put("/{empresa_id}")
def actualizar_empresa(empresa_id: int, empresa: Empresa):
    exito = repo.actualizar(empresa_id, empresa)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro actualizado correctamente"}


@router.delete("/{empresa_id}")
def eliminar_empresa(empresa_id: int):
    exito = repo.eliminar(empresa_id)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro eliminado correctamente"}
