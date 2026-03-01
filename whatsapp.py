from fastapi import APIRouter, Request, Response
from twilio.twiml.messaging_response import MessagingResponse
from router import route_query
from tools.hospital_finder import find_nearby_hospitals

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):

    form = await request.form()

    incoming_msg = form.get("Body", "").lower()
    latitude = form.get("Latitude")
    longitude = form.get("Longitude")

    resp = MessagingResponse()
    msg = resp.message()

    # ✅ If user shares location → ALWAYS fetch hospitals
    if latitude and longitude:
        location = (float(latitude), float(longitude))
        hospitals = find_nearby_hospitals(location)
        msg.body(f"🏥 Nearby Hospitals:\n\n{hospitals}")
        return Response(content=str(resp), media_type="application/xml")

    # 🏥 Hospital intent detection
    hospital_keywords = ["hospital", "clinic", "near me", "nearest"]

    if any(word in incoming_msg for word in hospital_keywords):
        msg.body(
            "📍 Please share your location to find nearby hospitals.\n\n"
            "Tap 📎 → Location → Send Current Location"
        )
        return Response(content=str(resp), media_type="application/xml")

    # 🧠 Normal routing
    answer = route_query(incoming_msg)

    msg.body(answer)

    return Response(content=str(resp), media_type="application/xml")