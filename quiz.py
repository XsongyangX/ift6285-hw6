from pickle import load
import sys

with open(sys.argv[1], "rb") as file:
    predictions = load(file)
truth, predicted = predictions

for p in predicted:
    print(p)