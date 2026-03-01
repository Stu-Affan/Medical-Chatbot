import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def find_nearby_hospitals(location=None):

    # fallback if location missing
    lat = 13.041343
    lng = 77.565350

    if location and len(location) == 2:
        lat, lng = location

    if not API_KEY:
        return "⚠️ Google Maps API key not loaded."

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    params = {
        "location": f"{lat},{lng}",
        "radius": 5000,
        "type": "hospital",
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "OK":
        return f"⚠️ Google API Error: {data.get('status')}"

    hospitals = []

    for place in data.get("results", [])[:5]:
        name = place.get("name")
        address = place.get("vicinity")
        rating = place.get("rating", "N/A")

        hospitals.append(
            f"{name}\n📍 {address}\n⭐ Rating: {rating}\n"
        )

    return "\n".join(hospitals) if hospitals else "No hospitals found nearby."