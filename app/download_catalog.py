import requests

url = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

response = requests.get(url)

with open("data/shl_catalog.json", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Catalog downloaded successfully!")