#web scrapper script
from bs4 import BeautifulSoup
import requests

url = 'https://www.natural-beauty.com.mx/MLM-2165880363-afrodita-baja-de-peso-_JM#item_id=MLM2165880363&component=tabbed_carrousel&page_from=home&custom_categories=false&promotions=false'

# Fetch the webpage
response = requests.get(url)
doc = BeautifulSoup(response.text, "html.parser")
prices = doc.find_all(text="1,199")
parent = prices[0].parent
print(parent)
andes money