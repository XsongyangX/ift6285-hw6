#!/bin/bash

# executes all the python scripts on all the data

authors=(10 50 100)
blogs=(10 50 100)

for i in "${authors[@]}"; do 
    for j in "${blogs[@]}"; do

        directory="data/blog-$i-$j-10"            

        if [ $# -eq 1 ] && [ $1 == "distribute" ]; then
            pkscreen -S worker ssh ens -J arcade bash $(pwd)/parallel_train.sh $directory/train.csv $i-$j        
        else
            python train.py $directory/train.csv $i-$j
        fi
    done
done