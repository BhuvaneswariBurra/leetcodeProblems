class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAverage = -100000000
        maxAverage = -100000000
        left = 0
        currentSum = 0
        for right in range(len(nums)):
            currentSum += nums[right]
            if right >= k - 1:
                avg = currentSum / k
                maxAverage = max(avg, maxAverage)
                currentSum -= nums[left]
                left += 1
        return maxAverage
