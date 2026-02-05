from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI() #FastAPI() is a router 

class Student(BaseModel): #used for automatic schema validation 
    name : str 
    age: int
    course: str

