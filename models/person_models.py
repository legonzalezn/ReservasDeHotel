from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PersonNameFullOut(BaseModel):
    name:str

class PersonIdIn(BaseModel):
    id:int

class PersonIn(BaseModel):
    nombre1:str
    nombre2:Optional[str] = ""
    apellido1:str
    apellido2:Optional[str] = ""
    fecha_nacimiento:Optional[datetime] = datetime(9999,12,31)
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

class PersonOut(BaseModel):
    id:int
    nombre1:str
    nombre2:str
    apellido1:str
    apellido2:str
    fecha_nacimiento:datetime
    nacionalidad:int
    numeroDeContacto:str
    direccion:str
    ubicacion:int
    otra:str
    documento:int
    numero:str
    email:str
    creado:datetime
    modificado:datetime