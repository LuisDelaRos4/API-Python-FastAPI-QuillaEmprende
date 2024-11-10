from fastapi import APIRouter
from controllers.tipos_documentos_controller import TiposDocumentosController
from models.tipos_documentos_model import Tipo_Documento

router = APIRouter()

tipo_documento_controller = TiposDocumentosController()

@router.post("/create_tipo_documento")
async def create_tipo_documento(tipo_documento: Tipo_Documento):
    rpta = tipo_documento_controller.create_tipo_documento(tipo_documento)
    return rpta

@router.get("/get_tipo_documento/{id}", response_model=Tipo_Documento)
async def get_tipo_documento(id: int):
    rpta = tipo_documento_controller.get_tipo_documento(id)
    return rpta

@router.get("/get_tipos_documentos/")
async def get_tipos_documentos():
    rpta = tipo_documento_controller.get_tipos_documentos()
    return rpta

@router.put("/update_tipo_documento/{id}")
async def update_tipo_documento(id: int, tipo_documento: Tipo_Documento):
    rpta = tipo_documento_controller.update_tipo_documento(id, tipo_documento)
    return rpta

@router.put("/disable_tipo_documento/{id}")
async def disable_tipo_documento(id: int):
    rpta = tipo_documento_controller.disable_tipo_documento(id)
    return rpta

@router.put("/enable_tipo_documento/{id}")
async def enable_tipo_documento(id: int):
    rpta = tipo_documento_controller.enable_tipo_documento(id)
    return rpta
