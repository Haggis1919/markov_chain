import requests
from markov_python.cc_markov import MarkovChain
from bs4 import BeautifulSoup


# mc=MarkovChain()
# mc.generate_text()

# A simple test message to prove that am not fumbling in the snake filled dark.
print ("Hello Markov Chain Maker!")

#  This section gets the html info from a lyric site.
r = requests.get('http://www.lyrics.com/do-i-wanna-know-lyrics-arctic-monkeys.html')
soup = BeautifulSoup(r.content, "html.parser")

# This section pulls out the lyrics and puts into a list
rough=soup.find_all(itemprop='description')
results = list(map(str, rough[0].contents))
stripped_results = []
for line in results[:-5]:
    if line != "<br/>":
        if line:
            stripped_results.append(line.strip())
song1 =''.join(stripped_results)

r2 = requests.get('http://www.lyrics.com/r-u-mine-lyrics-arctic-monkeys.html')
soup = BeautifulSoup(r2.content, "html.parser")

# This section pulls out the lyrics and puts into a list
rough=soup.find_all(itemprop='description')
results2 = list(map(str, rough[0].contents))
stripped_results2 = []
for line in results2[:-5]:
    if line != "<br/>":
        if line:
            stripped_results2.append(line.strip())
song2 =''.join(stripped_results2)


print ("*** New song with more Cowbell!",)
#print (stripped_results2)


mc=MarkovChain()
mc.add_string(song1)
mc.add_string(song2)
x =mc.generate_text()
x = ' '.join(x)
print(x)
#  This section pulls out the breaks
# new_rough = rough.replace("<br/>", "")


# print(new_rough)

# This printed the lyrics but included div class and <br>  print(soup.find_all(itemprop='description'))
# This found null print(soup.find_all('lyrics'))
# from jerry.  Said worked on 2.7  --  print ("".join(map(str, div.contents)))
#div = soup.find('div', id='lyrics')
#soup = BeautifulSoup(r.content, builder=HTMLParserTreeBuilder())

#rough=soup.find_all(itemprop='description')
#print(''.join(map(str, rough[0].contents)))
# trying someting new --rough=str(soup.find_all(itemprop='description'))
