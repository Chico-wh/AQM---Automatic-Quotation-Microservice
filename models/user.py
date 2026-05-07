from pydantic import BaseModel
#importamos o BaseModel do Pydantic para criar um modelo de dados para o usuário

class User(BaseModel):
    username: str
    password: str
#criamos a classe User que herda de BaseModel, com os campos username e password, ambos do tipo string. Este modelo será usado para validar os dados de entrada ao criar um novo usuário ou fazer login.
    is_active: bool
    