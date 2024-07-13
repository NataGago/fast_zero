from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    """Message"""

    message: str


class UserSchema(BaseModel):
    """Cadastro de Usuário"""

    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    """Retorno do Usuário"""

    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    """ID do usuário no banco de dados"""

    id: int


class UserList(BaseModel):
    """Lista os usuários"""

    users: list[UserPublic]
