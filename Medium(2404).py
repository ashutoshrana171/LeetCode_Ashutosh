"""
Q:
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.
"""

class Solution(object):
    def mostFrequentEven(self, nums):
        temp = [x for x in nums if x%2==0]
        temp.sort()
        print(temp)
        if temp == []:
            return -1
        
        tempset = sorted(set(temp))
        maxt = 0
        maxelement = 0
        print(tempset)
        for i in tempset:
            if temp.count(i) > maxt:
                maxelement = i
                maxt = temp.count(i)
        
        return maxelement
