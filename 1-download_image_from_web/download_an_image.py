import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


download_web_image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Morrell.jpg/800px-Morrell.jpg")






    