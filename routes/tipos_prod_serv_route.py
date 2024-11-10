from fastapi import APIRouter
from controllers.tipos_prod_serv_controller import TiposProdServController   
from models.tipos_prod_serv_model import Tipo_Prod_Serv

router = APIRouter()

tipo_prod_serv_controller = TiposProdServController()

@router.post("/create_tipo_prod_serv")
async def create_tipo_prod_serv(tipo_prod_serv: Tipo_Prod_Serv):
    rpta = tipo_prod_serv_controller.create_tipo_prod_serv(tipo_prod_serv)
    return rpta

@router.get("/get_tipo_prod_serv/{id}", response_model=Tipo_Prod_Serv)
async def get_tipo_prod_serv(id: int):
    rpta = tipo_prod_serv_controller.get_tipo_prod_serv(id)
    return rpta

@router.get("/get_tipos_prod_serv/")
async def get_tipos_prod_serv():
    rpta = tipo_prod_serv_controller.get_tipos_prod_serv()
    return rpta

@router.put("/update_tipo_prod_serv/{id}")
async def update_tipo_prod_serv(id: int, tipo_prod_serv: Tipo_Prod_Serv):
    rpta = tipo_prod_serv_controller.update_tipo_prod_serv(id, tipo_prod_serv)
    return rpta

@router.put("/disable_tipo_prod_serv/{id}")
async def disable_tipo_prod_serv(id: int):
    rpta = tipo_prod_serv_controller.disable_tipo_prod_serv(id)
    return rpta

@router.put("/enable_tipo_prod_serv/{id}")
async def enable_tipo_prod_serv(id: int):
    rpta = tipo_prod_serv_controller.enable_tipo_prod_serv(id)
    return rpta
