class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            a = word.index(ch)
            rev = word[:a+1]
            ans = rev[::-1]
            Ans = ans + word[a+1:]
            return Ans
        else:
            return word