# API2026 - Sistema de Gestión de Prácticas Profesionales

## Estructura

- `app/core/database.py`: conexión con Neon PostgreSQL.
- `app/models/`: modelos Pydantic.
- `app/repositories/`: CRUD y SQL.
- `app/api/`: rutas/endpoints.
- `app/main.py`: aplicación FastAPI.

## Instalación

```bash
pip install -r requirements.txt
```

Copia `.env.example` como `.env` y coloca tu `DATABASE_URL` de Neon.

## Ejecutar

```bash
uvicorn app.main:app --reload
```

## CRUD

Cada tabla tiene:

- GET `/tabla/`
- GET `/tabla/{id}`
- POST `/tabla/`
- PUT `/tabla/{id}`
- DELETE `/tabla/{id}`

Las tablas deben existir previamente en Neon usando el script SQL de la base de datos.

El frontend carga programas, empresas y estudiantes desde esta API al iniciar y
guarda sus altas y bajas en PostgreSQL. Los demás módulos todavía conservan sus
datos de demostración porque sus modelos requieren una adaptación independiente.
