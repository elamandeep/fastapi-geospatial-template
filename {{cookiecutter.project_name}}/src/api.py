from fastapi import FastAPI
from src.auth.controller import router as auth_router
from src.users.controller import router as users_router
from src.location.controller import router as location_router


def register_routes(app: FastAPI):
    app.include_router(location_router)
    app.include_router(auth_router)
    app.include_router(users_router)
