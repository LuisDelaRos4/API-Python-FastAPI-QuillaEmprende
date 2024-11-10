from fastapi import APIRouter
from controllers.modulos_controller import ModulosController
from models.modulos_model import Modulo

router = APIRouter()

modulo_controller = ModulosController()

@router.post("/create_modulo")
async def create_modulo(modulo: Modulo):
    rpta = modulo_controller.create_modulo(modulo)
    return rpta

@router.get("/get_modulo/{id}", response_model=Modulo)
async def get_modulo(id: int):
    rpta = modulo_controller.get_modulo(id)
    return rpta

@router.get("/get_modulos/")
async def get_modulos():
    rpta = modulo_controller.get_modulos()
    return rpta

@router.put("/update_modulo/{id}")
async def update_modulo(id: int, modulo: Modulo):
    rpta = modulo_controller.update_modulo(id, modulo)
    return rpta

@router.put("/disable_modulo/{id}")
async def disable_modulo(id: int):
    rpta = modulo_controller.disable_modulo(id)
    return rpta

@router.put("/enable_modulo/{id}")
async def enable_modulo(id: int):
    rpta = modulo_controller.enable_modulo(id)
    return rpta


