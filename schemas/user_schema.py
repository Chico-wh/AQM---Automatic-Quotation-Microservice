from pydantic import BaseModel, EmailStr, Field
#egamos field, email str pra aumentar a validação do email, e field_serializer para criar um método de serialização personalizado para o campo de senha. O BaseModel é a classe base do Pydantic que permite criar modelos de dados com validação automática.

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50,description="Username must be between 3 and 50 characters")
    email: EmailStr = Field(description="A valid email address is required", example="user@example.com", max_length=50)
    password: str = Field(description="Password Field", example="password123", min_length=8, max_length=128)
#class pra retornar infos de usuarios 
class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    

    class Config:
        orm_mode = True
        from_attributes = True

class UserUpdate(BaseModel):
    username: str = Field(min_length=3, max_length=50,description="Username must be between 3 and 50 characters")
    email: EmailStr = Field(description="A valid email address is required", example="user@example.com", max_length=50)
    password: str = Field(description="Password Field", example="password123", min_length=8, max_length=128)
    active:bool = Field(description="Indicates whether the user is active or not", example=True)

class UserDelete(BaseModel):
    id: int