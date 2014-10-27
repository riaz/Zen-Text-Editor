from nltk.corpus import wordnet
for word_meaning in wordnet.synsets('abrogate'):
        for syn in word_meaning:
                print syn
