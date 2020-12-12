from typing import Dict

from db.country_db import CountryInDB
from db.country_db import get_id, get_name, get_list

from models.country_models import CountryIn, CountryBoolIn, CountryNameIn, CountryOut

from db.person_db import PersonInDB
from db.person_db import get_person_full, get_name_full, save_person

from models.person_models import PersonIn, PersonIdIn, PersonNameFullOut, PersonOut

from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.get("/list/country/")
async def get_country(country_in:CountryIn):
    country_in_db = get_name(country_in.id)
    if country_in_db == None:
        raise HTTPException(status_code=404, detail="Índice de país no encontrado!")
    else:
        country_out = CountryOut(**country_in_db.dict())
        return country_out

@api.get("/list/countries/")
async def get_countries(index_id:CountryBoolIn):
    country_in_db = get_list(index_id.index_id)
    if country_in_db == None:
        raise HTTPException(status_code=404, detail="No hay información de paises registrados!")
    else:
        return country_in_db

@api.get("/list/country_name/")
async def get_country_name(country_in:CountryNameIn):
    country_in_db = get_id(country_in.name)
    if country_in_db == None:
        raise HTTPException(status_code=404, detail="Nombre de país no encontrado!")
    else:
        country_out = CountryOut(**country_in_db.dict())
        return country_out

@api.post("/add/person/")
async def put_person(person_in:PersonIn):
    person_in_db = PersonInDB(**person_in.dict())

    person_in_db = save_person(person_in_db)

    person_out = PersonOut(**person_in_db.dict())

    return person_in_db