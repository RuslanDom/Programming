from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    username: str = Field(max_length=30)
    password: str = Field(max_length=50)
    status: bool | None = Field(default=False)
    email: EmailStr
    chat_id: str

class UserSchemaGet(UserSchema):
    id: int