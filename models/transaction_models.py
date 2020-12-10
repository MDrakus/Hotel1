from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    nombre: str
    totalHabitaciones: int

class TransactionOut(BaseModel):
    id_transaction: int
    nombre: str
    date: datetime
    totalHabs: int
