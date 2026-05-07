from fastapi import APIRouter, Depends
from api.v1.routes import auth
from fastapi import FastAPI

Main_router = APIRouter()

#Auth routes 
Main_router.include_router(auth.router,prefix = "/api/v1")