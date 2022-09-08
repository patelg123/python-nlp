import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from porter2stemmer import Porter2Stemmer
from nltk.stem import WordNetLemmatizer
import tkinter


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
    for element in list:
        print (element)

#printlist(filtered_list)

stemmer = Porter2Stemmer()

string_for_stemming = """
The crew of the USS Discovery discovered many discoveries.
Discovering is what explorers do."""

words = word_tokenize(string_for_stemming)

stemmed_words = [stemmer.stem(word) for word in words]

#printlist(stemmed_words)


sagan_quote = """
If you wish to make an apple pie from scratch
you must first invent the universe."""

sagan_quote_words = word_tokenize(sagan_quote)

#printlist(nltk.pos_tag(sagan_quote_words))

jabberwocky_excerpt= """"
'T was brillig, and the slithy toves did gyre and gimble in the wabe:
all mimsy were the borogoves, and the mome raths outgrabe."""

jabberwocky_excerpt_words = word_tokenize(jabberwocky_excerpt)

#printlist(nltk.pos_tag(jabberwocky_excerpt_words))

lemmatizer = WordNetLemmatizer()

string_for_lemmatizing = "The worst friends of DeSoto love scarves"

words_for_lemmatizing = word_tokenize(string_for_lemmatizing);

lemmatized_words = [lemmatizer.lemmatize(word, pos="a") for word in words_for_lemmatizing]

#lemmatized_words = []
#for word in words_for_lemmatizing:
#    lemmatized_words.append(lemmatizer.lemmatize(word))
    

#printlist(lemmatized_words)

lotr_quote = "It's a dangerous business, Frodo, going out your door."

words_in_lotr_quote =  word_tokenize(lotr_quote);

#printlist(words_in_lotr_quote)

lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)

#printlist(lotr_pos_tags)

grammar = """
Chunk: {<.*>+}
       }<JJ>{"""

chunk_parser = nltk.RegexpParser(grammar)

#tree = chunk_parser.parse(lotr_pos_tags)

tree = nltk.ne_chunk(lotr_pos_tags, binary=True)

#print (tree)


quote = """
Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
for countless centuries Mars has been the star of war—but failed to
interpret the fluctuating appearances of the markings they mapped so well.
All that time the Martians must have been getting ready.

During the opposition of 1894 a great light was seen on the illuminated
part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
and then by other observers. English readers heard of it first in the
issue of Nature dated August 2."""

def extract_ne(quote):
    words = word_tokenize(quote, language='english')
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=False)
    
    tree.draw()
    
    #print (tree)
    results = [];
    
    for t in tree:
        if hasattr(t, "label") and t.label() == "PERSON":
            for i in t:
                results.append(i[0]);    
    
    
    return set(results);
    #return set(
    #    " ".join(i[0] for i in t)
    #    for t in tree
    #    if hasattr(t, "label") and t.label() == "PERSON"
    #)
    
print(extract_ne(quote))










