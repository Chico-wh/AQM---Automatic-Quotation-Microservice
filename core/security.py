from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from core.config import settings


# Configuração do bcrypt para hash de senha.
# Isso será usado no cadastro e no login.
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    """
    Recebe uma senha em texto puro e retorna a senha com hash.

    Nunca salve senha pura no banco.
    """

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compara a senha enviada no login com o hash salvo no banco.

    Retorna True se bater.
    Retorna False se estiver errada.
    """

    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Cria um token JWT.

    O parâmetro data geralmente recebe algo como:
        {"sub": "1"}

    O "sub" significa subject, ou seja, o dono do token.
    Nesse caso, vamos guardar o ID do usuário.
    """

    # Copia os dados para não alterar o dict original
    to_encode = data.copy()

    # Define quando o token vai expirar
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Adiciona a expiração dentro do token
    to_encode.update({"exp": expire})

    # Gera o JWT usando a SECRET_KEY e o algoritmo configurado
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    return encoded_jwt


def decode_access_token(token: str) -> dict:
    """
    Decodifica e valida um token JWT.

    Se o token estiver inválido ou expirado,
    o jose vai lançar uma exceção JWTError.
    """

    payload = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM],
    )

    return payload