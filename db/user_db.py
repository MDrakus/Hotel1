from typing import  Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    nombre:str
    ubicacion:str
    estrellas:str
    totalHabitaciones:int
    sencilla:int
    doble:int
    triple:int
    suite:int

database_users = Dict[str, UserInDB]

database_users = {

    "Hotel1": UserInDB(**{"nombre":"Hotel1",
                            "ubicacion":"Colombia",
                            "estrellas":"cinco",
                            "totalHabitaciones":30,
                            "sencilla":15,
                            "doble":10,
                            "triple":3,
                            "suite":2,
                            
                                            }),

    "Hotel2": UserInDB(**{"nombre":"Hotel2",
                            "ubicacion":"Colombia",
                            "estrellas":"tres",
                            "totalHabitaciones":12,
                            "sencilla":4,
                            "doble":4,
                            "triple":4,
                            "suite":0,
                                            }),
}

def get_user(nombre: str):
    if nombre in database_users.keys():
        return database_users[nombre]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
