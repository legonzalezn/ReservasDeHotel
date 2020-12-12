from pydantic import BaseModel

class CountryNameIn(BaseModel):
    name:str

class CountryIn(BaseModel):
    id:int

class CountryBoolIn(BaseModel):
    index_id:bool

class CountryOut(BaseModel):
    id:int
    name:str