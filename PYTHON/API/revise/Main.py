from fastapi import FastAPI, BackgroundTasks
from bs4 import BeautifulSoup
import requests

app = FastAPI()

# Global lists to store users and links
users = []
link_storage = []

# Function to scrape links in the background
def scrape_task(link_url: str):
    global link_storage
    try:
        response = requests.get(link_url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        link_storage = [i['href'] for i in links if i['href']]
    except Exception as e:
        link_storage = []
        print(f"Error scraping {link_url}: {e}")

# Home endpoint
@app.get("/")
def greet():
    return {"Message": "Hello from the developer"}

# Store user endpoint
@app.post("/name",)
def store_name(user_name: str):
    users.append(user_name)
    return {"Submitted": user_name}

# Show all users
@app.get("/show_user")
def show_user():
    return {"User": users}

# Scrape links in background
@app.post("/scrap_links")
def scrapper_link_endpoint(link_url: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(scrape_task, link_url)
    return {"message": f"Scraping started for {link_url}"}

# Show scraped links
@app.get("/show_links")
def print_links():
    if link_storage:
        links_list = [f"{idx+1} - {link}" for idx, link in enumerate(link_storage)]
        return {"links": links_list}
    else:
        return {"links": ["nahi hai"]}
