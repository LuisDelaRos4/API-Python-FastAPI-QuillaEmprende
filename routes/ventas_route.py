from fastapi import APIRouter
from controllers.ventas_controller import VentasController
from models.ventas_model import Venta

router = APIRouter()

ventas_controller = VentasController()

@router.post("/create_venta")
async def create_venta(venta: Venta):
    rpta = ventas_controller.create_venta(venta)
    return rpta

@router.get("/get_venta/{id}", response_model=Venta)
async def get_venta(id: int):
    rpta = ventas_controller.get_venta(id)
    return rpta

@router.get("/get_ventas/")
async def get_ventas():
    rpta = ventas_controller.get_ventas()
    return rpta

@router.put("/update_venta/{id}")
async def update_venta(id: int, venta: Venta):
    rpta = ventas_controller.update_venta(id, venta)
    return rpta

@router.put("/disable_venta/{id}")
async def disable_venta(id: int):
    rpta = ventas_controller.disable_venta(id)
    return rpta

@router.put("/enable_venta/{id}")
async def enable_venta(id: int):
    rpta = ventas_controller.enable_venta(id)
    return rpta
