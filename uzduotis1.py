from bs4 import BeautifulSoup
import requests
from random import shuffle

bad_words = ['COVID', 'mirt', 'NVSC', 'skiep', "karas"]

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all("div", class_="C-block-type-102-headline__content")

first_parts = []
second_parts = []

for blokas in blokai:
    antraste = blokas.find_all("a")[1].text.strip()
    if ":" in antraste:
        if not any(word in antraste for word in bad_words):
            splitted = antraste.split(":")
            first_parts.append(splitted[0])
            second_parts.append(splitted[1])

shuffle(second_parts)

for i in range(len(first_parts)):
    print(f"{first_parts[i]}:{second_parts[i]}")