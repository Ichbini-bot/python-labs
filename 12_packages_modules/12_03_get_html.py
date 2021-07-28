'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!

pip install beautifulsoup4 => as I did not create a venv, its globally available
to uninstall: pip uninstall beautifulsoup4 (whatch out: beautifulsou4 comes with soupsieve - so one would uninstall this as well)

'''
import urllib.request
from bs4 import BeautifulSoup as bs

wiki = "https://www.maler-scheuber.ch/"
page = urllib.request.urlopen(wiki)
soup = bs(page)

print(soup)
print(soup.title)


