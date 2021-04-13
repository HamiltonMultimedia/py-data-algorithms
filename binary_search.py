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

