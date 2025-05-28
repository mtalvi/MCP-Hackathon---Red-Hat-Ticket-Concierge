from llamastack.tools import Tool
import json
import os

class TicketLookupTool(Tool):
    name = "lookup_ticket"
    description = "Finds the correct Red Hat internal ticket form based on a natural language request."

    def __init__(self):
        super().__init__()
        # Load tickets.json relative to project root
        path = os.path.join(os.path.dirname(__file__), "../tickets.json")
        with open(path) as f:
            self.catalog = json.load(f)

    def run(self, input: str) -> dict:
        text_lower = input.lower()
        for key, data in self.catalog.items():
            for kw in data["keywords"]:
                if kw in text_lower:
                    return {
                        "ticket_type": key,
                        "url": data["url"],
                        "fields": data["fields"]
                    }
        return {
            "error": "Could not classify input."
        }
