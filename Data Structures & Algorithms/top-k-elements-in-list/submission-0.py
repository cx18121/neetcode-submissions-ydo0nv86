class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        pairs = list(map(lambda x: x[0], (sorted(freq.items(), key = lambda x: x[1]))))
        n = len(pairs)
        return pairs[n - k : n]