#!/usr/bin/python

from subprocess import call
from matplotlib import pyplot as plt

winProbs = []
winProbPols = []
balls = []

winProb = 0.0
winProbPol = 0.0
ball = 15

# plot 3
call(['./stategen.sh','15','30'])
call(['./run.sh','0.25'])
line = open('policyfile.txt','r').readlines()
while ball >= 1:
    winProb = float(line[20 + (15 - ball) * 30].strip().split()[2])
    winProbs.append(winProb)
    ball -=1
ball = 15
call(['./policyrun.sh','0.25'])
line = open('policyfile.txt','r').readlines()
while ball >= 1:
    winProbPol = float(line[20 + (15 - ball) * 30].strip().split()[2])
    winProbPols.append(winProbPol)
    balls.append(ball)
    ball -= 1

plt.plot(balls, winProbs)
plt.plot(balls, winProbPols)
plt.title('Win Probability v/s Balls Remaining')
plt.legend(['Optimal Policy', 'Random Policy'])
plt.xlabel('balls (Balls Remaining)')
plt.ylabel('V (Win Probability)')
plt.gca().invert_xaxis()
plt.savefig('../../plots/plot3.png')
print(winProbs)
print(winProbPols)

call(['./cleaner.sh'])