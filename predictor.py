import numpy as np
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup as bs
from datetime import datetime

winning_numbers = []
test_numbers =[]
all_numbers =[]
#wifor 

for x in range(2009,2020):
    page = urllib.request.urlopen("https://www.lottomaxnumbers.com/numbers/"+str(x))
    soup = bs(page,features="lxml")
    draws = soup.body.findAll('ul', attrs={'class': 'balls'})
    
    for numbers in draws:
        numbers = numbers.text
        numbers = numbers.split('\n')
        numbers=numbers[1:-2]
        numbers = [int(i) for i in numbers] 
        winning_numbers.append(numbers)
        

page2 = urllib.request.urlopen("https://www.lottomaxnumbers.com/numbers/2020")
soup2 = bs(page2,features="lxml")
draws2 = soup2.body.findAll('ul', attrs={'class': 'balls'})

for numbers in draws2:
    numbers = numbers.text
    numbers = numbers.split('\n')
    numbers=numbers[1:-2]
    numbers = [int(i) for i in numbers] 
    test_numbers.append(numbers)
    
        
total_balls =len(winning_numbers)*7
 


import itertools     
from itertools import *
import collections
counts = collections.Counter()
for sublist in winning_numbers:
    counts.update(sublist)
    
    
def get_probability(number):
    return counts[number]/total_balls


sum=0
total=0
for i in range(1,51):
#    print(i)
    prob=get_probability(i)
    print(i,":",round(prob*100,3))
    
    
def train_set():
    for i in winning_numbers:
        print(i,end="")
        buyprob=0    
        for j in i:
            buyprob+=get_probability(j)
        print(" :",end="")
        print(round(buyprob*100,2))
    

def test_set():
    for i in test_numbers:
        print(i,end="")
        buyprob=0    
        for j in i:
            buyprob+=get_probability(j)
        print(" :",end="")
        print(round(buyprob*100,2),end="")
        if (buyprob*100)> 13:
            print(" won")
        else:
            print(" lost")

print("train")
train_set()

print("test")
test_set()



buy =[9,10,12,19,24,26,33]

#for i in range(1,8):
#    buy.append(int(input("enter "+str(i)+ "th number")))
    
buyprob=0    
for i in buy:
    buyprob+=get_probability(i)

print("Your chance of winning is:"+str(round(buyprob*100,2))+"%!")
    

X = np.array(winning_numbers)
Y=np.full(len(X), 1)
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
#print(clf.predict([[-0.8, -1]]))
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
GaussianNB()
#print(clf_pf.predict([[-0.8, -1]]))
buy=[]
for i in range(1,8):
    buy.append(int(input("enter "+str(i)+ "th number")))
print(clf.predict([buy]))