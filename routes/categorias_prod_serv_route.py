from fastapi import APIRouter
from controllers.categorias_prod_serv_controller import Categorias_Prod_ServController
from models.categorias_prod_serv_model import Categoria_Prod_Serv

router = APIRouter()

categoria_prod_serv_controller = Categorias_Prod_ServController()

@router.post("/create_categoria_prod_serv")
async def create_categoria_prod_serv(categoria_prod_serv: Categoria_Prod_Serv):
    rpta = categoria_prod_serv_controller.create_categoria_prod_serv(categoria_prod_serv)
    return rpta

@router.get("/get_categoria_prod_serv/{id}", response_model=Categoria_Prod_Serv)
async def get_categoria_prod_serv(id: int):
    rpta = categoria_prod_serv_controller.get_categoria_prod_serv(id)
    return rpta

@router.get("/get_categorias_prod_serv/")
async def get_categorias_prod_serv():
    rpta = categoria_prod_serv_controller.get_categorias_prod_serv()
    return rpta

@router.put("/update_categoria_prod_serv/{id}")
async def update_categoria_prod_serv(id: int, categoria_prod_serv: Categoria_Prod_Serv):
    rpta = categoria_prod_serv_controller.update_categoria_prod_serv(id, categoria_prod_serv)
    return rpta

@router.put("/disable_categoria_prod_serv/{id}")
async def disable_categoria_prod_serv(id: int):
    rpta = categoria_prod_serv_controller.disable_categoria_prod_serv(id)
    return rpta

@router.put("/enable_categoria_prod_serv/{id}")
async def enable_categoria_prod_serv(id: int):
    rpta = categoria_prod_serv_controller.enable_categoria_prod_serv(id)
    return rpta