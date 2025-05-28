from fastapi import FastAPI, Request
import json

app = FastAPI()

# Load the ticket catalog at startup
with open("tickets.json") as f:
    TICKETS = json.load(f)

# Match user input to ticket type
def classify_request(text: str) -> str:
    text_lower = text.lower()
    for key, data in TICKETS.items():
        for kw in data["keywords"]:
            if kw in text_lower:
                return key
    return "unknown"

@app.post("/agent")
async def handle_request(request: Request):
    body = await request.json()
    user_input = body.get("message", "")

    ticket_type = classify_request(user_input)

    if ticket_type == "unknown":
        return {
            "status": "not_found",
            "message": "Could not classify request. Try rephrasing."
        }

    ticket = TICKETS[ticket_type]
    return {
        "status": "ok",
        "ticket_type": ticket_type,
        "ticket_url": ticket["url"],
        "prefilled_fields": ticket["fields"]
    }
