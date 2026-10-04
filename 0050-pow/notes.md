# Notes

## Solution 1

Normal solution, time limit exceeded, O(n).

## Solution 2

Second solution I thought for big integers n we can save up computation by caching values, accelerating and decelerating.

## Solution 3

Recursive solution, much easier to work with.

## Solution 4

Uses bit information about the power to know what to multiply the result with for every x^(2^n), log_2(n) time complexity.

### Idea

Calculate the biggest number 2^n such that 2^n <= x and use that to find the sequence of power multiplications that sums up to n
