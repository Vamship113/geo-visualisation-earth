import httpx

async def fetch_sunrise_sunset(lat: float, lng: float):

    url=f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&formatted=0"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    results=data.get("results", {})
    return {
        'sunrise': results.get("sunrise"),
        'sunset': results.get("sunset")
    }