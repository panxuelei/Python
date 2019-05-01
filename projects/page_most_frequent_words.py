# https://www.geeksforgeeks.org/python-program-crawl-web-page-get-frequent-words/
# Program to crawl a web page and get most frequent words
'''
requests : Will allow you to send HTTP/1.1 requests and many more.
beautifulsoup4 : For pulling data out of HTML and XML files.
operator : Exports a set of efficient functions corresponding to the intrinsic operators.
collections : Implements high-performance container datatypes.
'''

# Python3 program for a word frequency counter
# after crawling a web-page
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def start(url):
    wordlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')

    for eace_text in soup.findAll('div', {'class':'entry-content'}):
        content = eace_text.text
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()|\;:"<>?/., '
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    c = Counter(word_count)
    top = c.most_common(2)
    print(top)

if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/programming-language-choose')