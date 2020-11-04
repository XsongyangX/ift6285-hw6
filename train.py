import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.neural_network import MLPClassifier
import pandas as pd
import sys
from pickle import dump
from nltk import TweetTokenizer

import csv
csv.field_size_limit(100000000)

# a number of options can control a vectorizer, I reckon you investigate them
tweet = TweetTokenizer()
vectorizer = TfidfVectorizer(tokenizer=tweet.tokenize)

# read from file
train_data = sys.argv[1]
tag = sys.argv[2]
with open(train_data, encoding='utf-8') as file:
    df = pd.read_csv(file,\
        names=['bloggerID', 'gender', 'age', 'blog'], engine="python")

X_train = vectorizer.fit_transform(df['blog'])

# several meta-parameters can influence the performance of Logit (investigate)
clf = MLPClassifier(alpha=1, max_iter=1000)

clf.fit(X_train, df['bloggerID'])

# dump the vectorizer and the model (for use at test time)
os.makedirs("models/", exist_ok=True)

with open("models/tfidf_default-{}.vec".format(tag), "wb") as vec:
    dump(vectorizer, vec)
with open("models/logistic_regression-{}.model".format(tag), "wb") as model:
    dump(clf, model)