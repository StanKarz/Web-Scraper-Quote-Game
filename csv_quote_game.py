import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader

BASE_URL = "https://quotes.toscrape.com/"

def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

def start_game(quotes):
    quote = choice(quotes)
    guesses_left = 4
    print("Here's a quote: ")
    print(quote["text"])
    print(quote["author"])
    guess = ''
    while guess.lower() != quote["author"].lower() and guesses_left > 0:
        guess = input(f"Who is this quote by? Guesses Remaining: {guesses_left} \n")
        if guess.lower() == quote['author'].lower():
            print(f"You got it right!")
            break
        guesses_left -= 1
        if guesses_left == 3:
            res = requests.get(f"{BASE_URL}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
        elif guesses_left == 2:
            print(f"Here's another hint: The author's first name starts with {quote['author'][0]}")
        elif guesses_left == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Your final hint is: The author's last name begins with {last_initial}")
        else:
            print(f"Sorry you ran out of guesses the answer was {quote['author']} ")

    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)? \n")
    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print("Okay, Goodbye!")

quotes = read_quotes("quotes.csv")
start_game(quotes)