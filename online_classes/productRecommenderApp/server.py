from fastapi import FastAPI 
from pydantic import BaseModel, Field
from agent import SearchAgent
import json

app = FastAPI(title="Product Recommendation App")

categories = ['Fashion', 'Electronics', 'Food', 'Apps', 'Games', 'Books', 'Beauty', 'Cosmetics']

class RecommendationRequest(BaseModel): 
    Product_Description: str 
    category: str
    budget: int
    quantity: int 

@app.get('/')
def home(): 
    return {"Message":"Welcome to the App"}

@app.post('/recommend')
def recommend(request:RecommendationRequest):

    if request.category not in categories: 
        return {"error":f"Invalid Category, Please choose from: {categories}"}
    
    try: 
        agent = SearchAgent()
        response = agent.run(request.Product_Description)
        return json.loads(json.loads(response))
    except Exception as e: 
        return {"error": str(e)}
