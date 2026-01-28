from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI()

class Student(BaseModel): #used for automatic schema validation 
    name : str 
    age: int
    course: str

@app.get('/')
def home():
    return "Hello Welcome"

@app.post('/student/create')
def student(data: Student): 
    name = data.name 