import requests 
from bs4 import BeautifulSoup #importing BeautifulSoup from bs4 module
# URL of the webpage to scrape
# BeautifulSoup is a Python library used for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.
# It provides Pythonic idioms for iterating, searching, and modifying the parse tree.
# It is commonly used for web scraping tasks to extract information from web pages.
# Example usage: just like below
url="https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

for quote, author in zip(quotes, authors):
    print(f'Quote: {quote.text} - Author: {author.text}')

    for tag in quote.find_all('a', class_='tag'):
        print(f'Tag: {tag.text}')