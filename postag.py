from nltk import pos_tag  
from nltk.tokenize import word_tokenize  
  
text = "This is an example sentence."  
words = word_tokenize(text)  
pos = pos_tag(words)  
print(pos)  