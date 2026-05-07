from pydantic import BaseModel, Field
from pydantic import BaseModel, EmailStr, Field


class login(BaseModel):
    email: EmailStr = Field(description="A valid email address is required", example="user@example.com")
    password: str = Field(description="Password for login", example="password123")
