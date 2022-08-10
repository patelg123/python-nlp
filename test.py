from re import X
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from porter2stemmer import Porter2Stemmer

worf_quote = "Sir, I protest. I am not a merry man!"

words_in_quote = word_tokenize(worf_quote)
#print(words_in_quote);

stop_words = set(stopwords.words("english"))

filtered_list = [
    word for word in words_in_quote if word.casefold() not in stop_words
]

#for word in words_in_quote:
#    if word.casefold() not in stop_words:
#        filtered_list.append(word)
def printlist(list):
    print(list)


#printlist(filtered_list)

stemmer = Porter2Stemmer()

string_for_stemming = """
The crew of the USS Discovery discovered many discoveries.
Discovering is what explorers do."""

words = word_tokenize(string_for_stemming)

stemmed_words = [stemmer.stem(word) for word in words]

printlist(stemmed_words)