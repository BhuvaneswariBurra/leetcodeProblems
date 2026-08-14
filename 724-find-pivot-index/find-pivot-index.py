class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]
        runningSum=0 
        for i in nums:
            runningSum+=i
            prefix.append(runningSum)
        n=len(nums)
        for i in range(len(nums)):
            leftSum=prefix[i]
            rightSum=prefix[n]-prefix[i+1]
            if leftSum==rightSum:
                return i
        return -1