import nltk
##nltk.download('punkt')

from nltk.tokenize import sent_tokenize, word_tokenize
lines = ""
with open('c:\\Anu\\Learning\\Python\\HomeProject\\CactusRattlers.txt', encoding='utf8') as f:
    for line in f:
        lines += line.strip()
        ##print(line.strip())
##print(lines)

##print(sent_tokenize(lines))
print(word_tokenize(lines))