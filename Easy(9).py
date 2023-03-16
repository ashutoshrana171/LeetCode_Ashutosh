"""
Q: Palindrome Number
Given an integer x, return true if x is a  palindrome, and false otherwise.
"""
class Solution(object):
    def isPalindrome(self, x):
        if not (-2**31 <= x and x <= (2**31 - 1)):
            return 0
        x =str(x)
        return x==x[::-1]
