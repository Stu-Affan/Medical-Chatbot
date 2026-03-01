

---

#  AI Medical Assistant (WhatsApp Enabled)

An intelligent **AI-powered medical support assistant** designed to provide:

* Symptom understanding
* Drug information
* Medical knowledge
* Nearby hospital discovery

All accessible directly through **WhatsApp**.

Built using:

* FastAPI 
* LangChain 
* MedGemma / LLM routing
* Twilio WhatsApp API 
* Google Places API 
* Retrieval-Augmented Generation (RAG)

---

#  Project Objective

The goal of this project is to build a **safe, structured medical assistant** that:

✔ Understands user symptoms
✔ Suggests possible causes
✔ Recommends basic remedies
✔ Provides drug-related insights
✔ Locates nearby hospitals using real-time location
✔ Detects emergencies and prioritizes safety

Unlike generic chatbots, this system follows a **deterministic medical routing architecture** to ensure appropriate responses.

---

#  System Architecture

```
User (WhatsApp)
      ↓
Twilio Webhook
      ↓
FastAPI Backend
      ↓
Medical Router
 ┌───────────────┬──────────────┬───────────────┬──────────────┐
 │ Symptoms      │ Drugs        │ Hospitals     │ General Info │
 │ Analysis Tool │ Drug Tool    │ Finder Tool   │ RAG Engine   │
 └───────────────┴──────────────┴───────────────┴──────────────┘
      ↓
Safe Medical Response
```

---

#  Core Features

## 1. Symptom Analysis Engine

* Accepts natural language symptoms
* Suggests:

  * Possible causes
  * Home remedies
  * When to seek medical help

Example:

> “I have swelling in my knee”

 Response includes:

* Possible causes
* Remedies
* Medical warning signs

---

## 2. Drug Intelligence

Provides structured insights such as:

* Uses
* Side effects
* Safety considerations

Example:

> “What is Ibuprofen?”

---

## 3. Emergency Detection Layer

Detects high-risk inputs like:

* Chest pain
* Stroke symptoms
* Breathing difficulty

And immediately prioritizes hospital discovery.

---

## 4. WhatsApp Hospital Finder 

Users can:

1. Ask:

   > “Find hospitals near me”

2. Share live location

3. Receive:
   ✔ Nearby hospitals
   ✔ Address
   ✔ Ratings

Powered by **Google Places API**

---

## 5. Medical Knowledge Engine (RAG)

Provides reliable educational explanations for:

* Diseases
* Conditions
* Treatments

---

#  WhatsApp Integration

This assistant works directly via WhatsApp using:

* Twilio Sandbox
* FastAPI Webhooks
* ngrok for tunneling

Users can interact naturally like:

```
Hi
I have fever and headache
Find hospitals near me
What is paracetamol?
```

---

#  Tech Stack

| Layer             | Technology          |
| ----------------- | ------------------- |
| Backend           | FastAPI             |
| LLM Orchestration | LangChain           |
| Messaging         | Twilio WhatsApp API |
| Location Services | Google Places API   |
| AI Reasoning      | MedGemma            |
| Search            | Vector RAG          |
| Deployment        | ngrok (dev)         |

---

#  Safety Considerations

* Emergency detection built-in
* Educational use only
* Encourages professional consultation when needed

---

#  Project Structure

```
medical-chatbot/
│
├── main.py
├── router.py
├── whatsapp.py
├── safety.py
│
├── tools/
│   ├── medical_rag_tool.py
│   ├── drug_tool.py
│   ├── symptom_tool.py
│   ├── hospital_finder.py
│
├── vectorstore/
├── data/
│
├── .env (not committed)
└── README.md
```

---

# ⚠️ Disclaimer

This system is intended for **educational purposes only** and does not replace professional medical advice.
