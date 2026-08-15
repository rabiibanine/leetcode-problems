# Notes
## Solution 1

## Solution 2
This solution has time complexity O(n + m) and space complexity O(n + m), it consumes each item on each array exactly once and builds a separate sorted array with length n+m, not the most efficient but what I thought of without using binary search, an upgrade would be to abandon the new array and calculate the median when hitting the half of the array.

## Solution 3
This solution is what the previous solution talked about, walking through without building a new array.
