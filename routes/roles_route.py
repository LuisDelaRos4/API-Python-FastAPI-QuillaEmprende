from fastapi import APIRouter
from controllers.roles_controller import RolesController
from models.roles_model import Rol

router = APIRouter()

rol_controller = RolesController()

@router.post("/create_rol")
async def create_rol(rol: Rol):
    rpta = rol_controller.create_rol(rol)
    return rpta

@router.get("/get_rol/{id}", response_model=Rol)
async def get_rol(id: int):
    rpta = rol_controller.get_rol(id)
    return rpta

@router.get("/get_roles/")
async def get_roles():
    rpta = rol_controller.get_roles()
    return rpta

@router.put("/update_rol/{id}")
async def update_rol(id: int, rol: Rol):
    rpta = rol_controller.update_rol(id, rol)
    return rpta

@router.put("/disable_rol/{id}")
async def disable_rol(id: int):
    rpta = rol_controller.disable_rol(id)
    return rpta

@router.put("/enable_rol/{id}")
async def enable_rol(id: int):
    rpta = rol_controller.enable_rol(id)
    return rpta
