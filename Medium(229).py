"""
Q:
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
"""

class Solution(object):
    def majorityElement(self, nums):
        if len(nums) <=1 or nums=="":
            return nums
        result = []
        temp = set(nums)
        [result.append(x) for x in temp if nums.count(x) > len(nums)/3 and x not in result]
        return result
