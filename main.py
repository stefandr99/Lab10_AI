import compare_models as compare

if __name__ == '__main__':
    score, mean = compare.compareModels("Eminescu", "CompareWith")
    print(f"Score is {score} and mean is {mean}")