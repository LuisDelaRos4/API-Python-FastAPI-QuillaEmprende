from fastapi import APIRouter
from controllers.modulosxrol_controller import ModulosxRolController
from models.modulosxrol_model import ModuloxRol

router = APIRouter()

moduloxrol_controller = ModulosxRolController()

@router.post("/create_moduloxrol")
async def create_moduloxrol(moduloxrol: ModuloxRol):
    rpta = moduloxrol_controller.create_moduloxrol(moduloxrol)
    return rpta

@router.get("/get_moduloxrol/{id}", response_model=ModuloxRol)
async def get_moduloxrol(id: int):
    rpta = moduloxrol_controller.get_moduloxrol(id)
    return rpta

@router.get("/get_modulosxroles/")
async def get_modulosxroles():
    rpta = moduloxrol_controller.get_modulosxroles()
    return rpta

@router.put("/update_moduloxrol/{id}")
async def update_moduloxrol(id: int, moduloxrol: ModuloxRol):
    rpta = moduloxrol_controller.update_moduloxrol(id, moduloxrol)
    return rpta

@router.put("/disable_moduloxrol/{id}")
async def disable_moduloxrol(id: int):
    rpta = moduloxrol_controller.disable_moduloxrol(id)
    return rpta

@router.put("/enable_moduloxrol/{id}")
async def enable_moduloxrol(id: int):
    rpta = moduloxrol_controller.enable_moduloxrol(id)
    return rpta