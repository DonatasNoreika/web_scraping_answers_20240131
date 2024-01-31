from bs4 import BeautifulSoup
import requests
from random import choice
import pickle

quotes = []

quotes_url = "https://quotes.toscrape.com/"

counter = 1

while True:
    print("Page:", counter)
    r_text = requests.get(f"{quotes_url}/page/{counter}/").text

    if r_text.find("No quotes found!") > 0:
        print("Daugiau puslapių nėra")
        break
    soup = BeautifulSoup(r_text, 'html.parser')

    blokai = soup.find_all("div", class_="quote")

    for blokas in blokai:
        quote = blokas.find("span", class_="text").get_text()
        author = blokas.find("small", class_="author").get_text()

        url = blokas.find("small", class_="author").find_next_sibling()['href']
        r_author = requests.get(f"{quotes_url}{url}").text
        soup_author = BeautifulSoup(r_author, "html.parser")
        born = soup_author.find('h3', class_='author-title').find_next_sibling().get_text()
        print(quote, author)
        quotes.append({"quote": quote, "author": author, "born": born})
    counter += 1

with open('quotes.pkl', 'wb') as file:
    pickle.dump(quotes, file)
