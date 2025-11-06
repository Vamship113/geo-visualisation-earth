# Backend API Design
## Overview
This backend acts as a data aggregotor and cache layer for weather, sallelite, air quality, and disaster information. It collects data from public APIs, normalise, it stores in mongodb atlas and serves it to frontend for visualization.
## Core External APIS used
1. Weather https://open-meteo.com  
2. Sunrise and Sunset  https://sunrise-sunset.org/api
3. Air Quality https://docs.openaq.org/  or https://aqicn.org/json-api/doc/
4. Satellite image 
5. Natural Disasters https://eonet.gsfc.nasa.gov/docs/v3 
6. Reverse Geocoding / City Names https://nominatim.org/release-docs/develop/api/Search/ optional for now. It helper if you want to display city names or region metadata
## API Endpoints Plan

| Endpoint | Method | Purpose | External API | Caching | Notes |
|-----------|---------|----------|---------------|----------|--------|
| /api/weather | GET | Returns current temperature, precipitation, humidity, and windspeed for a given bounding box (bbox) | Open-Meteo | 1 hour | Used for temperature and precipitation map layers |
| /api/sunrise | GET | Returns sunrise and sunset times for specific coordinates | Sunrise–Sunset | 24 hours | Drives the day-night animation on the map |
| /api/airquality | GET | Returns air quality metrics (PM2.5, PM10, NO₂, etc.) for a given location or region | OpenAQ or AQICN | 1 hour | Used for AQI overlays |
| /api/satellite | GET | Returns metadata for NASA satellite imagery (e.g., MODIS True Color, VIIRS) for given layer/time | NASA GIBS | 6–12 hours | Serves base map imagery layer |
| /api/disasters | GET | Returns recent natural disasters like storms, floods, fires, and earthquakes | NASA EONET | 6–12 hours | Used for disaster overlays and alerts |
| /api/places | GET | Returns major place names (cities, regions) within visible map area (bbox) | OSM Nominatim | 7 days | Optional, used for labeling maps dynamically |

---

## Background Tasks (Scheduler)

| Task | Frequency | Description | Purpose |
|------|------------|-------------|----------|
| refresh_weather_data | Every 1 hour | Fetches weather data for key regions and updates the cache | Keeps weather layer current |
| refresh_aqi_data | Every 1 hour | Updates cached air quality data | Keeps AQI layer fresh |
| refresh_satellite_metadata | Every 6 hours | Updates satellite image layer metadata | Prevents stale imagery |
| refresh_disaster_feed | Every 6 hours | Pulls latest NASA EONET events | Ensures disaster overlay accuracy |
| cleanup_expired_cache | Every 24 hours | Deletes old cached data from MongoDB using TTL | Prevents memory bloat |

---

## Data Storage Plan (MongoDB Collections)

| Collection | Description | Key Fields | TTL |
|-------------|--------------|-------------|------|
| weather_cache | Stores regional weather JSON data | bbox, timestamp, data | 1 hour |
| aqi_cache | Caches air quality data per region | bbox, timestamp, data | 1 hour |
| satellite_cache | Holds NASA GIBS imagery metadata | layer, timestamp, data | 6–12 hours |
| disaster_cache | Stores EONET disaster events | type, region, timestamp | 12 hours |
| sunrise_cache | Stores sunrise/sunset info per coordinate | lat, lon, date, data | 24 hours |
| place_cache | Stores cached city and region names for map tiles | bbox, places, expiresAt | 7 days |

---

## Response Format (Standardized JSON)

All endpoints should return consistent JSON responses:

```json
{
  "status": "success",
  "cached": true,
  "source": "open-meteo",
  "timestamp": "2025-11-04T14:30Z",
  "data": { }
}
