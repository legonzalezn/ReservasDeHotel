from datetime import datetime
from typing import Optional
from typing import Dict
from pydantic import BaseModel

class PersonInDB(BaseModel):
    id:int
    nombre1:str
    nombre2:Optional[str] = ""
    apellido1:str
    apellido2:Optional[str] = ""
    fecha_nacimiento:Optional[datetime] = datetime(9999,12,1)
    nacionalidad:int
    numeroDeContacto:str
    direccion:Optional[str] = ""
    ubicacion:Optional[int] = 0
    otra:Optional[str] = ""
    documento:int
    numero:str
    email:str
    creado:datetime = datetime.now()
    modificado:datetime = datetime.now()

database_person = Dict[int, PersonInDB]

database_person ={
    1:PersonInDB(**{
    "id":1,
    "nombre1":"Alejandro",
    "apellido1":"Silva",
    "nacionalidad":57,
    "numeroDeContacto":"3009876541",
    "documento":1,
    "numero":"1",
    "email":"a.silva@misiontic2022.com.co",
    "creado":"2020-12-11 12:27:57",
    "modificado":"2020-12-11 12:27:57"
    }),
    2:PersonInDB(**{
    "id":2,
    "nombre1":"Alvaro",
    "apellido1":"Guerrero",
    "nacionalidad":57,
    "numeroDeContacto":"3009876542",
    "documento":1,
    "numero":"2",
    "email":"a.guerrero@misiontic2022.com.co",
    "creado":"2020-12-11 12:28:28",
    "modificado":"2020-12-11 12:28:28"
    }),
    3:PersonInDB(**{
    "id":3,
    "nombre1":"Giovanni",
    "apellido1":"Sanabria",
    "nacionalidad":57,
    "numeroDeContacto":"3009876543",
    "documento":1,
    "numero":"3",
    "email":"g.sanabria@misiontic2022.com.co",
    "creado":"2020-12-11 12:28:59",
    "modificado":"2020-12-11 12:28:59"
    }),
    4:PersonInDB(**{
    "id":4,
    "nombre1":"Luis",
    "apellido1":"Gonzalez",
    "nacionalidad":57,
    "numeroDeContacto":"3009876544",
    "documento":1,
    "numero":"4",
    "email":"l.gonzalez@misiontic2022.com.co",
    "creado":"2020-12-11 12:29:19",
    "modificado":"2020-12-11 12:29:19"
    }),
    5:PersonInDB(**{
    "id":5,
    "nombre1":"Maria",
    "apellido1":"Penagos",
    "nacionalidad":57,
    "numeroDeContacto":"3009876545",
    "documento":1,
    "numero":"5",
    "email":"m.penagos@misiontic2022.com.co",
    "creado":"2020-12-11 12:29:45",
    "modificado":"2020-12-11 12:29:45"
    }),
    6:PersonInDB(**{
    "id":6,
    "nombre1":"Simon",
    "apellido1":"Otalvaro",
    "nacionalidad":57,
    "numeroDeContacto":"3009876546",
    "documento":1,
    "numero":"6",
    "email":"s.otalvaro@misiontic2022.com.co",
    "creado":"2020-12-11 12:30:02",
    "modificado":"2020-12-11 12:30:02"
    })
}
generator = {"id":len(database_person)}

def save_person(person_in_db: PersonInDB):
    generator["id"] += 1
    person_in_db.id = generator["id"]
    database_person[person_in_db.id] = person_in_db
    return person_in_db

def update_person(person_in_db: PersonInDB):
    person_in = person_in_db
    person_in["modificado"] = datetime.now()
    database_person[person_in_db["id"]] = PersonInDB(**person_in)
    return person_in

def delete_person(id: int):
    if id in database_person.keys():
        database_person.pop(id)
        return len(database_person)
    else:
        return None

def get_person_full(id: int):
    if id in database_person.keys():
        return database_person[id]
    else:
        return None

def get_person_list():
    person_list_out = {1:"Hola"}
    person_list_out.pop(1)
    for person_key, person_value in database_person.items():
        person_list_out[person_key] = get_name_full(person_key)
    return person_list_out

def get_name_full(id: int):
    if id in database_person.keys():
        person_in = database_person[id]
        name = person_in.nombre1
        if len(person_in.nombre2) != 0:
            name += " " + person_in.nombre2
        name += " " + person_in.apellido1
        if len(person_in.apellido2) != 0:
            name += " " + person_in.apellido2
        return name
    else:
        return None