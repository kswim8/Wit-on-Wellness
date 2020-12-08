
from triestructure import *
from nltk.corpus import wordnet as wn
food = wn.synset('food.n.02')
foodcorpus = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))

keys = foodcorpus 
output = ["Not present in trie", 
        "Present in trie"] 

# Trie object 
t = Trie() 

# Construct trie 
for key in keys: 
    t.insert(key) 

# Search for different keys 
print("{} ---- {}".format("the",output[t.search("the")])) 
print("{} ---- {}".format("these",output[t.search("these")])) 
print("{} ---- {}".format("their",output[t.search("their")])) 
print("{} ---- {}".format("ther",output[t.search("ther")]))