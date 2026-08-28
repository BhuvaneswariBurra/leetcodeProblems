class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix=[0]
        runningSum = 0
        for i in nums:
            runningSum+=i
            prefix.append(runningSum)
        for i in range(n):
            leftSum=prefix[i]
            rightSum=prefix[n]-prefix[i+1]
            if leftSum==rightSum:
                return i
        return -1
        
        