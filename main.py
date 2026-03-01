from fastapi import FastAPI
from whatsapp import router as whatsapp_router

app = FastAPI()

# Include WhatsApp route
app.include_router(whatsapp_router)

@app.get("/")
def home():
    return {"status": "Medical AI WhatsApp Bot Running 🚀"}