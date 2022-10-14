#!/usr/bin/python

from subprocess import call
from matplotlib import pyplot as plt

winProbs = []
winProbPols = []
strength = []

winProb = 0.0
winProbPol = 0.0
q = 0.0

# plot 1
call(['./stategen.sh','15','30'])
while q <= 1.0:
    call(['./run.sh',str(q)])
    line = open('policyfile.txt','r').readline()
    winProb = float(line.strip().split()[2])
    call(['./policyrun.sh',str(q),'data/cricket/rand_pol.txt'])
    line = open('policyfile.txt','r').readline()
    winProbPol = float(line.strip().split()[2])
    winProbs.append(winProb)
    winProbPols.append(winProbPol)
    strength.append(q)
    q += 0.1

plt.plot(strength, winProbs)
plt.plot(strength, winProbPols)
plt.title('Win Probability v/s Strength of B')
plt.legend(['Optimal Policy', 'Random Policy'])
plt.xlabel('q (Strength of B)')
plt.ylabel('V (Win Probability)')
plt.savefig('../../plots/plot1.png')
print(winProbs)
print(winProbPols)

call(['./cleaner.sh'])