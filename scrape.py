import requests
from lxml import html

def scrape_value(url, xpath):
    # Send GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return None
    
    # Parse the HTML content using lxml
    tree = html.fromstring(response.content)
    
    # Use XPath to find the desired element
    result = tree.xpath(xpath)
    
    # If the result is found, return it
    if result:
        return result[0].text.strip() if result[0].text else "No text content"
    else:
        return "No element found with the given XPath"

# Example usage:
url = input("Enter the URL: ")
xpath = input("Enter the XPath: ")

value = scrape_value(url, xpath)
print("Scraped Value:", value)
