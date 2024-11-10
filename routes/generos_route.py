from fastapi import APIRouter
from controllers.generos_controller import GenerosController
from models.generos_model import Genero

router = APIRouter()

genero_controller = GenerosController()

@router.post("/create_genero")
async def create_genero(genero: Genero):
    rpta = genero_controller.create_genero(genero)
    return rpta

@router.get("/get_genero/{id}", response_model=Genero)
async def get_genero(id: int):
    rpta = genero_controller.get_genero(id)
    return rpta

@router.get("/get_generos/")
async def get_generos():
    rpta = genero_controller.get_generos()
    return rpta

@router.put("/update_genero/{id}")
async def update_genero(id: int, genero: Genero):
    rpta = genero_controller.update_genero(id, genero)
    return rpta

@router.put("/disable_genero/{id}")
async def disable_genero(id: int):
    rpta = genero_controller.disable_genero(id)
    return rpta

@router.put("/enable_genero/{id}")
async def enable_genero(id: int):
    rpta = genero_controller.enable_genero(id)
    return rpta