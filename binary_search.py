#!/usr/local/bin/python3

import random
import time

# Implementation of binary search algorithm. 

# This is used to speed up searching through a sorted list. 
# Binary search algo. ~ 0(log(n))

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

# if l = [1, 3, 5, 10, 12] it should return 3
midpoint = (low + high) // 2 

# Now we'll test if l[midpoint] == target, 
# If not we'll find out if the target is on the left or the right of the the midpoint
# The algo tells us everything to the left of the midpoint is smaller that the midpoint
# and everything to the right will be bigger
if l[midpoint] == target:
    return midpoint
elif target < l[midpoint]:
    return binary_search(l, target, low, midpoint-1)
else:
# At this point target > l[midpoint]
    return binary_search(l, target, midpoint+1, high)

