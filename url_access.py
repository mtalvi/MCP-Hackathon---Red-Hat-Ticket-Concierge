import json
import requests

# Load cookies from the exported JSON
with open("cookies.json", "r") as f:
    cookie_list = json.load(f)

# Convert to requests-style cookie dict
cookies = {cookie['name']: cookie['value'] for cookie in cookie_list}

# Your target URL (same as in the browser)
url = "https://redhat.service-now.com/help?id=sc_cat_item&sys_id=ac8b875a82822004c7185ae62325874"

# Send GET request with your cookies
response = requests.get(url, cookies=cookies)

# Output the result (HTML content of the page)
print("Status:", response.status_code)
print(response.text[:1000])  # Preview first 1000 characters
