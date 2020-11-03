#!/bin/bash

# Provide a log file name to store a summary of the performances
if [ $# -ne 1 ]; then
	echo "Usage: ./learn_all.sh name-of-log"
	echo "Ex: ./learn_all.sh accuracies_raw_logistic_tfidf.log"
	exit 1
fi

# Executes the entire NLP pipeline
chmod u+x *.sh
./clean.sh
./train_all.sh
./predict_all.sh
./evaluate_all.sh

# Group performances
mkdir reports
grep "accuracy" performances/* > reports/$1
