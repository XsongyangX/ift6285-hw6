from pickle import load
import sys
from sklearn.metrics import classification_report

with open(sys.argv[1], "rb") as file:
    predictions = load(file)
truth, predicted = predictions
print(classification_report(truth, predicted))