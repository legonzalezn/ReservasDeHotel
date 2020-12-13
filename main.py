from typing import Dict
from auxiliar import message

from db.country_db import CountryInDB
from db.country_db import get_id, get_name, get_list

from models.country_models import CountryIn, CountryBoolIn, CountryNameIn, CountryOut

from db.person_db import PersonInDB
from db.person_db import get_person_full, get_name_full, save_person, update_person, delete_person, get_person_list

from models.person_models import PersonIn, PersonIdIn, PersonUpdateIn, PersonNameFullOut, PersonOut, PersonDeleteOut

from fastapi import FastAPI
from fastapi import HTTPException

reservas = FastAPI()

@reservas.get("/list/country/")
async def get_country(country_in:CountryIn):
    country_in_db = get_name(country_in.id)
    if country_in_db == None:
        raise HTTPException(status_code=404, detail = message(1, "país"))
    else:
        country_out = CountryOut(**country_in_db.dict())
        return country_out

@reservas.get("/list/countries/")
async def get_countries(index_id:CountryBoolIn):
    country_in_db = get_list(index_id.index_id)
    if country_in_db == None:
        raise HTTPException(status_code=404, detail = message(2, "paises"))
    else:
        return country_in_db

@reservas.get("/list/country_name/")
async def get_country(country_in:CountryNameIn):
    country_in_db = get_id(country_in.name)
    if country_in_db == None:
        raise HTTPException(status_code=404, detail = message(3, "país", "nombre"))
    else:
        country_out = CountryOut(**country_in_db.dict())
        return country_out

@reservas.get("/person/")
async def get_person(person_in:PersonUpdateIn):
    person_in_db = get_person_full(person_in.id)
    if person_in_db == None:
        raise HTTPException(status_code=404, detail = message(1,"usuario"))
    else:
        person_out = PersonOut(**person_in_db.dict())
        return person_out

@reservas.get("/list/person/")
async def get_list_person():
    person_in_db = get_person_list()
    if person_in_db == None:
        raise HTTPException(status_code=404, detail = message(2,"usuarios"))
    else:
        return person_in_db

@reservas.get("/person/full_name/")
async def get_full_name(person_in:PersonIdIn):
    person_in_db = get_person_full(person_in.id)
    if person_in_db == None:
        raise HTTPException(status_code=404, detail = message(1,"usuario"))
    else:
        person_out = PersonNameFullOut(**{"name":get_name_full(person_in_db.id)})
        return person_out

@reservas.post("/add/person/")
async def post_person(person_in:PersonIn):
    person_in_aux = person_in.dict()
    person_in_aux["id"] = 0
    person_in_db = PersonInDB(**person_in_aux)

    person_in_db = save_person(person_in_db)

    person_out = PersonOut(**person_in_db.dict())

    return person_in_db

@reservas.put("/update/person/")
async def put_person(person_in:PersonUpdateIn):
    updated = False
    person_in_db = get_person_full(person_in.id)
    if person_in_db == None:
        raise HTTPException(status_code=404, detail = message(1,"usuario"))
    else:
        person_in_db = person_in_db.dict()
        for personk, personv in person_in.dict().items():
            if personv != None:
                if person_in_db[personk] != personv:
                    person_in_db[personk] = personv
                    updated = True
        if updated:
            person_in_db = update_person(person_in_db)
            person_out = PersonOut(**person_in_db)
            return person_out
        else:
            raise HTTPException(status_code=404, detail = mensaje(4))

@reservas.delete("/delete/person/")
async def del_person(person_in:PersonIdIn):
    person_in_db = get_person_full(person_in.id)
    if person_in_db == None:
        raise HTTPException(status_code=404, detail = message(1,"usuario"))
    else:
        count = delete_person(person_in.id)
        return count