# mdp-and-cricket

Repository for the course project done as part of CS-747 (Foundations of Intelligent & Learning Agents) course at IIT Bombay in Autumn 2022.  
Webpage: https://sarthakmittal92.github.io/projects/aut22/mdp-and-cricket/

## Overview
In this assignment, you will write code to compute an optimal policy for a given MDP using the algorithms that were discussed in class: Value Iteration, Howard's Policy Iteration, and Linear Programming.

The first part of the assignment is to implement these algorithms. Input to these algorithms will be an MDP and the expected output is the optimal value function, along with an optimal policy. You also have to add an optional command line argument for the policy, which evaluates the value function for a given policy instead of finding the optimal policy, and returns the action and value function for each state in the same format.

MDP solvers have a variety of applications. As the second part of this assignment, you will use your solver to find an optimal policy for a batter chasing a target during the last wicket in a game of **cricket**.

## Code Structure
[This compressed directory](https://www.cse.iitb.ac.in/~shivaram/teaching/cs747-a2022/pa-2/code.tar.gz) contains a data directory with sample data for both parts and helper functions to visualize and test your code. Your code will also be evaluated on instances other than the ones provided.

## Report
Prepare a short report, in which you put your design decisions, assumptions, and observations about the algorithms (if any) for Task 1. Also describe how you formulated the MDP for the Cricket problem: that is, for Task 2. Finally, include the 3 graphs for Task 2 with your observations.

## Complete Problem
The full problem statement is accessible here: [CS747 Programming Assignment 2](https://hackmd.io/@sarthakmittal/HykvfZGzo)