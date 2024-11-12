from fastapi import FastAPI
from routes.modulos_route import router as modulo_router
from routes.roles_route import router as rol_router
from routes.modulosxrol_route import router as modulosxrol_router
from routes.generos_route import router as genero_router
from routes.tipos_documentos_route import router as tipo_documento_router
from routes.tipos_prod_serv_route import router as tipo_prod_serv_router
from routes.categorias_prod_serv_route import router as categoria_prod_serv_router
from routes.productos_servicios_route import router as producto_servicio_router
from routes.ventas_route import router as venta_router
from routes.abonos_route import router as abono_router
from routes.usuarios_route import router as usuario_router

import os

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost:4200"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(modulo_router,tags=["Requests Módulos"])   
app.include_router(rol_router,tags=["Requests Roles"])   
app.include_router(modulosxrol_router,tags=["Requests Módulos por Roles"])   
app.include_router(genero_router,tags=["Requests Géneros"])
app.include_router(tipo_documento_router,tags=["Requests Tipos de Documentos"])
app.include_router(tipo_prod_serv_router,tags=["Requests Tipos de Productos y Servicios"])
app.include_router(categoria_prod_serv_router,tags=["Requests Categorías de Productos y Servicios"])
app.include_router(producto_servicio_router,tags=["Requests Productos y Servicios"])
app.include_router(venta_router,tags=["Requests Ventas"])
app.include_router(abono_router,tags=["Requests Abonos"])
app.include_router(usuario_router,tags=["Requests Usuarios"])





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=os.getenv("DB_HOST"), port=3306)