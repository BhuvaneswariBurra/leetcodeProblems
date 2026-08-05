class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        maxCount = 1
        for  i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 1
        return max(maxCount, count)