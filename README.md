# Fault Tolerence System design ECSE 422

## Programming Assignment: Communication Network Designer
Here is the problem you need to solve.
You are given N number of cities. You need to design a communication network connecting these cities. The costs of connecting the cities using fiber
optic cables are given. This is called a cost matrix M. M is symmetric. The reliabilities of connecting the cities (i.e., the reliabilities of the fiber optic connections between the cities) are given by the matrix R. Your program needs to output a design to meet the following requirements

### Requirements:
- Meet a given reliability goal.
- Maximize reliability subject to a given cost constraint

### Input
Your program should take a text file as input defining the parameters.
Here is the format of the input file.
N # number of cities
N(N-1)/2 numbers # costs of inter-city connecting
N(N-1)/2 numbers # reliabilities of inter-city connections

### Input sample
```
# this is a comment - skip lines starting with a hash
#
# number of nodes
6
#
# symmetric reliability matrix - stored in row major form
#
0.94 0.91 0.96 0.93 0.92 0.94 0.97 0.91 0.92 0.94 0.90 0.94 0.93 0.96 0.91
#
# symmetric cost matrix - stored in row major form
#
10 25 10 20 30 10 10 25 20 20 40 10 20 10 30
#
# end 
```

### Usage
```
usage: main.py [-h] [-f FILE_PATH] -r RELIABILITY_GOAL -c COST_CONSTRAINT

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_PATH, --input-file FILE_PATH
                        InputFile to work on
  -r RELIABILITY_GOAL, --reliability-goal RELIABILITY_GOAL
                        the reliability goal of the network
  -c COST_CONSTRAINT, --cost-constraint COST_CONSTRAINT
                        the cost constraint of the network
```
