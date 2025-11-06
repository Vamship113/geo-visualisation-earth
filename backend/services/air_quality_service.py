import os 
from dotenv import load_dotenv
import httpx
import asyncio
load_dotenv()
token=os.getenv("AQICN_API_KEY")

async def fetch_air_quality_data(city: str=None, lat: float=None, lon: float=None) -> dict:
    if city:
        url=f"https://api.waqi.info/feed/{city}/?token={token}"
    elif lat is not None and lon is not None:
        url=f"https://api.waqi.info/feed/geo:{lat};{lon}/?token={token}"
    else:
        raise ValueError("Either city or both lat and lon must be provided.")
    
    async with httpx.AsyncClient() as Client:
        response = await Client.get(url)
        data = response.json()
    results=data.get("data", {})
    return{
        'city': results.get("city", {}).get("name"),
        'coordinates': {
            'lat': results.get("city", {}).get("geo", [None, None])[0],
            'lon': results.get("city", {}).get("geo", [None, None])[1],
        },
        'aqi': results.get("aqi"),
        'dominentpol': results.get("dominentpol"),
        'pollutants': results.get("iaqi", {}),
        'forecast': results.get("forecast", {}).get("daily", {}),
        'time': results.get("time", {}).get("s"),
        'status':"ok"
    }


