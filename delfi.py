from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all("div", class_="C-block-type-102-headline__content")
with open("delfi_straipsniai.csv", 'w', encoding="utf-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Antraštė", 'Kategorija', 'Nuoroda'])

    for blokas in blokai:
        kategorija = blokas.a.text.strip()
        antraste = blokas.find_all("a")[1].text.strip()
        nuoroda = blokas.find_all("a")[1]['href']
        csv_writer.writerow([antraste, kategorija, nuoroda])