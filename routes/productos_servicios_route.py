from fastapi import APIRouter
from controllers.productos_servicios_controller import ProductoServicioController
from models.productos_servicios_model import Producto_Servicio

router = APIRouter()

producto_servicio_controller = ProductoServicioController()


@router.post("/create_producto_servicio")
async def create_producto_servicio(producto_servicio: Producto_Servicio):
    rpta = producto_servicio_controller.create_producto_servicio(producto_servicio)
    return rpta

@router.get("/get_producto_servicio/{id}", response_model=Producto_Servicio)
async def get_producto_servicio(id: int):
    rpta = producto_servicio_controller.get_producto_servicio(id)
    return rpta

@router.get("/get_productos_servicios/")
async def get_productos_servicios():
    rpta = producto_servicio_controller.get_productos_servicios()
    return rpta

@router.put("/update_producto_servicio/{id}")
async def update_producto_servicio(id: int, producto_servicio: Producto_Servicio):
    rpta = producto_servicio_controller.update_producto_servicio(id, producto_servicio)
    return rpta

@router.put("/disable_producto_servicio/{id}")
async def disable_producto_servicio(id: int):
    rpta = producto_servicio_controller.disable_producto_servicio(id)
    return rpta

@router.put("/enable_producto_servicio/{id}")
async def enable_producto_servicio(id: int):
    rpta = producto_servicio_controller.enable_producto_servicio(id)
    return rpta
