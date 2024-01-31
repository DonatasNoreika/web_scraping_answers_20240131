
from random import choice
import pickle

with open("quotes.pkl", 'rb') as file:
    quotes = pickle.load(file)


random_quote = choice(quotes)

print(random_quote['quote'])
answer1 = input("Kas yra šios citatos autorius?")
if answer1 == random_quote['author']:
    print("Sveikiname, atspėjote")
else:
    print("Autoriaus inicialai:", " ".join(f"{name[0]}." for name in random_quote['author'].split()))
    answer2 = input("Kas yra šios citatos autorius?")
    if answer2 == random_quote['author']:
        print("Sveikiname, atspėjote")
    else:
        print("Gimė:", random_quote['born'])
        answer3 = input("Kas yra šios citatos autorius?")
        if answer3 == random_quote['author']:
            print("Sveikiname, atspėjote")
        else:
            print(f"Neatspėjote, autorius: {random_quote['author']}")
