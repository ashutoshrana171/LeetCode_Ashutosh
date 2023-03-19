"""
Q:
An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.
"""

class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 1
        current = 1 
        for i in range(1,len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                current+= 1
                start = max(current,start)
            else:
                current = 1

        return start
