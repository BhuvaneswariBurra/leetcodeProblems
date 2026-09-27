class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
       repeated = "" 
       count = 0
       while repeated + word in sequence:
        repeated += word
        count += 1
       return count