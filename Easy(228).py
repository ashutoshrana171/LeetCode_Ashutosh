"""
Q:
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i< len(nums):
            start = nums[i]
            
            while i < len(nums) - 1 and nums[i] == nums[i+1] - 1:
                i+=1
            end = nums[i]
            
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(end))
            i+=1 

        return result
