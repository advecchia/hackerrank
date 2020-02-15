# [Day 11: 2D Arrays](https://www.hackerrank.com/challenges/30-2d-arrays/problem)

## Objective
Today, we're building on our knowledge of Arrays by adding another dimension. Check out the [Tutorial](https://www.hackerrank.com/challenges/30-2d-arrays/tutorial) tab for learning materials and an instructional video!

## Context
Given a *6 X 6* 2D Array, *A*:

We define an hourglass in *A* to be a subset of values with indices falling in this pattern in *A*'s graphical representation:

There are **16** hourglasses in *A*, and an hourglass sum is the sum of an hourglass' values.

## Task
Calculate the hourglass sum for every hourglass in *A*, then print the maximum hourglass sum.

## Input Format
There are *6* lines of input, where each line contains *6* space-separated integers describing 2D Array *A*; every value in *A* will be in the inclusive range of *-9* to *9*.

## Constraints
* *-9 <= A[i][j] <= 9*
* *0 <= i,j <= 5*

## Output Format
Print the largest (maximum) hourglass sum found in *A*.

## Run
> python3 solution.py