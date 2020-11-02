#!/bin/bash

# executes all the python scripts on all the data

authors=(10 50 100)
blogs=(10 50 100)

for i in "${authors[@]}"; do 
    for j in "${blogs[@]}"; do

        directory="data/blog-$i-$j-10"            

        python train.py $directory/train.csv "$i-$j"
    done
done