import re
import requests
# import nltk
from bs4 import BeautifulSoup
def word_tokenize(someText):
        tokenList = []
        tokens = re.split('([^a-zA-Z0-9@#*&\'])', someText)
        for token in tokens:
            token = token.lower()
            if token != " " and token != "" and len(token) > 1:
                if len(token) == 1 and not ord(token) < 128:
                    continue
                tokenList.append(token)
        return tokenList
url = "https://www.ics.uci.edu/"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
output = []
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
]
for t in text:
    if t.parent.name not in blacklist and format(t) != "\n":
        print(t.parent.name)
        list = word_tokenize(format(t))
        if list:
            for word in list:
                output.append(word)
print(output)

