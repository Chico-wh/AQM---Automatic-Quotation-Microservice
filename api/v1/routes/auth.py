from fastapi import APIRouter, Depends
from fastapi.requests import Request
from core.security import hash_password, verify_password, create_access_token, decode_access_token
from schemas.user_schema import UserCreate, UserLogin, User, UserDelete, UserUpdate
router = APIRouter(
    prefix = "/auth",
    tags = ["auth"]
)
#declaração das rotas de autenticação, como login, registro e logout. Cada rota é definida
@router.post("/login")
async def Login(user_data: UserLogin, request: Request):
    
    #a função Login é um endpoint POST que, quando chamada, retorna uma mensagem indicando que é a rota de login. Da mesma forma, as funções Register e Logout são endpoints POST para registro e logout, respectivamente, cada uma retornando uma mensagem correspondente. Essas rotas são incluídas no roteador principal (Main_router) para serem acessíveis através do prefixo "/auth".
    return {"message": "Login route", "method": request.method}


@router.post("/register")
async def Register(user_data: UserCreate, request: Request):

    #Registra um usuario com email e senha 
    return {"message": "Register route"}
@router.get("/me",response_model=User)
async def Me(request: Request):
    token = request.headers.get("Authorization")
    #a função Me é um endpoint GET que retorna as informações do usuário autenticado. Ele
    user_data = decode_access_token(token)

    return {"message": "Me route", "method": request.method,
            'data':
                {"id": user_data.sub,
                "username": user_data.username,
                "email": user_data.email,
                "is_active": user_data.is_active

                }
            
            
            }

@router.post("/logout")
async def Logout():
    return {"message": "Logout route"}