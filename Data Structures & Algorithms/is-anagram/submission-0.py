class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hset = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in hset:
                hset[i] = 1
            else:
                hset[i] += 1

        for i in t:
            if i not in hset:
               return False
            elif hset[i] == 0:
                return False
            else:
                hset[i] -= 1
        return True
