# Notes

# Solution 1

Keep track of references using a set, if the next isn't in the set, add it and keep going until you find a null pointer.

# Solution 2

Uses a fast and slow pointer, and the fact that if there is a loop, due to the different travel speeds, the pointers must overlap each other.
