#!/bin/bash

cd ..
python3 encoder.py --states scripts/states.txt --parameters data/cricket/sample-p1.txt --q "$1" > mdpfile
python3 planner.py --mdp mdpfile > vpfile
python3 decoder.py --states scripts/states.txt --value-policy vpfile > scripts/policyfile.txt
rm mdpfile
rm vpfile
cd scripts