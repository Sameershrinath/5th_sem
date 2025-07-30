import requests

url = "http://127.0.0.1:8000"


response = requests.get(url)
add_response = requests.get(url=url+"/add/5/5")
multiply_response = requests.get(url=url+"/multiply/5/5")

print("Response from API:", response.json())
print(add_response.json())
print(multiply_response.json())