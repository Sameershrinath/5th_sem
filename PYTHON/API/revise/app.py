import streamlit as st
import requests
import time
url = "http://127.0.0.1:8000"

st.header("API Application")

# Display greeting from server
opening = requests.get(url).json()
st.text(opening["Message"])

# -------------------- Show users --------------------
st.subheader("Show Users")
if st.button("Show Users"):
    data = requests.get(url + "/show_user").json()
    if data["User"]:
        for user in data["User"]:
            st.text(user)
    else:
        st.text("No user found on server")

st.markdown("---")

# -------------------- Add user --------------------
st.subheader("Add User")
stu_name = st.text_input("Enter name of student")
if st.button("Send User"):
    if stu_name:
        response = requests.post(url +"/name",params={"user_name":stu_name})
        st.text(response.json()["Submitted"])
    else:
        st.text("Please enter a name")

st.markdown("---")

# -------------------- Scrape links --------------------
st.subheader("Scrape Links")
link_input = st.text_input("Enter any website URL")

# Use session state to prevent multiple POST requests
if 'scrape_started' not in st.session_state:
    st.session_state.scrape_started = False

if st.button("Start Scraping"):
    if link_input:
        requests.post(url + f"/scrap_links",params={"link_url": link_input})
        st.session_state.scrape_started = True
        st.text(f"Scraping started for {link_input}")
    else:
        st.text("Please enter a valid URL")

# Show scraped links after scraping
if st.session_state.scrape_started:
    time.sleep(30)
    st.subheader("Scraped Links")
    response = requests.get(url + "/show_links").json()
    links = response.get("links", [])
    for link in links:
        st.text(link)
