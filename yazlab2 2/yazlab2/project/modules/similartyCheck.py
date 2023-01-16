from modules.stringOperations import removePunctuation, removeStopWords


def similarityCheck(text1, text2, similarityRate):
    if text1 == text2:
        text1 = removeStopWords(removePunctuation(text1)).replace("/", "")
        return (1.0, text1, text1)

    else:
        text1 = removeStopWords(removePunctuation(text1)).replace("/", "")
        text2 = removeStopWords(removePunctuation(text2)).replace("/", "")
        words1 = text1.lower().split()
        words2 = text2.lower().split()

        listOfIntersection = [
            word for word in words1 if word in words2]

        if len(words1) > len(words2):
            wordCount = len(words1)

        else:
            wordCount = len(words2)
        tuples = (float(len(listOfIntersection)) /
                  wordCount, text1, text2)
        if float(len(listOfIntersection)) / wordCount >= similarityRate:
            return tuples
