# Web Scraper Quote Game

This Python Project scrapes data from the url https://quotes.toscrape.com/, to avoid sending requests to the website each time the code is executed the relevant data 
is written to a CSV file and a quote is selected at random. The user has 4 attempts to guess the author of the quote, each time a wrong answer is provided the
user will receive a hint about the author such as their birth data, birth place or initials. 

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
* [Request](https://pypi.org/project/requests/) - Used to make requests to url's
* [CSV](https://docs.python.org/3/library/csv.html) - Used to read and write data in the CSV (comma separated values) format
* [Random](https://docs.python.org/3/library/random.html) - Used to randomly select a quote from a list of quotes
