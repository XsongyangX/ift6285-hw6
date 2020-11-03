#!/bin/bash

# Compiles all min, max and means from the logs
> all_accuracies.log
for file in reports/accuracies*; do
    echo $file >> all_accuracies.log
    python examine.py $file >> all_accuracies.log
done