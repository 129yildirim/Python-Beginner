import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.find_all('a', {'class':'boxStyle color-general hbBoxMainText'}):
        title = str(post_text.get('title'))
        words = title.lower().split()
        for each_word in words:
            word_list.append(each_word)
    
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []    
    for word in word_list:
        symbols = "!'^+%&/()\"\/=?_,.>£#$½{,}[]*+-"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(my_list):
    word_count = {}
    for word in my_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # First of all, the key in the second parameter of sorted func is not the key that is in our list. It is special to the function
    # And with that key we can tell the sorted func that list the items according to this to that to it....
    # operator.itemgetter(1) is getting the value (the value of our list).
    # And Then we are becoming to sort the list according to the value of our list 
    # itemgetter(0) would sort it according to the key
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)






start('https://www.haberler.com/guncel/')