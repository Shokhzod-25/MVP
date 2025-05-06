from pydantic import BaseModel


class UserData(BaseModel):
    username: str
    age: int
    file_name: str
