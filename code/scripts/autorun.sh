#!/bin/bash

cd ..
python3 autograder.py --task 1 --algorithm all > ../outputs/task1.txt
python3 autograder.py --task 2 > ../outputs/task2.txt
cd scripts