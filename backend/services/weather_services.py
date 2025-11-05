import openmeteo_requests

async def fetch_weather_data(lat: float, lon: float):
    openmeteo = openmeteo_requests.AsyncClient()  # no async with
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": ["temperature_2m", "precipitation"],
        "current": ["temperature_2m", "relative_humidity_2m", "windspeed_10m"],
        "timezone": "auto"
    }

    responses = await openmeteo.weather_api(url, params=params)
    response = responses[0]
    current = response.Current()

    current_temperature_2m = current.Variables(0).Value()
    current_relative_humidity_2m = current.Variables(1).Value()
    current_windspeed_10m = current.Variables(2).Value()
    elevation = response.Elevation()

    return {
        "latitude": lat,
        "longitude": lon,
        "temperature": current_temperature_2m,
        "humidity": current_relative_humidity_2m,
        "windspeed": current_windspeed_10m,
        "elevation": elevation
    }
