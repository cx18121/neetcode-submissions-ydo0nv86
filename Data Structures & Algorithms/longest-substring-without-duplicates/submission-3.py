class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastPos = {}
        res = 0
        cur = 0
        for i, n in enumerate(s):
            if n in lastPos and lastPos[n] >= i - cur:
                res = max(res, cur)
                cur = i - lastPos[n]
                lastPos[n] = i
            else:
                lastPos[n] = i
                cur += 1
            
        res = max(res, cur)
        return res