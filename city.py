import requests
from bs4 import BeautifulSoup

def fetch_college_urls(city):
    city = city.replace(" ", "+")  # Prepare city for URL query
    search_url = f"https://www.google.com/search?q=colleges+in+{city}"
    
    # Set a User-Agent to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    # Make a request to the search URL
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return f"Failed to fetch data (status code {response.status_code})"
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract links from the search results
    links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag['href']
        if "/url?q=" in href and "google.com" not in href:
            url = href.split("/url?q=")[1].split("&")[0]
            links.append(url)
    
    # Filter out duplicates
    links = list(set(links))
    
    return links

# Input from the user
user_city = input("Enter the city name: ")
urls = fetch_college_urls(user_city)

# Output the result
if urls:
    print(f"Colleges in {user_city.title()}:")
    for url in urls:
        print(f" - {url}")
else:
    print(f"No results found for {user_city}.")
