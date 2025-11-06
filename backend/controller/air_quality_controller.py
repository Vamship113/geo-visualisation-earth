from backend.services.air_quality_service import fetch_air_quality_data

async def get_air_quality(city: str=None, lat: float=None, lon: float=None):
    data = await fetch_air_quality_data(city, lat, lon)
    return {
        "city": data['city'],
        "coordinates": data['coordinates'],
        "aqi": data['aqi'],
        "dominentpol": data['dominentpol'],
        "pollutants": data['pollutants'],
        "forecast": data['forecast'],
        "time": data['time'],
        "status": data['status']
    }
