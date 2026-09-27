class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s = list(s2.intersection(s1))
        return s 