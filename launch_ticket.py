import requests
import webbrowser

message = input("What do you need help with? ")

# Call your MCP agent
response = requests.post(
    "http://127.0.0.1:8080/agent",
    json={"message": message}
)

if response.status_code != 200:
    print("Error contacting agent.")
    exit()

data = response.json()

if data["status"] != "ok":
    print("Could not understand the request.")
    exit()

print("\n✅ Ticket Type:", data["ticket_type"])
print("🔗 Opening ticket form:", data["ticket_url"])
print("📝 Suggested Field Values:")
for k, v in data["prefilled_fields"].items():
    print(f"  - {k}: {v}")

# Open the form in browser
webbrowser.open(data["ticket_url"])
