from fastapi import APIRouter
from controllers.abonos_controller import AbonosController
from models.abonos_model import Abono

router = APIRouter()

abono_controller = AbonosController()

@router.post("/create_abono")
async def create_abono(abono: Abono):
    rpta = abono_controller.create_abono(abono)
    return rpta

@router.get("/get_abono/{id}", response_model=Abono)
async def get_abono(id: int):
    rpta = abono_controller.get_abono(id)
    return rpta

@router.get("/get_abonos/")
async def get_abonos():
    rpta = abono_controller.get_abonos()
    return rpta

@router.put("/update_abono/{id}")
async def update_abono(id: int, abono: Abono):
    rpta = abono_controller.update_abono(id, abono)
    return rpta

@router.put("/disable_abono/{id}")
async def disable_abono(id: int):
    rpta = abono_controller.disable_abono(id)
    return rpta

@router.put("/enable_abono/{id}")
async def enable_abono(id: int):
    rpta = abono_controller.enable_abono(id)
    return rpta
