#Given an array of integers nums, return the value of the largest element in the array
class Solution:
    def largestElement(self, nums):
        max_num = nums[0]
        
        for current in nums:
            if current>max_num:
                max_num = current
        return max_num
        