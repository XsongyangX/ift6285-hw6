#!/bin/bash

authors=(10 50 100)
blogs=(10 50 100)

for i in "${authors[@]}"; do 
    for j in "${blogs[@]}"; do

        directory="data/blog-$i-$j-10"            

        python predict.py $directory/test-closed.csv \
            "models/logistic_regression-$i-$j.model" "models/tfidf_default-$i-$j.vec"
        python predict.py $directory/test-open.csv \
            "models/logistic_regression-$i-$j.model" "models/tfidf_default-$i-$j.vec"
    done
done