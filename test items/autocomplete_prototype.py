import nltk
nltk.download('brown')

# CITATION: 
# https://stackoverflow.com/questions/19626737/where-can-i-find-a-text-list-or-library-that-contains-a-list-of-common-foods
from nltk.corpus import wordnet as wn
food = wn.synset('food.n.02')
foodcorpus = (set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))


# CITATION:
# https://stackoverflow.com/questions/38233145/nltk-most-common-synonym-wordnet-for-each-word/38234480#38234480
from nltk.corpus import brown
freqs = nltk.FreqDist(w.lower() for w in brown.words())

matchingFoodsList = []

userinput = input("Enter a food/drink: ")
try:
    for aFood in foodcorpus:
        if aFood.startswith(userinput):
            matchingFoodsList.append(aFood)
        if len(matchingFoodsList) >= 20:
            break 
except:
    print("Nothing found")

print(matchingFoodsList)