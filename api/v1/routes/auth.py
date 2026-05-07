from fastapi import APIRouter, Depends
from fastapi.exceptions import MalformedRequest
from fastapi.requests import Request

router = APIRouter(
    prefix = "/auth",
    tags = ["auth"]
)
#declaração das rotas de autenticação, como login, registro e logout. Cada rota é definida
@router.post("/login")
async def Login():
    #a função Login é um endpoint POST que, quando chamada, retorna uma mensagem indicando que é a rota de login. Da mesma forma, as funções Register e Logout são endpoints POST para registro e logout, respectivamente, cada uma retornando uma mensagem correspondente. Essas rotas são incluídas no roteador principal (Main_router) para serem acessíveis através do prefixo "/auth".
    return {"message": "Login route"}


@router.post("/register")
async def Register(request: Request):
    #Registra um usuario com email e senha 
    return {"message": "Register route"}


@router.post("/logout")
async def Logout():
    return {"message": "Logout route"}