print("Analysing..")
import urllib.request
from bs4 import BeautifulSoup as bs
import datetime

winning_numbers = []
draw_dates =[]
sums =[]
dateobjs=[]
draw_dict={}
sum_dict={}

start=2020
end=2022

for x in range(start,end):
    page = urllib.request.urlopen("https://www.lottomaxnumbers.com/numbers/"+str(x))
    soup = bs(page,features="lxml")
    draws = soup.body.findAll('ul', attrs={'class': 'balls'})
    dates = soup.body.findAll('a', attrs={'class': 'archive-date-link'})
    
    for i in range(len(draws)):
        numbers=draws[i]
        numbers = numbers.text
        numbers = numbers.split('\n')
        numbers=numbers[1:-2]
        numbers = [int(i) for i in numbers]     
        winning_numbers.append(numbers)
        date=dates[i]
        date = date.text   
        draw_dates.append(date)
        date_time_obj = datetime.datetime.strptime(date, '%B %d %Y').date()
        dateobjs.append(date_time_obj)
        draw_dict[date_time_obj]=numbers
        
draw_dict=dict(sorted(draw_dict.items()));      
        
def get_timestamp(dateTimeObj):
    return dateTimeObj.strftime("%d-%b-%Y")
       
with open('draws.txt', 'w') as f:
    for key,value in draw_dict.items():
        f.write("%s " % get_timestamp(key))
        f.write("%s\n" % value)

import collections
counts = collections.Counter()
for sublist in winning_numbers:
    counts.update(sublist)
    
    
def print_draws():
    for key,value in draw_dict.items():
        print(value,end="")
        print(" "+get_timestamp(key))
    
for i in range(len(winning_numbers)):
    sum=0
    for j in range(len(winning_numbers[i])):
        sum+=winning_numbers[i][j]
    sums.append(sum)
    sum_dict[dateobjs[i]]=sum

sum_dict=dict(sorted(sum_dict.items())); 

draw_dates.reverse()
sums.reverse()

import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize = (len(draw_dict.keys()), 10)) 
plt.title("Lotto Max Draws in "+str(start)) 
dates=list(draw_dict.keys())
x = [get_timestamp(x) for x in dates]
y=list(draw_dict.values())
plt.xticks(rotation=90)
sx=range(1,51)
plt.yticks(np.arange(min(sx), max(sx)+1, 1.0))
#plt.yticks(np.arange(min(y), max(y)+1, 1.0))
#plt.plot(draw_dates,winning_numbers,marker='o',markerfacecolor="black")
for i in range(7):
    for x1,y1 in zip(x,y):
        label = "{:.2f}".format(y1[i])
        plt.annotate(label, 
                     (x1,y1[i]), 
                     textcoords="offset points", 
                     xytext=(0,10),
                     ha='center')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='x', alpha=0.7)
plt.plot(x, y,marker='o')
plt.savefig('drawfig.png')



import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize = (len(draw_dates)/2, 10)) 
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='x', alpha=0.7)
plt.xticks(rotation=90)
plt.yticks(np.arange(len(y)))
plt.title("Lotto Max Draw Sums in "+str(start)) 
for x,y in zip(draw_dates,sums):

    label = "{:.2f}".format(y)

    plt.annotate(label,
                 (x,y), 
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center')
plt.plot(draw_dates,sums,marker='o',color="red",markerfacecolor="black")
plt.savefig('SumGraph.png')



print("Most Common Numbers drawn")
print(counts.most_common())
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize = (len(counts.keys())/2, 10)) 
x=list(counts.keys())
y=list(counts.values())
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.title("LottoMax Number Frequency in "+str(start)) 
plt.xlabel("Number") 
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
for i in range(len(y)):
    plt.annotate(str(y[i]), xy=(x[i],y[i]), ha='center', va='bottom')
plt.bar(x, y,align='center',edgecolor = 'red')
plt.savefig('frequencygraph.png')

print("Stats Completed!")