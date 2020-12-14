import re
import json


def getWithoutStopWords(file):
    try:
        f = open("StopWords", "r")
        stop = f.read().split('\n')
        f2 = open(file, "r")
        words = re.findall(re.compile('\w+'), f2.read().lower())
        extracted_words = [w for w in words if w not in stop]
        return extracted_words
    except Exception as e:
        print(e)


def buildJson(data, file):
    with open(file, 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()


def build_model(textFile, modelFile):
    try:
        text = getWithoutStopWords(textFile)
        textSet = set(text)
        model = dict()
        numberOfWords = len(text)
        for w in textSet:
            count = text.count(w) / numberOfWords * 1000000
            model[w] = count
        buildJson(model, modelFile)
    except Exception as e:
        print(e)
