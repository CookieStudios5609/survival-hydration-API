from fastapi import FastAPI
import uvicorn
from Utils import AsyncNumberTools


api = FastAPI()


@api.get("/calculate/{weight}")
async def get_water_from_weight(weight: int):
    water_ounces = await AsyncNumberTools.get_required_water_intake(weight=weight)
    water = await AsyncNumberTools.ounces_to_liters(ounces=water_ounces)
    return {"daily liters": f"{water}"}


@api.get("/supply")
async def get_supply():
    water_supply = await AsyncNumberTools.get_total_water_supply()
    return {"supply": f"{water_supply}"}


@api.post("/edit/{operation}/{liters}")
async def update_water(operation: str, liters: int):
    """Updates the water in liters in the DB.
    Provide the operation (+ or - symbol) and the amount you want to change by"""
    # curl -X POST 127.0.0.1:8000/edit/+/500
    water_supply = await AsyncNumberTools.get_total_water_supply()
    if operation == "+":
        liters = liters + water_supply
    elif operation == "-":
        liters = water_supply - liters
    result = await AsyncNumberTools.update_water_amount(liters)
    return {"result": f"{result}"}


if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000, reload=True)
