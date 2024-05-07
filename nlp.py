import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "NLP text"

stop_words = set(stopwords.words('english'))
words = word_tokenize(text.lower())
filtered_words = [word for word in words if word not in stop_words]

print(filtered_words)
