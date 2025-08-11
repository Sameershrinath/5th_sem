import requests

url = "https://gfgcdn.com/tu/Vb4/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}
for i in range(1000):
    response = requests.get(url, headers=headers, allow_redirects=True)
    print("Final URL after redirect:", response.url)
    print("Status Code:", response.status_code)
    print(f"the run count is {i}")

