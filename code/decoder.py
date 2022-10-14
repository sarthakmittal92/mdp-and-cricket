#!/usr/bin/python

from argparse import ArgumentParser as ap

parser = ap()
parser.add_argument('--value-policy', required = True, type = str, help = 'Path to value and policy file')
parser.add_argument('--states', required = True, type = str, help = 'Path to states file')

args = parser.parse_args()
vpfile = args.value_policy
statesfile = args.states

lines = open(statesfile,'r').readlines()
S = len(lines)
states = {i:lines[i].strip() for i in range(S)}

actionMap = {0:0, 1:1, 2:2, 3:4, 4:6} # map from indices to runs
lines = open(vpfile,'r').readlines()
for s in states: # print the optimal results
    l = lines[s].split()
    print(f'{states[s]} {actionMap[int(l[1])]} {float(l[0]):.6f}')