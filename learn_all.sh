#!/bin/bash

# Provide a log file name to store a summary of the performances
if [ $# -ne 3 ] && [ $# -ne 1 ]; then
	echo "Usage: ./learn_all.sh name-of-log [--distribute timeout]"
	echo "Ex: ./learn_all.sh accuracies_raw_logistic_tfidf.log"
    echo "Ex: ./learn_all.sh accuracies_tweet_mlp_tfidf.log --distribute \"1 day\""
    echo "If learning has not ended after the specified timeout, the script moves to prediction phase."
	exit 1
fi

# Executes the entire NLP pipeline
chmod u+x *.sh
./clean.sh

# Distributed
if [ $# -eq 3 ] && [ $2 == "--distribute" ]; then

    ./train_all.sh distribute

    runtime=$3
    endtime=$(date -ud "$runtime" +%s)

    while [[ $(date -u +%s) -le $endtime ]]
    do
        # check if all worker screens have ended
        remaining=$(screen -ls | grep -c "worker")
        if [ $remaining -eq 0 ]; then
            break
        fi
        sleep 10
    done

    ./predict_all.sh
    ./evaluate_all.sh

# Sequential
else
    ./train_all.sh
    ./predict_all.sh
    ./evaluate_all.sh
fi
# Group performances
mkdir reports
grep "accuracy" performances/* > reports/$1

