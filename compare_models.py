import build_model as build
import json


def compareModels(file1, file2):
    build.build_model(file1, "model1")
    build.build_model(file2, "model2")
    json_file1 = open('model1')
    model1 = json.load(json_file1)

    json_file2 = open('model2')
    model2 = json.load(json_file2)
    totalCount = len(model1.keys())

    score = 0
    for word1 in model1.keys():
        count1 = model1[word1]
        count2 = 0
        if word1 in model2.keys():
            count2 = model2[word1]
        score += abs(count1 - count2)
    mean = score / totalCount
    return score, mean