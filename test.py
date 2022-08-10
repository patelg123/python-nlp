import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


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
        
print(filtered_list)