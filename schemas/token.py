from pydantic import BaseModel, Field 

#token que será retornado após o login bem-sucedido, contendo o access_token, token_type e refresh_token. O TokenData é um modelo para os dados contidos no token, como username, user_id e is_active, que podem ser usados para validar e autorizar o acesso a recursos protegidos na aplicação. Esses modelos são essenciais para a implementação de autenticação baseada em tokens JWT (JSON Web Tokens) na aplicação FastAPI.
class Token(BaseModel):
    access_token: str = Field(description="JWT access token for authentication")
    token_type: str = Field(description="Type of the token, typically 'bearer'")
    refresh_token: str = Field(description="JWT refresh token for obtaining new access tokens")
    


#Token data pra retornar os dados do token 
class TokenData(BaseModel):
    username: str = Field(description="Username associated with the token")
    user_id: int = Field(description="User ID associated with the token")
    is_active: bool = Field(description="Indicates whether the user is active or not")