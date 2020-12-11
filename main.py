from db.country_db import CountryInDB
from db.country_db import get_id, get_name

from models.country_models import CountryIn, CountryNameIn, CountryOut

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.get("/list/country/")
async def get_country(country_in:CountryIn):
    country_in_db = get_name(country_in.id)
    if country_in_db == None:
        raise HTTPException(status_code=404, detail="Índice de país no encontrado!")
    else:
        return{"name":country_in_db.name}

@api.get("/list/country_name/")
async def get_country(country_in:CountryNameIn):
    country_in_db = get_id(country_in.name)
    if country_in_db == None:
        raise HTTPException(status_code=404, detail="Nombre de país no encontrado!")
    else:
        return{"id":country_in_db.id}
