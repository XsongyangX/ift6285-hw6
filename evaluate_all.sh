#!/bin/bash

mkdir -p performances/
for file in $(ls predictions);
do
    python evaluate.py predictions/$file > performances/$file
done