from backend.controller.weather_controller import get_weather
from fastapi import APIRouter
router=APIRouter()
@router.get("/weather")
async def weather(lat: float, lon: float):
 return await get_weather(lat, lon)