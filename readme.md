# IFT 6285 Homework 6
Part of the NLP class.

The code tries to learn the best machine learning model to predict authors from a blog corpus given by the teacher.

# Installation
* python 3
* sklearn, nltk, pandas: either through `pip` or `conda`
* bash shell

## nltk specific
You may need to install additional data for the `nltk` package, even after doing `pip` or `conda`.

# Data: the blog corpus
The blog corpus for this assignment is a subset of the larger blog corpus made by Google. The larger corpus is composed of bloggers and their blogs from the early 2000s, mainly in the English language. Their identities have been anonymized, but the corpus contains complementary meta-data on the authors. They are gender, age and zodiac signs.

The subset corpus is located here: www-labs.iro.umontreal.ca/~felipe/IFT6285-Automne2020/blogs/devoir6.tar.gz

Extract the tar and rename the `devoir6` folder to `data` to suit the scripts. The folder contains many subfolders, which are data slices that are already separated into train-test slices.

## Labels of interest and features
The labels of interest are author anonymized names, contrary to the intended labels of the original corpus.

The features are the blog posts themselves.

The data is organized in a `csv` file, where the last element of each row is the blog post of the author identified in the beginning of the row.

# Running the scripts
The entire learning pipeline is segmented in mainly four sections:
* training: `train.py` and `train_all.sh` (preprocessing is here)
* predicting: `predict.py` and `predict_all.sh`
* evaluating: `evaluate.py` and `evaluate_all.sh`
* examinating: `examine.py` and `examine_all.sh`

The first three sections are all grouped into `learn_all.sh`, which go through the sections one after the other.

## Examination
In order to decide what is the best model, there are the examination scripts `examine.py` and `examine_all.sh`.

* `examine.py`: Computes the min, max and mean of the accuracies in the `grep`-ed report.
  * In order to get the reports digestable by `examine.py`, use 
```bash
grep "accuracies" performances/* > reports/$file #replace $file by your own name
```
* `examine_all.sh`: Performs `examine.py` on the entire directory of reports, grouping into one file called `all_accuracies.log`.

# Results
After trying out many kinds of preprocessing and learning models, I found that the logistic regression classifier coupled with the `nltk` tweet tokenizer and a Tfidf vectorizer works the best, given the right hyperparameters.

Pre-emptive results stand at 80% accuracy for the best data slice, 65% on average.

For this performance, I used a `C` coefficient of 20 inside the logistic regression classifier. The Tfidf vectorizer uses a tweet tokenizer with default settings, but the vectorizer was told to not lowercase everything.

## Insights with logistic regression
Logistic regression has the benefit of being a model that is not a black-box. `sklearn`'s logistic regression has a `coeff_` attribute which gives the coefficient matrix of the features for each class.

By using the best performing slice with logistic regression (80% accuracy on the slice 10-100-10), I found out what influences the decisions of logistic regression the most.

```text
1YX99F2 
?	post	to	name	Here's	that	dun	Rosa	RWBS	show
4VSEFM9 
,	...	or	I	Bad	office	very	Anne	And	chicken
7DEUROP 
...	.	injured	Testing	I'm	urlLink	"	Innocence	,	Beautiful
7JQQ84O 
"	Party	...	of	Satiric	Two	I	To	i	controls
96TQZLJ 
...	!	,	the	Kill	Tom	Jo	Max	thanks	thats
AXNX7FB 
recovery	that	house	Chase	is	Matt	Jim	i	Thy	Book
BGTGOOS 
,	I	!	i	'	it's	"	the	...	you
G04W97J 
~	...	�	,	urlLink	said	;	�	:	-
GM24J1X 
.	was	Alex	Oh	haha	Amanda	I	tho	Today	boring
TA0Q1LV 
i	!	cigarette	I	blah	...	cup	is	coffee	cowgirl
```

So not all words are English words. Punctuation counts as a token for the vectorizer. If logistic regression ranks it as the most deciding feature, then it means that punctuation reveals the identity of the author more than words. Perhaps, the logistic regression classifier has learned the writing styles of these bloggers. After all, it is normal that blogs have more punctuation than a news article. 