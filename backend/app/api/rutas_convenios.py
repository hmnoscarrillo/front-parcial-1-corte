from fastapi import APIRouter, HTTPException
from app.models.convenio import Convenio
from app.repositories.convenio_repo import ConvenioRepository

router = APIRouter(prefix="/convenios", tags=["Convenio"])

repo = ConvenioRepository()


@router.get("/")
def listar_convenios():
    return repo.obtener_todos()


@router.get("/{convenio_id}")
def obtener_convenio(convenio_id: int):
    registro = repo.obtener_por_id(convenio_id)

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return registro


@router.get("/empresa/{empresa_id}")
def obtener_convenios_por_empresa(empresa_id: int):
    return repo.obtener_por_empresa(empresa_id)


@router.post("/", status_code=201)
def crear_convenio(convenio: Convenio):
    nuevo_id = repo.crear(convenio)

    return {"mensaje": "Registro creado exitosamente", "id": nuevo_id}


@router.put("/{convenio_id}")
def actualizar_convenio(convenio_id: int, convenio: Convenio):
    exito = repo.actualizar(convenio_id, convenio)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro actualizado correctamente"}


@router.delete("/{convenio_id}")
def eliminar_convenio(convenio_id: int):
    exito = repo.eliminar(convenio_id)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro eliminado correctamente"}
