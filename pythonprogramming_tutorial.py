from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

example_sentence = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words("english"))

word_tokens = word_tokenize(example_sentence)

filtered_sentence = [w for w in word_tokens if w not in stop_words]

#for w in word_tokens:
#    if w not in stop_words:
#        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)