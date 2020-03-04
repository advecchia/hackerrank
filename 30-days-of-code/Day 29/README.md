# [Day 29: Bitwise AND](https://www.hackerrank.com/challenges/30-bitwise-and/problem)

## Objective
Welcome to the last day! Today, we're discussing bitwise operations. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-bitwise-and/tutorial) tab for learning materials and an instructional video!

## Task
Given set *S = {1,2,3,...,N}*. Find two integers, *A* and *B* (where *A < B*), from set *S* such that the value of *A&B* is the maximum possible and also less than a given integer, *K*. In this case, *&* represents the bitwise AND operator.

## Input Format
The first line contains an integer, *T*, the number of test cases.

Each of the *T* subsequent lines defines a test case as *2* space-separated integers, *N* and *K*, respectively.

## Constraints
* *1 <= T <= 10^3*
* *2 <= N <= 10^3*
* *2 <= K <= N*

## Output Format
For each test case, print the maximum possible value of *A&B* on a new line.

## Run
> python3 solution.py