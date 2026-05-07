from fastapi import APIRouter, Depends
from fastapi.requests import Request
from core.database import get_db
from core.security import hash_password, verify_password, create_access_token, decode_access_token
from schemas.user_schema import UserCreate, User, UserDelete, UserUpdate
from schemas.auth import login as UserLogin
router = APIRouter(
    prefix = "/auth",
    tags = ["auth"]
)
#declaração das rotas de autenticação, como login, registro e logout. Cada rota é definida
@router.post("/login")
async def Login(user_data: UserLogin, request: Request, db = Depends(get_db)):
    password = user_data.password
    email = user_data.email
    if password is not None and email is not None:
        db_user = db.query(User).filter(User.email == email).first()
        if db_user and verify_password(password, db_user.hashed_password):
            token = create_access_token({"sub": str(db_user.id)})
            return {"acess_token":token, "token_type": "bearer"}
        else:
            return {"message": "Credencias invalidas"}
    #a função Login é um endpoint POST que, quando chamada, retorna uma mensagem indicando que é a rota de login. Da mesma forma, as funções Register e Logout são endpoints POST para registro e logout, respectivamente, cada uma retornando uma mensagem correspondente. Essas rotas são incluídas no roteador principal (Main_router) para serem acessíveis através do prefixo "/auth".
    return {"Error": "error"}


@router.post("/register")
async def Register(user_data: UserCreate, request: Request,db = Depends(get_db)):
    db.add(User(username=user_data.username, email=user_data.email, hashed_password=hash_password(user_data.password)))
    db.commit()

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