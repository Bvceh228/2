from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
class Pizza(BaseModel):
    name: str
    description: str
    ingredients: list[str]
    price: float
pizzas = [
    Pizza(name="Pepperoni", description="A classic pizza with pepperoni", ingredients=['1', '2', '3'], price=10.0), 
    Pizza(name="Pepperoni2", description="A classic pizza with pepperoni2", ingredients=['1', '2', '3'], price=12.0)
]
@app.get("/")
async def root():
    return pizzas
@app.get("/pizzas/{pizza_name}")
async def get_pizza(pizza_name: str):
    for pizza in pizzas:
        if pizza.name == pizza_name:
            return pizza
    raise HTTPException(status_code=404, detail="Pizza not found")
