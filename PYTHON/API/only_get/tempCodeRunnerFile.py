efine the API URL (add quotes to make it a string)
url = "http://127.0.0.1:8000"


# Send GET request to root endpoint and get response
response = requests.get(url)

# Display the response
st.write("Response from API:", response.json())