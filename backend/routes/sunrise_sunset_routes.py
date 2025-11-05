from fastapi import APIRouter
from backend.controller.sunrise_sunset_controller import get_sunrise_sunset
router=APIRouter()

@router.get("/sunrise_sunset")
async def sunrise_sunset(lat: float, lon: float):
 return await get_sunrise_sunset(lat, lon)

