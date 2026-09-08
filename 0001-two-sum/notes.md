# Notes

# Solution 1

Brute force, checks every possible combination and returns the indices. O(n^2) time complexity and O(1) space complexity.

# Solution 2

Uses a hash table to store seen numbers, and instantly looks up if they are compatible with the current number at the pointer. O(n) for both time and space.

# Solution 3

Uses quicksort to sort the list, then uses two pointers at each end of the array to look for the solution
