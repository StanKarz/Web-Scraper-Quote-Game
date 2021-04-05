# Web Scraper Quote Game

This Python Project scrapes data from the url https://quotes.toscrape.com/, to avoid sending too many requests and scraping the entire website each time for quotes, all the quotes along with the author and their bio link are written to a CSV file, this is the purpose of the file csv_scraper.py. The file csv_quote_game.py reads the contents of the CSV file and runs the guessing game, if a user enters a wrong answer the url is scraped and author's birth place and date are extracted and given as a hint, other hints include the author's initials which are obtained by reading the CSV file and extracting the relevant data. 

### Prerequisites

This project relies on the requests, BeautifulSoup, random and csv libraries. As the csv and random libraries are already built in, you won't have to install them. BeautifulSoup is
the library that will provide us with the functionality to pull data out of the HTML file. 

### Installing

The following command can be used to install the requests library

```
$ python -m pip install requests
```
The following command can be used to install BeautifulSoup

```
$ apt-get install python3-bs4 
```
## Built With

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#) - Used to scrape data from HTML and XML files 
* [Requests](https://pypi.org/project/requests/) - Used to send HTTP requests to webpages
* [CSV](https://docs.python.org/3/library/csv.html) - Used to read and write data in the CSV (comma separated values) format
* [Random](https://docs.python.org/3/library/random.html) - Used to randomly select data
