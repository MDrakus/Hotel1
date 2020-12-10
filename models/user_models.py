from pydantic import BaseModel

class UserIn(BaseModel):
    nombre: str
    ubicacion: str

class UserOut(BaseModel):
    nombre: str
    totalHabitaciones: int
