from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, RegexpTokenizer


def removeStopWords(text):

    stop_words = set(stopwords.words('english'))

    wordTokens = word_tokenize(text)
    filteredSentence = []

    for word in wordTokens:
        if word not in stop_words:
            filteredSentence.append(word)

    newText = " ".join(filteredSentence)

    return newText


def removePunctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    textList = tokenizer.tokenize(text)
    newText = " ".join(textList)
    return newText


removeStopWords('Checking or savings account')
