from collections import defaultdict, deque
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = [0] * 26
        for i in s1:
            l1[ord(i) - ord('a')] += 1
        q = deque()
        l2 = [0] * 26
        print("l1: ", l1)
        for i in s2:
            q.append(i)
            l2[ord(i) - ord('a')] += 1
            if len(q) > len(s1):
                tmp = q.popleft()
                l2[ord(tmp) - ord('a')] -= 1

            if l1 == l2:
                return True
        return False