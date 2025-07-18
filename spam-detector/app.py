import nltk
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
text = "This is a boy"

text = word_tokenize(text)

print(text)