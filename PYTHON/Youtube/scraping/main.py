import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://pmc.ncbi.nlm.nih.gov/articles/PMC5587110/"

# Add headers to look like a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

# Send HTTP request with headers
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract content with id="main-content"
    main_content = soup.find(id="main-content")
    
    if main_content:
        # Get clean text
        text_data = main_content.get_text(separator="\n", strip=True)
        
        # Save to file
        with open("scraped_content.txt", "w", encoding="utf-8") as f:
            f.write(text_data)
        
        print("Data successfully saved in scraped_content.txt")
    else:
        print("No element with id='main-content' found.")
else:
    print("Failed to retrieve webpage. Status code:", response.status_code)
