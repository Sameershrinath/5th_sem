import requests

url = "http://127.0.0.1:8000"


response = requests.get(url)
add_response = requests.get(url=url+"/add/5/5")
multiply_response = requests.get(url=url+"/multiply/5/5")
listf={"msg":"how are you"}
uploaddata = requests.post(url=url+"/check",json=listf)
download_data=requests.get(url+"/check2")

print("Response from API:", response.json())
print(add_response.json())
print(multiply_response.json())
print(download_data.json())