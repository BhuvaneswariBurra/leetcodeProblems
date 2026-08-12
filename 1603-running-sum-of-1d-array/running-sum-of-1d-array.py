class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lst=[]
        runningSum=0
        for i in nums:
            runningSum+=i
            lst.append(runningSum)
        return lst