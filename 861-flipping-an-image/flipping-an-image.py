class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        ans = []
        for i in image:
            row = i[::-1]
            row = [1-x for x in row]
            ans.append(row)
        return ans
