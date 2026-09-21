
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set() 
        for i in nums:
            s.add(i)
        res = 0
        for i in nums:
            if i-1 in s:
                continue
            ct = 1
            inc = i + 1
            
            while inc in s:
                ct +=1
                inc += 1
            res = max(res, ct)
        return res
         