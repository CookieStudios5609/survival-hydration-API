from fastapi import FastAPI
import uvicorn
from Utils import AsyncNumberTools
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/")
async def root():
    return {f"Head to /redoc for information"}


@api.get("/calculate/{weight}")
async def get_water_from_weight(weight: int):
    """This calculates how many liters one would need to drink per day at the provided weight, in pounds."""
    water_ounces = await AsyncNumberTools.get_required_water_intake(weight=weight)
    water = await AsyncNumberTools.ounces_to_liters(ounces=water_ounces)
    return {"daily liters": f"{water}"}


@api.get("/supply")
async def get_supply():
    """Returns the amount of water in liters stored in the DB."""
    water_supply, weight, days = await AsyncNumberTools.get_totals()
    return {"supply": f"{water_supply}", "weight": f"{weight}", "days": f"{days}"}


@api.post("/editliters/{operation}/{liters}")
async def edit_water(operation: str, liters: int):
    """Updates the water in liters in the DB.
    Provide the operation (+ or - symbol) and the amount you want to change by"""
    # curl -X POST 127.0.0.1:8000/editwater/+/500
    water_supply = await AsyncNumberTools.get_totals()
    if operation == "+":
        liters = liters + water_supply[0]
    elif operation == "-":
        liters = water_supply[0] - liters
    result = await AsyncNumberTools.update_water_amount(liters)
    return {"result": f"{result}"}


@api.post("/editweight/{operation}/{weight}")
async def edit_weight(operation: str, weight: int):
    """Updates the weight in pounds in the DB.
    Provide the operation (+ or - symbol) and the amount you want to change by"""
    # curl -X POST 127.0.0.1:8000/editweight/+/500
    totals = await AsyncNumberTools.get_totals()
    if operation == "+":
        weight = weight + totals[1]
    elif operation == "-":
        weight = totals[1] - weight
    result = await AsyncNumberTools.update_weight(weight)
    return {"result": f"{result}"}

