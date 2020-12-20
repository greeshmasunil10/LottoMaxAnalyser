#Imports are here
import numpy as np
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup as bs
from datetime import datetime

winning_numbers = []
#for 
page = urllib.request.urlopen("https://www.lottomaxnumbers.com/numbers/2020")
soup = bs(page,features="lxml")
 
draws = soup.body.findAll('ul', attrs={'class': 'balls'})

for numbers in draws:
    numbers = numbers.text
    numbers = numbers.split('\n')
    numbers=numbers[1:-1]
    winning_numbers.append(numbers)
