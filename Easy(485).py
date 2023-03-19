"""
Q:
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        tmax = 0
        for i in nums:
            if i == 1:
                count+=1
                tmax = max(tmax,count)
            else:
                count = 0
        return tmax
