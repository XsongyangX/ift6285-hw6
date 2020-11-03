from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from pickle import load

# Load a good model and its vectorizer from disk

# Accuracy of 80% with f1-score between 50% to 100%, on slice blog-10-100-10
# Logistic regression with C=20
# Tfidf vectorizer with Tweet tokenizer from nltk, without lowercasing

with open("logistic_regression-10-100.model", "rb") as file:
    model : LogisticRegression = load(file)
with open("tfidf_default-10-100.vec", "rb") as file:
    vectorizer : TfidfVectorizer = load(file)
    int_to_feature = vectorizer.get_feature_names()

# Examine coefficients of the feature matrix
for i, author in enumerate(model.classes_):
    print(author, "top features from logistic regression")
    word_importance = [abs(x) for x in model.coef_[i]]
    sorted_word_importance = sorted(zip(word_importance, range(len(model.coef_[i]))),\
        key=lambda x: x[0], reverse=True)
    words = [int_to_feature[word] for _,word in sorted_word_importance[:10]]
    print("\t".join(words))