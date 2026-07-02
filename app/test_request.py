import requests

url = "https://www.shl.com/solutions/products/product-catalog/"

response = requests.get(url)

print("Status Code:", response.status_code)
print(response.text[:1000])