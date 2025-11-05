from backend.services.weather_services import fetch_weather_data

async def get_weather(lat:float,lon:float):
    data= await fetch_weather_data(lat, lon)
    return {
        "latitude": lat,
        "longitude": lon,
        "temperature": data['temperature'],
        "humidity": data['humidity'],
        "windspeed": data['windspeed'],
        "elevation": data['elevation']
    }