#!/usr/bin/python

from argparse import ArgumentParser as ap

def computeNext(states,s,r): # compute next state
    if s - 100 - min(s % 100,r) in states: # pending runs
        return states[s - 100 - min(s % 100,r)], 0
    if r >= s % 100: # target achieved
        return -1, 1
    return -2, 0 # failed

parser = ap()
parser.add_argument('--states', required = True, type = str, help = 'Path to states file')
parser.add_argument('--parameters', required = True, type = str, help = 'Path to parameters')
parser.add_argument('--q', required = True, type = str, help = 'Strength of player B')

args = parser.parse_args()
statesfile = args.states
paramsfile = args.parameters
q = float(args.q)

lines = open(statesfile,'r').readlines()
S = len(lines)
print(f'numStates {2 * S}') # MDP states for A and B
states = {int(lines[i]):i for i in range(S)} # state list for A
statesB = {int(lines[i]):i + S for i in range(S)} # state list for B

print('numActions 5')
lines = open(paramsfile,'r').readlines()[1:]
actions = {}
actionMap = {0:0, 1:1, 2:2, 4:3, 6:4} # map from indices to runs
for line in lines:
    a = int(line.split()[0])
    pout, p0, p1, p2, p3, p4, p6 = map(float,line.split()[1:])
    actions[actionMap[a]] = {-1:pout, 0:p0, 1:p1, 2:p2, 3:p3, 4:p4, 6:p6} # outcome probabilities

probMapB = {-1:q,0:(1 - q) / 2,1:(1 - q) / 2} # probabilities for B
actionB = {i:probMapB for i in range(5)}

print('end -1 -2')

for s in states: # for A
    over = (s // 100) % 6 == 1 # over up next ball
    for a in actions: # action to attempt
        for r in actions[a]: # runs outcome
            p = actions[a][r]
            if p > 0: # non-zero probability
                if r == -1: # out
                    print(f'transition {states[s]} {a} {-2} {0} {p}')
                elif r % 2 == 0: # even runs
                    if over: # strike change
                        ns, rew = computeNext(statesB,s,r)
                        print(f'transition {states[s]} {a} {ns} {rew} {p}')
                    else:
                        ns, rew = computeNext(states,s,r)
                        print(f'transition {states[s]} {a} {ns} {rew} {p}')
                elif r % 2 == 1: # odd runs
                    if not over: # strike change
                        ns, rew = computeNext(statesB,s,r)
                        print(f'transition {states[s]} {a} {ns} {rew} {p}')
                    else:
                        ns, rew = computeNext(states,s,r)
                        print(f'transition {states[s]} {a} {ns} {rew} {p}')

for s in statesB: # for B
    over = (s // 100) % 6 == 1
    for a in actionB: # action to attempt
        for r in actionB[a]: # runs outcome
            p = actionB[a][r]
            if p > 0: # non-zero probability
                if r == -1: # out
                    print(f'transition {statesB[s]} {a} {-2} {0} {p}')
                elif r == 0: # defend
                    if over: # strike change
                        ns, rew = computeNext(states,s,r)
                        print(f'transition {statesB[s]} {a} {ns} {rew} {p}')
                    else:
                        ns, rew = computeNext(statesB,s,r)
                        print(f'transition {statesB[s]} {a} {ns} {rew} {p}')
                elif r == 1: # single
                    if not over: # strike change
                        ns, rew = computeNext(states,s,r)
                        print(f'transition {statesB[s]} {a} {ns} {rew} {p}')
                    else:
                        ns, rew = computeNext(statesB,s,r)
                        print(f'transition {statesB[s]} {a} {ns} {rew} {p}')

print('mdptype episodic')
print('discount 1.0')