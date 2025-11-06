from backend.controller.air_quality_controller import get_air_quality
from fastapi import APIRouter
router = APIRouter()

@router.get("/air_quality")
async def air_quality(city: str = None, lat: float = None, lon: float = None):
    return await get_air_quality(city, lat, lon)