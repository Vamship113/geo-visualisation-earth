from backend.services.sunrise_sunset_services import fetch_sunrise_sunset

async def get_sunrise_sunset(lat: float, lon: float):
    data= await fetch_sunrise_sunset(lat, lon)
    return {
        "latitude": lat,
        "longitude": lon,
        "sunrise": data['sunrise'],
        "sunset": data['sunset']
    }
