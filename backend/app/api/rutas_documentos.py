from fastapi import APIRouter, HTTPException
from app.models.documento import Documento
from app.repositories.documento_repo import DocumentoRepository

router = APIRouter(prefix="/documentos", tags=["Documento"])

repo = DocumentoRepository()


@router.get("/")
def listar_documentos():
    return repo.obtener_todos()


@router.get("/{documento_id}")
def obtener_documento(documento_id: int):
    registro = repo.obtener_por_id(documento_id)

    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return registro


@router.get("/practica/{practica_id}")
def obtener_documentos_por_practica(practica_id: int):
    return repo.obtener_por_practica(practica_id)


@router.post("/", status_code=201)
def crear_documento(documento: Documento):
    nuevo_id = repo.crear(documento)

    return {"mensaje": "Registro creado exitosamente", "id": nuevo_id}


@router.put("/{documento_id}")
def actualizar_documento(documento_id: int, documento: Documento):
    exito = repo.actualizar(documento_id, documento)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro actualizado correctamente"}


@router.delete("/{documento_id}")
def eliminar_documento(documento_id: int):
    exito = repo.eliminar(documento_id)

    if not exito:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "Registro eliminado correctamente"}
