"""
Q:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""
class Solution(object):
    def mySqrt(self, x):
        i = 1
        while(i<=x/i):
            if int(x/i) == i:
                return i
            else:
                i+=1
        return i-1
