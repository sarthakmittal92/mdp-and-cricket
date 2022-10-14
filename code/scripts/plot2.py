#!/usr/bin/python

from subprocess import call
from matplotlib import pyplot as plt

winProbs = []
winProbPols = []
runs = []

winProb = 0.0
winProbPol = 0.0
run = 20

# plot 2
call(['./stategen.sh','15','30'])
call(['./run.sh','0.25'])
line = open('policyfile.txt','r').readlines()
while run >= 1:
    winProb = float(line[180 - run].strip().split()[2])
    winProbs.append(winProb)
    run -= 1
run = 20
call(['./policyrun.sh','0.25'])
line = open('policyfile.txt','r').readlines()
while run >= 1:
    winProbPol = float(line[180 - run].strip().split()[2])
    winProbPols.append(winProbPol)
    runs.append(run)
    run -= 1

plt.plot(runs, winProbs)
plt.plot(runs, winProbPols)
plt.title('Win Probability v/s Runs to Score')
plt.legend(['Optimal Policy', 'Random Policy'])
plt.xlabel('runs (Runs to Score)')
plt.ylabel('V (Win Probability)')
plt.gca().invert_xaxis()
plt.savefig('../../plots/plot2.png')
print(winProbs)
print(winProbPols)

call(['./cleaner.sh'])