from pydantic import BaseModel, constr


class Register(BaseModel):
    name: str
    cpf: str
    address: str
    phone: constr(min_length=10, max_length=20)
