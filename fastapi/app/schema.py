from pydantic import BaseModel, EmailStr

class userCreate(BaseModel):
    email: EmailStr
    first_name: str
    last_name : str
    passowrd: str

    class Config:
        orm_mode = True
