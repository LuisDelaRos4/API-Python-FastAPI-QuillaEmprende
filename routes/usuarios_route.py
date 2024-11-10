from fastapi import APIRouter
from controllers.usuarios_controller import UsuariosController
from models.usuarios_model import Usuario

router = APIRouter()

usuario_controller = UsuariosController()

@router.post("/create_usuario")
async def create_usuario(usuario: Usuario):
    rpta = usuario_controller.create_usuario(usuario)
    return rpta

@router.get("/get_usuario/{id}", response_model=Usuario)
async def get_usuario(id: int):
    rpta = usuario_controller.get_usuario(id)
    return rpta

@router.get("/get_usuarios/")
async def get_usuarios():
    rpta = usuario_controller.get_usuarios()
    return rpta

@router.put("/update_usuario/{id}")
async def update_usuario(id: int, usuario: Usuario):
    rpta = usuario_controller.update_usuario(id, usuario)
    return rpta

@router.put("/disable_usuario/{id}")
async def disable_usuario(id: int):
    rpta = usuario_controller.disable_usuario(id)
    return rpta

@router.put("/enable_usuario/{id}")
async def enable_usuario(id: int):
    rpta = usuario_controller.enable_usuario(id)
    return rpta
