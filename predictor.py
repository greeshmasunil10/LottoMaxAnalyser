import urllib.request
from bs4 import BeautifulSoup as bs


winning_numbers = []
draw_dates =[]


for x in range(2009,2022):
    page = urllib.request.urlopen("https://www.lottomaxnumbers.com/numbers/"+str(x))
    soup = bs(page,features="lxml")
    draws = soup.body.findAll('ul', attrs={'class': 'balls'})
    dates = soup.body.findAll('a', attrs={'class': 'archive-date-link'})
    
    for numbers in draws:
        numbers = numbers.text
        numbers = numbers.split('\n')
        numbers=numbers[1:-2]
        numbers = [int(i) for i in numbers]     
        winning_numbers.append(numbers)
        
    for numbers in dates:
        numbers = numbers.text   
        draw_dates.append(numbers)
        
        
with open('draws.txt', 'w') as f:
    for i in range(len(winning_numbers)):
        f.write("%s " % winning_numbers[i])
        f.write("%s\n" % draw_dates[i])
 

import collections
counts = collections.Counter()
for sublist in winning_numbers:
    counts.update(sublist)
    
    
def print_draws():
    for i in range(len(winning_numbers)):
        print(winning_numbers[i],end="")
        print(" "+draw_dates[i])

#print("draws")
#print_draws()

print("Most Common Numbers drawn")
print(counts.most_common())

import matplotlib.pyplot as plt
plt.figure(figsize = (20, 10)) 

plt.bar(counts.keys(), counts.values(), align='center',color='cyan', edgecolor = 'red')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.title("Lotto Max Number Frequency") 
plt.xlabel("Number") 
plt.ylabel("Frequency") 
plt.savefig('graph.png')
plt.show()