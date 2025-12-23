import requests as req


url="https://dummyjson.com/products"

response=req.get(url)
print(response)
print(response.json())
print(response.status_code)