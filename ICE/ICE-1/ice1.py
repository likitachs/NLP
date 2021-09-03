import urllib.request
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

#Using SpaceX wikipedia page URL to grab the data

response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html =  response.read()

#Using Beautiful Soup to clean the grabbed text
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip = True)
tokens = [t for t in text.split()]
clean_tokens = tokens[:]

#Calculating the frequency distribution of tokens using NLTK
frequency = nltk.FreqDist(tokens)
keys =[]
values = []

for key,val in frequency.items():
    #Printing Values whose frequency is greater than 5
    if val>5:
        print(str(key) + ':' +str(val))
        keys.append(key)
        values.append(val)
    else:
        tokens.remove(key)

#Plotting a graph using the tokens
frequency.plot(20,cumulative= False)

#Removing stop words using NLPK
for token in tokens:
    #Removing Tokens that have digits
    if str(token).isdigit():
        clean_tokens.remove(token)
    #Removing English language Stopwords
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

#Calculating the frequency distribution of tokens using NLTK after removing stopwords
final = nltk.FreqDist(clean_tokens)

#Plotting the graph with first 10 high distribution words
final.plot(10,cumulative= False)

#Plotting different visualization for frequency distribution - Bar Graph
plt.bar(keys[0:10], values[0:10], color='blue')
plt.show()



