from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import closing
import os
from app.core.database import Database
from app.api import (
    rutas_programas,
    rutas_estudiantes,
    rutas_empresas,
    rutas_tutor_academicos,
    rutas_tutor_empresarials,
    rutas_convenios,
    rutas_practicas,
    rutas_seguimientos,
    rutas_evaluacions,
    rutas_documentos,
    rutas_roles,
)

app = FastAPI(
    title="API Sistema de Gestión de Prácticas Profesionales",
    description="Backend modular con FastAPI y PostgreSQL (Neon) para Sistema de Gestión de Prácticas Profesionales",
    version="1.0.0"
)

allowed_origins = [
    origin.strip().rstrip("/")
    for origin in os.getenv("CORS_ORIGINS", "https://front-parcial-1-corte.onrender.com").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conectamos cada módulo de rutas a la aplicación principal
app.include_router(rutas_roles.router)
app.include_router(rutas_programas.router)
app.include_router(rutas_estudiantes.router)
app.include_router(rutas_empresas.router)

# Rutas de tutores
app.include_router(rutas_tutor_academicos.router)
app.include_router(rutas_tutor_academicos.router_compat)

app.include_router(rutas_tutor_empresarials.router)
app.include_router(rutas_tutor_empresarials.router_compat)

app.include_router(rutas_convenios.router)
app.include_router(rutas_practicas.router)
app.include_router(rutas_seguimientos.router)
app.include_router(rutas_evaluacions.router)
app.include_router(rutas_documentos.router)


@app.get("/")
def estado_api():
    return {
        "mensaje": "API Para Sistema de Gestión de Prácticas Profesionales",
        "estado": "Activo",
        "framework": "FastAPI + PostgreSQL (Neon)",
        "base_datos": "Conectada" if database_check() else "No disponible"
    }


@app.get("/health")
def health_check():
    return {"estado": "ok"}


def database_check():
    try:
        with closing(Database().get_connection()) as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                return cursor.fetchone() is not None
    except Exception:
        return False
