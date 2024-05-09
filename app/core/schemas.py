from pydantic import BaseModel


class Services(BaseModel):
    id: int
    name: str
    is_active: bool

    class Config:
        orm_mode = True
