from os.path import basename
import sys, pickle, pandas as pd
from joblib import load
import sys, os

test_set = sys.argv[1]
model_name = sys.argv[2]
vectorizer_name = sys.argv[3]

# 1) read from stdin
with open(test_set, encoding='utf-8') as file:
    df = pd.read_csv(file,\
        names=['bloggerID', 'gender', 'age', 'blog'], encoding="ISO-8859-1", engine="python")

# 2) fit a classifier
clf = load(model_name)
vectorizer = load(vectorizer_name)
X_test = vectorizer.transform(df['blog'])
y = clf.predict(X_test)

# 3) output the predicition
out_dir = "predictions/"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, 
    "{kind}-{vec}-{model}.out".format(vec=os.path.basename(vectorizer_name), 
    model=os.path.basename(model_name),
    kind="closed" if "closed" in test_set else "open"))
with open(out_file, 'wb') as out:
    pickle.dump([df['bloggerID'],y], out)