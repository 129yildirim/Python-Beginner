from urllib import request


goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1656604153&period2=1688140153&interval=1d&events=history&includeAdjustedClose=true'


def download(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    #'r' stands for 'raw': allows to use all characters in the string after it examp: backslashes 
    dest_url = r'goog.cvs'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + "\n")

    fx.close()

download(goog_url)




