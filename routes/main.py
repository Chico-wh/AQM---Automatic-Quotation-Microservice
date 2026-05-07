from fastapi import APIRouter, Depends
from fastapi.exceptions import MalformedRequest
from routes import auth

Main_router = APIRouter()

#Auth routes 
Main_router.include_router(auth.router)