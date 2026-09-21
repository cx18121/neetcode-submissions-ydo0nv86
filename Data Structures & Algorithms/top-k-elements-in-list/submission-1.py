from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        a = sorted(d.items(), key = lambda item:item[1], reverse = True)
        a = list(map(lambda x:x[0], a[:k]))

        return a
        