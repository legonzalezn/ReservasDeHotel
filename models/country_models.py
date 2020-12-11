from pydantic import BaseModel

class CountryNameIn(BaseModel):
    name:str

class CountryIn(BaseModel):
    id:int

class CountryOut(BaseModel):
    id:int
    name:str
