from db.user_db import UserInDB
from db.user_db import update_user, get_user
from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction
from models.user_models import UserIn, UserOut
from models.transaction_models import TransactionIn, TransactionOut
import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):

    user_in_db = get_user(user_in.nombre)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El Hotel no existe")

    if user_in_db.ubicacion != user_in.ubicacion:
        return  {"Autenticado": False}

    return  {"Autenticado": True}


@api.get("/user/totalHabitaciones/{nombre}")
async def get_balance(nombre: str):

    user_in_db = get_user(nombre)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El Hotel no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out


@api.put("/user/transaction/")
async def make_transaction(transaction_in: TransactionIn):

    user_in_db = get_user(transaction_in.nombre)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El hotel no existe")

    if user_in_db.totalHabitaciones < transaction_in.totalHabitaciones:
        raise HTTPException(status_code=400, detail="No se tienen los fondos suficientes")

    user_in_db.totalHabitaciones = user_in_db.totalHabitaciones - transaction_in.reserva
    update_user(user_in_db)

    transaction_in_db = TransactionInDB(**transaction_in.dict(), totalHabs = user_in_db.totalHabitaciones)
    transaction_in_db = save_transaction(transaction_in_db)

    transaction_out = TransactionOut(**transaction_in_db.dict())

    return  transaction_out