class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = [0] * 26
        for i in s1:
            l1[ord(i) - ord('a')] += 1
        l2 = [0] * 26
        
        l = 0
        for i, n in enumerate(s2):
            l2[ord(n) - ord('a')] += 1
            if i - l >= len(s1):
                tmp = s2[l]
                l2[ord(tmp) - ord('a')] -= 1
                l +=1
            if l1 == l2:
                return True
        return False